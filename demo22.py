import re
s1="Hi 007 this 001 from python"
result=re.findall(r"\d",s1)
print(result)