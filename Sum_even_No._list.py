from re import I


out=list(map(int,input("Enter:").split()))
s=0
for i in out:
    if i % 2 == 0:
        s=s+i
print(s)