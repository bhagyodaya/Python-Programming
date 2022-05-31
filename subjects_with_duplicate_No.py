m={'math':'34','Python':'19','English':'34'}
o={}
for i in m.values():
    o[i]=[]
for i in m.keys():
    x=m[i]
    o[x].append(i)
for i in o:
    if len(o[i])>1:
        print(i,o[i])