import re
input=input("Enter an input string:")
m=re.match('[^@]+@]+\.[^@]+',input)
if m:
    print("String found.")

else:
    print("Nothing found.")
    