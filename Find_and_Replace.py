f=open(r"C:\Users\Dell\Desktop\file\info2.txt",'r')
d=f.read().split()
c=0
n=input("Enter Word to Find:")
for i in d:
    if i==n:
        c+=1
if c>=0:
    print("Entered Word Found")
else:
    print("Not Found")
op=input("For Exit Type 'E' and to Replace Any Word Than Type'R' ")
if op=="E":
    f.close()
elif op=="R":
    wd=input("Enter Word to Replace:")
    for i in d:
        if i==n:
            d[d.index(i)]=wd

    b=' '.join(d)
f.close()
a=open(r"C:\Users\Dell\Desktop\file\info2.txt",'w')
a.write(b)


a.close()