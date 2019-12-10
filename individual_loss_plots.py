import matplotlib.pyplot as plt
import bokeh
#import plotly
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

""" fs """
plt.plot(losses[0][0])
plt.plot(losses[2][0])
plt.ylabel('(loss type one) modified fs vs original fs')
plt.show()

plt.plot(losses[0][1])
plt.plot(losses[2][1])
plt.ylabel('(loss type two) modified fs vs original fs')
plt.show()

plt.plot(losses[0][2])
plt.plot(losses[2][2])
plt.ylabel('(loss type three) modified fs vs original fs')
plt.show()

""" ft """
plt.plot(losses[1][0])
plt.plot(losses[3][0])
plt.ylabel('(loss type one) modified ft vs original ft')
plt.show()

plt.plot(losses[1][1])
plt.plot(losses[3][1])
plt.ylabel('(loss type two) modified ft vs original ft')
plt.show()

plt.plot(losses[1][2])
plt.plot(losses[3][2])
plt.ylabel('(loss type three) modified ft vs original ft')
plt.show()
