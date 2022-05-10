"""yes_no_checker_v1
Adding instructions, name checker"""

import re


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Allows users to input name
def name(user_name):
    while True:
        if len(user_name) > 35:
            print("Please enter a name under 36 characters.")
        elif len(user_name) < 1:
            print("Please enter a name")
        elif re.match("^[a-zA-Z -]+$", user_name) is None:  # the only type of characters allowed
            print("Only A-Z and hyphens are allowed!")
        else:
            break


# yes/no checking function for instructions
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        # If they say yes, output "Program Continues"
        if answer == 'yes' or answer == "y":
            answer = "Yes"
            return answer

        # If they say no, output "Display Instructions"
        elif answer == 'no' or answer == "n":
            answer = "No"
            return answer

        # Otherwise - show error
        else:
            print("Error: Please put either Yes or No")


# Instructions for the quiz
def instructions():
    print()
    print(formatter("*", "Instructions"))
    print()
    print("You will be tested on Maori numbers 1-10 in 10 questions these will be randomized")
    print()
    print("Every question you get right will be 1 point. You need to get 7 points correct to pass.")
    print()
    print("This means you will need to get 7 Questions correct to pass the quiz")
    print()
    print("To answer question simply type in your answer and press enter (This quiz is not case sensitive)")


# main routine
print(formatter("-", "Welcome to the Maori Number Quiz"))
print()
user = input("What is your name? ")
name(user)
print(f"Welcome to the Maori Number Quiz {user}")
show_instructions = yes_no("Have you played this game before? (Yes/No): ")

if show_instructions == "No":
    instructions()
    print()
while True:
    player_ready = yes_no("Are you ready to play? (Yes/No): ")
    if player_ready == "Yes":
        print("player ready")
        break
