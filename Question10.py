#Armstrong Number
#number if  153=1^3+5^3+3^3, 1452=1^4+4^4+5^4+2^4
dig=int(input("Enter the digit:"))
for num in range(10**(dig-1),10**dig):
    s=0
    t=num
    while num!=0:
        x= num%10
        s=s+x**dig
        num=num//10
    if t==s:
        print(s)


