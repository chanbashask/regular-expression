import re
s1="I am learning python with naveen"
result=re.findall(r"[aeiouAEIOU]\W+",s1)
print(result)

