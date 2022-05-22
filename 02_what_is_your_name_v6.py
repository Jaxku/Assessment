
"""02_what_is_your_name_v6
based on v5, refined a loop to make sure that if a user gives an invalid input it can ask them again."""

def name():
    user_name = input("What is your name? ")
    if len(user_name) > 35:
        print("Please enter a name under 36 characters.")
        return False
    elif len(user_name) < 1:
        print("Please enter a name.")
        return False
    elif re.match("^[a-zA-Z -]+$", user_name) is None:  # the only type of characters allowed
        print("Only A-Z and hyphens are allowed!")
        return False
    else:
        return user_name
 
 # (from main loop)
 while True:
    user = name()
    if user:
       break
