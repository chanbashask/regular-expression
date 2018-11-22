import re
st="chan@gmail.com mailmechanbasha@yahoo.com pythionchan@co.in"
result=re.findall(r"@\w+.\w+",st)
print(result)