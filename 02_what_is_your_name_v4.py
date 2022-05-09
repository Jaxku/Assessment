"""02_what_is_your_name_v4
experimenting with a different method"""

import asciiletters

user_name = input("What is your name? ")  # User inputs name
AllowedCharacters = asciiletters.extend([" ", "-"]) #allowed characters
In = False
for Letter in user_name:
    if Letter not in AllowedCharacters :
        In = True
        break
