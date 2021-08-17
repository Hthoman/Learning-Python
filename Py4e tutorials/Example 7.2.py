# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
workingaverage=0.0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    tempdata=(line[20:26])
    tempdata=float(tempdata)
    workingaverage=workingaverage+tempdata

workingaverage=(workingaverage/27)
Average_spam_confidence=workingaverage
print("average spam confidence:", Average_spam_confidence)