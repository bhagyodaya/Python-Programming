# sum of all digit of given number
n=int(input("Enter:"))
s=0
while n>0:
    r=n%10
    s=s+r
    n=n//10
 
print(int(s))

#second Way
n= input("Enter the number:")
s=0
for i in n:
    s=s+int(i)
print(s)



