n=int(input("Enter:"))
for i in range(n):
    for j in range(n+n):
        if i ==0 or i == n-1 or i== n-1 or i>=j:
            print("*",end=" ")
        elif j==0 or j==(n+n)-1:
            print("#",end=" ")
        else:
            print(" ",end=" ")
    print(" ")