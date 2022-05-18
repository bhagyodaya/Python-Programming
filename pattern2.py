n=int(input("Enter the No. of Rows:"))
for i in range(n):
    for j in range(i):
            if i==j:
                print("*",end='')
    print("")