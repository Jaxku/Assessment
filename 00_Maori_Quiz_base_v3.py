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
        show_instructions = ""
        while show_instructions != "x":
            # Ask the user if they have played before
            show_instructions = input('Have you taken this quiz before? (Yes/No): ').lower()

            # If they say yes, output "Program Continues"
            if show_instructions == 'yes' or show_instructions == "y":
                print("-Program continues-")
                break

            # If they say no, output "Display Instructions"
            elif show_instructions == 'no' or show_instructions == "n":
                print("-Instructions for program-")

            # Otherwise - show error
            else:
                print("Error: Please put either Yes or No")

            print(f"You entered '{show_instructions}'")


# Instructions for the quiz


# main routine
print(formatter("-", "Welcome to the Maori Number Quiz\n"))
user = input("What is your name? ")
name(user)
print(f"Welcome to the Maori Number Quiz {user}")
show_instructions = yes_no("Have you played this game before? (Yes/No): ")

if show_instructions == "No":
    instructions()
