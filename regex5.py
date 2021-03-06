import re 
txt = input("enter the string : ")
x = re.findall("^a.*d$",txt)
print(x)
if x:
	print("have a match ")
else:
	print("No match")
