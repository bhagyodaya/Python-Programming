amt=int(input("Enter the Amount:"))
if amt>=25000:
    print("Congratulations You comes under our Gold Category Customers")
    print("You Get 20% Discount on your Total Amount")
    a=amt*0.2
    print("You have to Pay:",amt-a)
elif 10000<amt<=25000:
    print("Congratulations You comes under our Silver Category Customers")
    print("You Get 10% Discount on your Total Amount")
    a=amt*0.1
    print("You have to Pay:",amt-a)
elif amt<=10000:
    print("Congratulations You comes under our Bronze Customers")
    print("You Get 5% Discount on your Total Amount")
    a=amt*0.05
    print("You have to Pay:",amt-a)