import re
s1="Basha is here"
result=re.match(r"Basha",s1)
print(result.group(0))
print(result)
