"""02_what_is_your_name_v
Limiting character length"""


user_name = input("What is your name? ")  # User inputs name
if len(user_name) > 35:
    print("Please enter a name under 36 characters.")
if len(user_name) < 1:
    print("Please enter a name")

print(user_name)  # testing if program is working so far
