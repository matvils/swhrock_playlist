import sys, os


filepath =  'swh_rock_list.txt'

meklet = []
with open(filepath) as fp: 
    line = fp.readline()
    while line:
        line = fp.readline()
        meklet.append(line.strip())
    
final = []
meklet = meklet[:-1]

jauns = []
fin_list = []
mold=""

for m in meklet:
    start = m.find( '*' )
    garums = len(m)

    if start != -1: 
        result = m[start+2:garums]
    
    if (mold !=m) and (result != "") and (result != "SWHROCK - LIVE") and (result !="SWHROCK - REKLAMA"):    
        jauns.append(result)

for g in jauns:
    if g != mold:
        fin_list.append(g)
        print(g)
    mold = g
