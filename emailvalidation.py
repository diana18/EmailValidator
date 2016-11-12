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
def testATs(email):
	numberOfATs = email.count("@")
	if numberOfATs > 1 :
		raise SystemExit("Sorry! There can only be one @ character in a valid email address.")
	if "@" not in email:
		raise SystemExit("Sorry! This is not a valid email. Your email must have an @ character.")

# Check for periods
def testPeriods(string):
	numberofperiods = string.count(".")
	# Check whether it has more than 1 period
	if numberofperiods > 1 :
		raise SystemExit("Sorry! There can only be one dot after the @ in a valid email address.")

# Input your email
print("Your Very Own Email Validator!")
email = raw_input("Type your email: ")

testATs(email)

# Partition email into two strings separated by @
string1 = email.split("@")[0] 
string2 = email.split("@")[1]

testPeriods(string2)

print(email+" is a valid email. We can spam you now! Woo!")



