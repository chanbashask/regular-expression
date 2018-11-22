import re
st="chan@gmail.com mailmechanbasha@yahoo.com pythionchan@co.in"
result=re.findall(r"@\w+",st)
print(result)
