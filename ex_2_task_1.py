# Python refresher exercises 2 - task 1

# Write and test a function is_valid_email_address(s) that evaluates string s as a valid email address 
# Returns: tuple of 2 elements (res, err):
#          res contains the result (None or error code)
#          err contains an error string ("seems legit" for None,  a short error message for the error code
#
# Rules: (these are mine, not the official web standards!)
# must have 3 parts: <A>@<B>.<C>
# A must have between 3 and 16 alpha numeric chars (test: isalnum()) 
# B must have between 2 and 8 alpha numeric chars (test: isalnum()) 
# C must be one of these:  com edu org gov 
#
# Here are some tests and the expected results:
# 
# charding@iastate.edu (None, 'Seems legit')
# chris.edu (1, 'Must have exactly one @!')
# chris@edu (4, 'post @ part must have exactly one dot!')
# @bla.edu (2, 'pre @ part must contain 3 - 16 alfanum chars')
# throatwobblermangrove@mpfc.org (2, 'pre @ part must contain 3 - 16 alfanum chars')
# chris@X.com (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# chris.harding@iastate.edu (3, 'pre @ part must only contain alfanum chars')
# chris@pymart.biz (7, 'past-dot part invalid, must be from: com, edu, org, gov')
# chris@letsgo!.org (6, 'part after @ and before . must only contain alfanum chars')
# chris@megasavings.org (5, 'part after @ and before . must contain 2 - 8 alfanum chars')
# tc@tank.com (2, 'pre @ part must contain 3 - 16 alfanum chars')
#
# your function MUST react the same (OK or error) but you don't have to use my exact error messages or codes 
# just something similar to that effect. You could even be more helpful e.g. 
# "throatwobblermangrove is too long (21 chars), must be 3 - 16"
# It's OK to bail out at the first proven error, even if there would have been more errors later!
# Also, I prb. forgot some possible edge cases, please add more if needed!

# As proof, please manually copy/paste the console output for one run into a file called
# results1.txt

def is_valid_email_address(s):
    
    # your code here
    def result(code):
        errors = {
            "AtMissing":"Missing '@' symbol",
            "DomainExtensionMissing":"Missing domain extension",
            "DomainExtensionInvalid":"Domain extension not in 'com edu org gov'",
            "DomainNameMissing":"Missing domain name",
            "DomainNameInvalid":"Domain name must have between 2 and 8 alpha numeric characters",
            "UsernameMissing":"Missing username",
            "UsernameInvalid":"Username must have between 3 and 16 alpha numeric characters",
            "None":"Seems legit"
        }
        return [code, errors[code]]

    # check for missing @
    at_pos = s.find('@')
    if at_pos == -1:
        return result("AtMissing")

    # check for domain extension
    has_domext = s[-4]
    if has_domext != '.':
        return result("DomainExtensionMissing")

    # check for valid domain extension
    domains = ["com", "edu", "org", "gov"]
    domain = s[-3:]
    if domain not in domains:
        return result("DomainExtensionInvalid")

    # check for missing domain name
    domain_name = s[at_pos+1:-4]
    if domain_name == '':
        return result("DomainNameMissing")

    # check for invalid domain name length
    if len(domain_name) < 2 or len(domain_name) > 8:
        return result("DomainNameInvalid")

    # check for invalid domain name chars
    if domain_name.isalnum() == False:
        return result("DomainNameInvalid")

    # check for missing username
    username = s[:at_pos]
    if username == '':
        return result("UsernameMissing")

    # check for invalid username length
    if len(username) < 3 or len(username) > 16:
        return result("UsernameInvalid")

    # check for invalid username chars
    if username.isalnum() == False:
        return result("UsernameInvalid")

    # checks out
    return result("None")


    

# This if ensures that the following is NOT run if this file was imported as a module (which we'll do next!)
if __name__ == "__main__":

    # tests, including edge cases (incomplete? add more!)
    email_list = ["charding@iastate.edu", 
        "chris.edu",
        "chris@edu",
        "@bla.edu",
        "throatwobblermangrove@mpfc.org", 
        "chris@X.com",
        "chris.harding@iastate.edu",
        "chris@pymart.biz",
        "chris@letsgo!.org",
        "chris@megasavings.org",
        "tc@tank.com"
        ]
    # validate each email from the list
    for e in email_list:
        r, s = is_valid_email_address(e) 
        if r == None:
            print(e, s) # OK
        else:
            print(f"{e} - error: {s}, error code: {r}") # Error

        
