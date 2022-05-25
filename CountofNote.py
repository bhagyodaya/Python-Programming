amt=int(input("Enter the Amount:"))


a=amt//2000
amt=amt-a*2000
b=amt//500
amt=amt-b*500
c=amt//200
amt=amt-c*200
d=amt//100
amt=amt-d*100
e=amt//50
amt=amt-e*50
f=amt//20
amt=amt-f*20
g=amt//10
amt=amt-g*10

print("2000:",a,"500:",b,"200:",c,"100:",d,"50:",e,"20:",f,"10:",g)