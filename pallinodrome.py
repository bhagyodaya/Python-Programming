


n=int(input("Enter No:"))
r=0
x=n
while n>0:
    s=n%10
    r=r*10+s
    n //=10
print(r)
if x==r:
    print("it is a plainodrome Number")


