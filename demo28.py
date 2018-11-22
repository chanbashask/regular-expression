import re
input="Contact me by mailmechanbasha@gamil.com or at the office."
m=re.search('[^@]+@[^@]+\.[^@]+',input)
if m:
    print("String found.")

else:
    print("Nothong found.")
