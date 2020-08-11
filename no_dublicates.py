import sys, os

filepath = 'FAILA_NOSAUKUMS.txt'
meklet = []
with open(filepath) as fp: 
    line = fp.readline()
    while line:
        line = fp.readline()
        meklet.append(line.strip())
    

mylist = list(dict.fromkeys(meklet))

for k in mylist:
    print(k)
