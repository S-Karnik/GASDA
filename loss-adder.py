# sample file to get format:
"""
(epoch: 1, iters: 32, lr: 1.000000e-04, time: 0.501, data: 2.045) R_Depth_Src: 1.791482 S_Depth_Tgt: 0.004090 R_Img_Tgt: 0.931685
(epoch: 1, iters: 64, lr: 1.000000e-04, time: 0.507, data: 0.000) R_Depth_Src: 1.076508 S_Depth_Tgt: 0.002815 R_Img_Tgt: 0.953709
(epoch: 1, iters: 96, lr: 1.000000e-04, time: 0.513, data: 0.000) R_Depth_Src: 0.776601 S_Depth_Tgt: 0.002751 R_Img_Tgt: 0.648530
(epoch: 1, iters: 128, lr: 1.000000e-04, time: 0.520, data: 0.000) R_Depth_Src: 1.019340 S_Depth_Tgt: 0.001453 R_Img_Tgt: 0.900342
(epoch: 1, iters: 160, lr: 1.000000e-04, time: 0.529, data: 0.000) R_Depth_Src: 0.635303 S_Depth_Tgt: 0.000968 R_Img_Tgt: 0.912626
(epoch: 1, iters: 192, lr: 1.000000e-04, time: 0.537, data: 0.000) R_Depth_Src: 0.536452 S_Depth_Tgt: 0.001892 R_Img_Tgt: 0.882364
(epoch: 1, iters: 224, lr: 1.000000e-04, time: 0.551, data: 0.000) R_Depth_Src: 1.128218 S_Depth_Tgt: 0.001678 R_Img_Tgt: 0.676509
(epoch: 1, iters: 256, lr: 1.000000e-04, time: 0.552, data: 0.000) R_Depth_Src: 0.496064 S_Depth_Tgt: 0.000992 R_Img_Tgt: 0.841776
(epoch: 1, iters: 288, lr: 1.000000e-04, time: 0.561, data: 0.000) R_Depth_Src: 0.660709 S_Depth_Tgt: 0.000897 R_Img_Tgt: 0.729915
(epoch: 1, iters: 320, lr: 1.000000e-04, time: 0.571, data: 0.000) R_Depth_Src: 0.546880 S_Depth_Tgt: 0.000982 R_Img_Tgt: 0.751556
(epoch: 1, iters: 352, lr: 1.000000e-04, time: 0.578, data: 0.000) R_Depth_Src: 0.416950 S_Depth_Tgt: 0.000980 R_Img_Tgt: 0.825165
(epoch: 1, iters: 384, lr: 1.000000e-04, time: 0.591, data: 0.000) R_Depth_Src: 0.314563 S_Depth_Tgt: 0.001143 R_Img_Tgt: 0.883379
(epoch: 1, iters: 416, lr: 1.000000e-04, time: 0.598, data: 0.000) R_Depth_Src: 0.692782 S_Depth_Tgt: 0.000828 R_Img_Tgt: 0.808506
(epoch: 1, iters: 448, lr: 1.000000e-04, time: 0.598, data: 0.000) R_Depth_Src: 0.724772 S_Depth_Tgt: 0.000828 R_Img_Tgt: 0.882798
(epoch: 1, iters: 480, lr: 1.000000e-04, time: 0.603, data: 0.000) R_Depth_Src: 0.567331 S_Depth_Tgt: 0.000911 R_Img_Tgt: 0.909565 

"""

# in order shown in the file
import re
losses = []

FILENAME = "sample_losses.txt"

with open(FILENAME) as file:
    for line in file:
        text = line[1:-1] # get rid of newline and (
        texts = text.split(")")
        #blocks = re.split("[A-Za-b0-9_]+ \s [0-9.]+", texts[1])
        blocks = texts[1].split(" ")[1:] # get rid of the first space and split
        loss = 0
        for i in range(1,len(blocks),2):
            loss += float(blocks[i])
        losses.append(loss)
#print(losses)