import re
s1="chan@gmail.com mailmechanbasha@yahoo.com pythionchan@co.in"
result=re.findall(r"@\w+.(\w+)",s1)
print(result)
