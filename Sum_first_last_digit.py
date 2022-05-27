#program to find sum of first and last digit of given number
#with string
num= input("Enter the num:")
sum=int(num[0])+int(num[-1]) if len(num)>1 else int(num)

print(sum)

#without string
num= int(input("Enter:"))
a=num%10
num=num//10
while num>9:
    num=num//10
q=





