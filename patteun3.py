n=int(input("Enter:"))
for i in range(1,n+1):
    for j in range(i):
        if j>=0:
            print("*",end='')
    for j in range(n+1-1):
        print(" ",end='')
    for j in range(n+1-i):
        print("*",end='')
    print()