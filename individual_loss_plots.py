import matplotlib.pyplot as plt
import bokeh
import statistics 

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

"""
print("fs lengths: ", len(fs), len(ofs))
ratio_fs = int(len(ofs)/len(fs)) # look below for why floor
print("ft lengths: ", len(ft), len(oft))
ratio_ft = int(len(oft)/len(ft)) # we want it floored so we are guaranteed to get >= points and we can ignore after a point

print(ratio_fs,ratio_ft)

ofs_short = []
oft_short = []


for i in range(0, len(ofs),ratio_fs):
    if(len(ofs_short) == len(fs)):
        break
    else:
        ofs_short.append(ofs[i])

for j in range(0, len(oft),ratio_ft):
    if(len(oft_short) == len(ft)):
        break
    else:
        oft_short.append(oft[j])


ofs = ofs_short
oft = oft_short
"""

for x in range(2, len(losses)):
    x0 = x-2
    for i in range(3):
        short_oft = []
        ofs = losses[x][i] # could also oft this is a bad name and just refers to whichever we look at now
        fs = losses[x0][i]
        ratio_fs = max(int(len(ofs)/len(fs)),1)

        #print(len(ofs), len(fs), len(short_oft), ratio_fs)

        for j in range(0, len(ofs), ratio_fs):
            if(len(short_oft) == len(fs)):
                break
            else:
                short_oft.append(losses[x][i][j])

        # update
        losses[x][i] = short_oft


"""
plt.plot(losses[0][0], label="Modified")
plt.plot(losses[2][0], label="Original")
plt.title('(Depth Consistency Loss) Modified Fs vs Original Fs')
plt.ylabel("Loss")
plt.xlabel("Iteration")
plt.legend()
plt.show()

plt.plot(losses[0][1], label="Modified")
plt.plot(losses[2][1], label="Original")
plt.title('(Depth Smootheness Loss) Modified Fs vs Original Fs')
plt.ylabel("Loss")
plt.xlabel("Iteration")
plt.legend()
plt.show()

plt.plot(losses[0][2], label="Modified")
plt.plot(losses[2][2], label="Original")
plt.title('(Geometry Consistency Loss) Modified Fs vs Original Fs')
plt.ylabel("Loss")
plt.xlabel("Iteration")
plt.legend()
plt.show()
"""

""" ft """

"""
plt.plot(losses[1][0], label="Modified")
plt.plot(losses[3][0], label="Original")
plt.title('(Depth Consistency Loss) Modified Ft vs Original Ft')
plt.ylabel("Loss")
plt.xlabel("Iteration")
plt.show()

plt.plot(losses[1][1], label="Modified")
plt.plot(losses[3][1], label="Original")
plt.title('(Depth Smootheness Loss) Modified Ft vs Original Ft')
plt.ylabel("Loss")
plt.xlabel("Iteration")
plt.legend()
plt.show()

plt.plot(losses[1][2], label="Modified")
plt.plot(losses[3][2], label="Original")
plt.title('(Geometric Consistency Loss) Modified Ft vs Original Ft')
plt.ylabel("Loss")
plt.xlabel("Iteration")
plt.legend()
plt.show()
"""


# skip the first 10 percent of the image because of the dip
geometry_fs = losses[0][2][int(len(fs)/10):]
geometry_ft = losses[1][2][int(len(fs)/10):]
geometry_ofs = losses[2][2][int(len(fs)/10):]
geometry_oft = losses[3][2][int(len(fs)/10):]

stdev_fs = statistics.stdev(geometry_fs)
stdev_ft = statistics.stdev(geometry_ft)
stdev_ofs = statistics.stdev(geometry_ofs)
stdev_oft = statistics.stdev(geometry_oft)

print("fs", stdev_fs, stdev_ofs)
print("ft", stdev_ft, stdev_oft)