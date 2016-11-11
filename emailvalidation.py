# 
# Exercise:
# Write a function to validate an email address.  
# You can use regex or any other method you want, but the function should be able to take in an email address (as a string), 
# and output whether or not it appears to be a valid email address 
# (you can return true or false, a message that says "This is an email" -- whatever). 
#
# My Notes:
# https://en.wikipedia.org/wiki/Email_address
# email format: local-part@domain


# Check that there's exactly one @
def hasexactlyoneAT(email):
	numberofATs = email.count("@")
	if numberofATs > 1 :
		raise SystemExit("Sorry! There can only be one @ character in a valid email address.")
	if "@" not in email:
		raise SystemExit("Sorry! This is not a valid email. Your email must have an @ character.")

# Check that it has no more than one period after the @
def hasnomorethanoneperiod(string):
	numberofperiods = string.count(".")
	if numberofperiods > 1 :
		raise SystemExit("Sorry! There can only be one dot after the @ in a valid email address.")

# Input your email
print("Your Very Own Email Validator!")
email = raw_input("Type your email: ")

hasexactlyoneAT(email)

# Partition email into two strings separated by @
string1 = email.split("@")[0] 
string2 = email.split("@")[1]

hasnomorethanoneperiod(string2)

print(email+" is a valid email. We can spam you now! Woo!")



