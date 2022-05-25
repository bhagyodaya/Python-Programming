from os import sep


inp=input("Enter:")
c=dict()
for i in inp:
        if i in c:
            c[i]=c[i]+1
        else :
            c[i]=1
print(c,end="\n")

inp=input("ENter:")
d={}
for i in inp:
    d[i]=inp.count(i)
print(d,sep=":")