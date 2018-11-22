import re
s1="Chan is from sathya chan is teaching pytho"
result=re.match(r"Chan",s1)
print(result.start())
print("-------------------")
print(result.end())

