num=int(input("Enter the no.:"))
if num%2==0:
    print("Even Number")
else:
    print("Odd Number.")



    #  if else  in single line
    num=int(input("Enter:"))
    print('odd' if num%2 else 'Even')

    #Without if else
    num =int(input("enter the number:"))
    print(['Even','Odd'][num%2])