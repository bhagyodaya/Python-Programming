


def prime(x):
    c=0
    for i in range(1,x+1):
        if x%i==0:
            c+=1
    if c==2:
            return True
    else:
            return False
st=eval(input("Enter:"))
re1=[]
re2=[]
test=str(st)
for i in test:
    if prime(int(i)):
        re1.append(i)
    else:
        re2.append(i)
re1.sort()
r=''.join(re1+re2)
print(f"{r}")