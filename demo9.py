import re
st="programming"
result=re.split(r"m",st)
print(result)
print("-------------------------")
result=re.split(r"m",st,maxsplit=1)
print(result)


