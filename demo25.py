import re
user_name=input("name pleace:")
result=re.match("^[A-Za-z]*$",user_name)
if result==None:
    print("invalid name")

else:
    print("Welcome Mr\Miss:",user_name)
    