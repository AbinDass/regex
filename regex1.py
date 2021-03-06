import re 
txt = input("enter the string : ")
x = re.findall("w.....d*",txt)
print(x)
if x:
	print("have a match ")
else:
	print("No match")
