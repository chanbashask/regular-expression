import re
s1="This is Chan"
result=re.search(r"Chan",s1)
print(result)

print("----------------------")
print(result.group(0))

