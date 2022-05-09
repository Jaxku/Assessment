"""02_what_is_your_name_v1
added while loop"""

import re



user_name = input("What is your name? ")  # User inputs name
if len(user_name) > 35:
    print("Please enter a name under 36 characters.")
if len(user_name) < 1:
    print("Please enter a name")
if not re.complie("^[a-z],[-],[ ]*$", user_name):
    print("Only A-Z and hyphens are allowed!")

