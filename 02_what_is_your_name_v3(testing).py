"""02_what_is_your_name_v3 testing
experimenting"""

user_name = input("What is your name? ")  # User inputs name
if any( [ i>'z' or i<'a' for i in user_name]):
    print("Error: Contains illegal characters")
elif len(user_name)>15:
    print("Very long string")
