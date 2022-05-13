"""02_what_is_your_name_v5
based on v3 adding a while loop statement and making it testing ready. final version"""

import re

user_name = ""
while True:
    user_name = input("What is your name? ")  # User inputs name
    if len(user_name) > 35:
        print("Please enter a name under 36 characters.")
    elif len(user_name) < 1:
        print("Please enter a name")
    elif re.match("^[a-zA-Z -]+$", user_name) is None:  # the only type of characters allowed
        print("Only A-Z and hyphens are allowed!")
    else:
        print("you have a normal name")  # prints text (for testing) if the name fits all of the rules
        print(user_name)
        break
