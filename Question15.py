#prime no without loop

n=int(input("Enter:"))
c="prime"
d="not prime"
b=[c,d][n%2!=0 and n%1==0]
print(b)