# Program to Merge two Python Dictionaries
n1=input("Enter 1 Name:")
n2=input("Enter 2 Name:")
n5=input("Enter Roll NO.:")
n3={'name':n1}
n4={'name':n2,'Roll No.':n5}
for i in n4:
    n3[i]=n4[i]
print(n3)
