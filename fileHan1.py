from unicodedata import name


a=open(r"C:\Users\Dell\Desktop\file\info.txt",'w')
name=input("Enter name:")
section=input("Enter Section:")
rollNo=int(input("Roll No:"))
st=f'''
        Name:{name}
        Section:{section}
        Roll No.:{rollNo}'''
a.write(st)
a.close()