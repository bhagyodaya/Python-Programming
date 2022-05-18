n= int(input("Enter:"))
f=1
for i in range(n+1):
    for j in range(i):
        print(f,end=" ")
        f=f+1
        if f>=10:
            f=1
    print()