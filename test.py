import time
import torch.nn
from options.test_options import TestOptions
from data import create_dataloader
from models import create_model
from utils.dataset_util import compute_errors
import numpy as np
import os
from PIL import Image
import cv2
if __name__ == '__main__':
    opt = TestOptions().parse()
    data_loader = create_dataloader(opt)
    dataset_size = len(data_loader)
    print('#test images = %d' % dataset_size)
    
    model = create_model(opt)
    model.setup(opt)
    model.eval()
    
    save_dir = os.path.join('results', opt.model+'_'+opt.suffix+'_'+opt.which_epoch)
    os.makedirs(save_dir)
    
    avg_a1 = 0
    avg_a2 = 0
    avg_a3 = 0
    
    idx = 0
    
    for ind, data in enumerate(data_loader):
        
        model.set_input(data)
        model.test()
        
        visuals = model.get_current_visuals()
        
        gt_depth = np.squeeze(data['depth'].data.numpy())
        pred_depth = np.squeeze(visuals['pred'].data.cpu().numpy())
        
        w = gt_depth.shape[1]
        h = gt_depth.shape[0]
        w0 = pred_depth.shape[1]
        pred_depth = cv2.resize(pred_depth, (w, h), cv2.INTER_CUBIC)
        pred_depth += 1.0
        pred_depth /= 2.0
        
        pred_img = Image.fromarray(pred_depth * 255, mode='I')
        pred_img.save('%s/%05d_pred.png'%(save_dir, ind))
        
        normalized_gt_depth = gt_depth / np.max(gt_depth)
        
        gt_depth_img = Image.fromarray((normalized_gt_depth * 255), mode='I')
        gt_depth_img.save('%s/%05d_gt_depth.png'%(save_dir, ind))
        
        pred_depth[pred_depth<1/80] = 1/80
        
        
        gt_depth[gt_depth<1] = 1
        
        pred_depth *= 80
        
        abs_rel, sq_rel, rmse, rmse_log, a1, a2, a3 = compute_errors(gt_depth, pred_depth)
        avg_a1 += a1
        avg_a2 += a2
        avg_a3 += a3
        
        print(abs_rel, sq_rel, rmse, rmse_log)
        print(a1, a2, a3)
        
        idx += 1
    
    avg_a1 = a1/idx
    avg_a2 = a2/idx
    avg_a3 = a3/idx
    
    print("Overall")
    print(a1, a2, a3)
