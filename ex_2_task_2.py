# Python refresher exercises 2 - task 2

# - as part of some app, the user has to create a valid email address
# - any address will do as long as it's valid
# - your validation will only allow a number of retries if a invalid email is given (default 3)
# - once the number of attempts is exhausted (you should show how many retries are left!), set the
#   variable (flag) gave_up to True and bail out.
# 
# - it's OK to start with my solution from the lecture in flow control, although I 
#   encourage you to try you own solution first (if you can't remember). Any other, working
#   solution is fine, too!
# - when it comes to how to react to an error, your user MUST re-enter a string, but it's up to 
#   you how helpful you want to be:
#   - you could just list all the rules on error and demand a new input
#   - you could list the appropriate error message returned from you function and demand a new input
#   - you could do something fancy and only require re-typing of what's wrong (if that's technically possible):
#       e.g. if the pre @ is wrong (too long, contains a invalid char) you could demand that
#       only that incorrect part is re-entered. Warning - this can be complicated and laborious to test!
# - Note that the check for a valid email is a bit weird (b/c of how I set it up):
#   - iff the first return is None (r == None), the email is valid (yes, None doesn't sound like an OK ...)
#   - if you didn't get None (r != None), then r contains an error code, which you could use in your 
#     flow control for branching, if you want to do something fancy

# Optionally, you can use regex for all this!

# Once you're solved this, run some tests to show me that it works. 
# Again, manually copy/paste the console output in a text file (results2.txt)



# import your function from the previous .py file as a module (you can abbreviate it)
# use ex_2_task_2 here instead once your function works!
from ex_2_task_1 import is_valid_email_address as is_valid 

gave_up = False
attempts_left = 3

# your code - start

while True:
    email = input("Email? ")
    r, s = is_valid(email)

    if r == 'None': # if valid
        print("\nWelcome "+email+"!")
        break
    else: # if invalid
        attempts_left = attempts_left - 1 # decrease attempts

        print(f"\nThe email you entered is invalid: {s}") # give the reason

        if attempts_left > 0: # if there are attempts left
            print(f"\t{attempts_left} attempts left\n") # print how many attempts left
        else: # if out of attempts
            gave_up = True # give up
            print("\tSorry! Out of attempts, try again later.") # print out no attempts left
            break

# your code - end
if not gave_up:
    print("\n\nValid email", email)
else:
    print("\n\nInvalid email", email)
