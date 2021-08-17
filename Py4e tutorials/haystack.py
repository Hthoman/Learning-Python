import re

name='haystack.txt'
handle=open(name)

intlst=[]

for line in handle:
    line=line.rstrip()
    numbersearch=re.findall('[0-9]+', line)
    if numbersearch==[]: continue
    for i in numbersearch:
        intlst.append(int(i))

total=sum(intlst)
print(intlst)
print(total,len(intlst))