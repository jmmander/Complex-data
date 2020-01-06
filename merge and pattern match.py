import re

lista = [5,7,2,6,8,3,1,6,9]
listb = [2,4,5,5,5,4,7,5,4]

listc = sorted(lista+listb)
print(listc)

pat = "^[A-Za-z]\d[A-Za-z]\d[A-Za-z]\d"

stringer = "a1a1a1a1"
match = re.search(pat,stringer)
if match:
    print("True")
