"""02_what_is_your_name_v3
added while loop and experimented on different ways on how to detect"""

import re

user_name = input("What is your name? ")  # User inputs name
if len(user_name) > 35:
    print("Please enter a name under 36 characters.")
elif len(user_name) < 1:
    print("Please enter a name")
elif re.match("^[a-zA-Z -]+$", user_name) is None:  # the only type of characters allowed
    print("Only A-Z and hyphens are allowed!")
else:
    print("you have a normal name")
