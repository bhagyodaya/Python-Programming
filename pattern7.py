n=int(input("Enter:"))
for i in range(n):
    for j in range(n):
        if i==0 and i<=j:
            print("#",end=" ")
        elif i==n-1 and i>=j:
            print("%",end=" ")
        elif j==0 and i>=j:
            print("!",end=" ")
    print()