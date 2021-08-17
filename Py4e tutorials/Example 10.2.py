name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
times={}

for line in handle:
    if not line.startswith('From '): continue
    words=line.split()
    rawtime=words[5].split(":")
    time=rawtime[0]
    times[time]= times.get(time,0) +1
    

for v,k in sorted(times.items()):
    print(v,k)
