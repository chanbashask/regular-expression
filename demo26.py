import re
input=input("Enter an input string:")
m=re.match('\d{5}\Z',input)
if m:
    print("True")

else:
    print("False")
