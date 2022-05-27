f=open(r"C:\Users\Dell\Desktop\file\info.txt",'r')
data=f.readlines()
print(max(data,key=len))