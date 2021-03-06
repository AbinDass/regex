import re
username = input("enter your user name : ")
print("enter lowercase , uppercase , digits ,special chars")
password = input("enter the password : ")
p = (("[a-z]") and ("\d") and ("[$#@]"))
if re.findall(p,password):
	print("success")
else:
	print("enter specified charecters")


