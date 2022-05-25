amt=int(input("Enter the Amount:"))
amt=amt-100
c=amt//2000
amt=amt-c*2000
b=amt//500
amt=amt-b*500

a=amt//100+1


print("2000:",c,"500:",b,"100:",a)



