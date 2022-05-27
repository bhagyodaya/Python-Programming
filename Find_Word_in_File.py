#to find specific word in the word
f=open(r"C:\Users\Dell\Desktop\file\info2.txt",'r')
d=f.read().split()
n=input("Enter Word to Find:")
c=0
for i in d:
    if i==n:
        c+=1
if c>0:
    print("Find")
    print(f"Enter Word {n} is {c}  times in the file")
f.close()
