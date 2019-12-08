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