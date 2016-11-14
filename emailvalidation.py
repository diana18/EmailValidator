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


# Check for @
def testATs(email):
	# Check that there is exactly one @
	numberOfATs = email.count("@")
	if numberOfATs > 1 :
		raise SystemExit("Sorry! There can only be one @ character in a valid email address.")
		
	if "@" not in email:
		raise SystemExit("Sorry! This is not a valid email. Your email must have an @ character.")

	# Check that the @ is not the first or last character
	positionOfAT = email.index("@")
	if positionOfAT is 0:
		raise SystemExit("Sorry! This is not a valid email. Your email cannot start with an @ character.")	

	positionOfLastCharacter = len(email)-1
	if positionOfAT is positionOfLastCharacter:
		raise SystemExit("Sorry! This is not a valid email. Your email cannot end with an @ character.")	


# Check for periods
def testPeriods(email):
	# Partition email into two strings separated by @
	firstPart = email.split("@")[0] 
	lastPart = email.split("@")[1]

	# Check for a period
	if email.count(".") is 0:
		return

	# Check whether the last part has more than 1 period
	numberOfPeriods = lastPart.count(".")
	if numberOfPeriods > 1 :
		raise SystemExit("Sorry! There can only be one dot after the @ in a valid email address.")

	# Check for double periods
	numberOfDoublePeriods = email.count("..")
	if numberOfDoublePeriods > 0 :
		raise SystemExit("Sorry! There cannot be a double period in a valid email address.")

	# Check that the period is not the first or last character of the first part
	positionOfPeriod = email.index(".")
	if positionOfPeriod is 0:
		raise SystemExit("Sorry! This is not a valid email. Your email cannot start with a period.")	

	positionOfLastCharacterOfFirstPart = len(firstPart)-1
	if positionOfPeriod is positionOfLastCharacterOfFirstPart:
		raise SystemExit("Sorry! This is not a valid email. The first part of your email cannot end with a period.")	

# Check length
def testLength(email):
	# Partition email into two strings separated by @
	firstPart = email.split("@")[0] 
	lastPart = email.split("@")[1]

	# Check that the first part is less than 64 characters
	if len(firstPart) > 63:
		raise SystemExit("Sorry! This is not a valid email. The first part of your email is too long.")	

	# Check that the last part is less than 255 characters
	if len(lastPart) > 254:
		raise SystemExit("Sorry! This is not a valid email. The last part of your email is too long.")	

# Input your email
print("Your Very Own Email Validator!")
email = raw_input("Type your email: ")

testATs(email)
testPeriods(email)
testLength(email)

print(email+" is a valid email. We can spam you now! Woo!")



