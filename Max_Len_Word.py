f=open(r"C:\Users\Dell\Desktop\file\info.txt",'r')
da=f.read().split()
print(max(da,key=len))