x = list(map(int, input("Enter multiple values: ").split(",")))
print("List of students: ", x)
q=1
for i in x:
    q=q*i
    print(q,end=',')
