"""02_what_is_your_name_v1
added while loop"""

user_name = input("What is your name? ")  # User inputs name
if any( [ i>'z' or i<'a' for i in user_name]):
    print("Error: Contains illegal characters")
elif len(user_name)>15:
    print("Very long string")
