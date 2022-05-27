#multiple longest word
f=open(r"C:\Users\Dell\Desktop\file\info.txt",'r')
da=f.read().split()
wr=max(da,key=len)
b=[]
for i in da:
    if len(i)==len(wr):
     b.append(i)
print(b)