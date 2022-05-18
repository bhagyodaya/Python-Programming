n=int(input("Enter the Number of Rows:"))
for i in range(n):
    for j in range(n-i):
        print(" ",end='')
    for j in range(i-1):
        print("*",end='')
    for i in range(i):
        print("*",end='')
    print()
for i in range(n):
    for j in range(i):
        print(' ',end="")
    for j in range(n-i):
        print("*",end="")
    for j in range(n-i-1):
        print("*",end='')
    print()
