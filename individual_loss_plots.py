"""
file1(loss_type1, loss_type2, loss_type3),
file2(loss_type1, loss_type2, loss_type3),
file3(loss_type1, loss_type2, loss_type3),
file4(loss_type1, loss_type2, loss_type3)
"""
losses = [[[],[],[]], [[],[],[]], [[],[],[]], [[],[],[]]] # 4 for file then 3 for each loss type

files = ["modified_fs_loss_log.txt", "modified_ft_loss_log.txt", "original_fs_loss_log.txt", "original_ft_loss_log.txt"]

for i in range(len(files)):
    filename = files[i]
    with open(filename) as file:
        for line in file:
            text = line[1:-1] # get rid of newline and (
            texts = text.split(")")
            #blocks = re.split("[A-Za-b0-9_]+ \s [0-9.]+", texts[1])
            blocks = texts[1].split(" ")[1:] # get rid of the first space and split
            which_one = 0
            for j in range(1,len(blocks),2):
                losses[i][which_one].append(float(blocks[j]))
                which_one += 1
print(losses[0][0])
