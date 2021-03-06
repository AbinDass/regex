import re 
txt = input("enter the string : ")
x = re.findall("^[a-z]+_[a-z]+$",txt)
print(x)
if x:
	print("have a match ")
else:
	print("No match")

# import re
# def lower(txt):
# 	p = "^[a-z]+_[a-z]+$"
# 	if re.search(p,txt):
# 		return "found a match"
# 	else:
# 		return "not found a match"

# print(lower("aabc_vvvc"))
# print(lower("aAb_cvvvc"))
# print(lower("aab_cvXvvc"))
