n={"name":"bhagyodaya","roll no.":45,"section":"H"}
c={}
v=45
for i in n.copy():
    if n[i]==v:
        n.pop(i)
print(n)