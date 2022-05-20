def anagram():
    a=sorted(str1)
    b=sorted(str2)
    if a==b:
         print(f"Enter both Letter {str1} and {str2} are Anagram")
    else:
        print(f"Enter both Letter {str1} and {str2} are not Anagram")
str1=input("Enter the 1 string:")
str2=input("ENter the 2 string:")
anagram()
