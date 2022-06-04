l=list(input("Enter:").split(" "))
c=[]
for i in l:
    if i not in  c:
        c.append(i)
c.sort()
b=' '.join(c)
print(b)
    