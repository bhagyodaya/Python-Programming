#to count no.of lower and upper case alphabetes and digits in the text file
# to copy text from sample.txt to data.txt
f=open(r"C:\Users\Dell\Desktop\file\info2.txt",'r')
lower= 0 
upper=0
digits=0
da=f.read()
print(da)
for i in da:
    if i>='a' and i<='z':
        lower+=1
    elif i>='A' and i<='Z':
        upper+=1
    elif i>='0' and i<='9':
        digits+=1
print("l:",lower)
print("U:",upper)
print("D:",digits)
