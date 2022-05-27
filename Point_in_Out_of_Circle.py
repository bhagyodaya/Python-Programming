r=int(input("Enter radius:"))
x1c=int(input("Enter X of Center:"))
x2c=int(input("Enter Y of Center:"))
x1a=int(input("Enter X of Point:"))
x2a=int(input("Enter Y of Point:"))

out= ((x1a-x1c)**2+(x2a-x2c)**2)**0.5

if out>r:
    print("Out the Circle")
elif out<r:
    print("In the circle")
else:
    print("On the circle")