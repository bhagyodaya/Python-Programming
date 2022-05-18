
n=int(input("Enter the Number of Rows:"))
for i in range(n+1):
    for j in range(n+1-i):
        print("&",end=' ')
        for j in range(i):
            print("*",end=' ')
    print()