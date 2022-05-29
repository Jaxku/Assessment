"""Maori_quiz_base_v4
Adding quiz"""

import re
import random


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


#  Quiz also contains score checker
def quiz():
    # This uses two ordinary (1-dimensional) lists
    print("Let's begin.\n"
          "\n"
          "You will be shown numbers in English and you need to convert them into Maori.\n"
          "\n"  # used to space out each line by another line
          "You don't need to the put the line (macron) over the letter.\n"
          " ")  # Briefing the user on what is about to happen in the test

    # 1st list
    numbers_english = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
    # 2nd list
    number_maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

    rounds_played = 1
    user_score = 0

    while rounds_played < 11:  # Limits quiz to 10 rounds
        question = random.choice(numbers_english)
        print(formatter("-", f"Question {rounds_played}"))
        attempt = input(f"What is the Maori number for {question}: ").lower()

        # Using the index position of the question in one list to find the corresponding
        # index position of the answer
        answer_index = numbers_english.index(question)
        answer = number_maori[answer_index]
        # Compare the attempt to see if it matches the correct answer
        if attempt == answer:
            print(formatter("✓", f"CORRECT"))
            print("You have earned 1 point. Good work!")
            user_score = user_score + 1  # gives the user a point for getting the question correct
            print(f"Your current score is {user_score}")
            print(f"You are on round {rounds_played}/10")
            rounds_played += 1  # keep track of rounds
            print()  # adds some spacing between questions
        else:
            print(formatter("x", f"INCORRECT"))
            print("No points have been awarded, better luck next time.")
            print(f"Your current score is {user_score}")
            print(f"You are on round {rounds_played}/10")
            rounds_played += 1  # keep track of rounds
            print()  # adds some spacing between questions

    print("You finished the quiz! Give yourself a pat on the back")

    # gives user a special message if they get 10/10 on the quiz
    if user_score == 10:
        print(formatter("✓", f"Congratulations you got a perfect score of 10!"))

    # checks if user scored more than the minimum to pass the test.
    elif user_score > 7:
        print(formatter("✓", f"Congratulations you passed the test!"))
        print(f"You scored {user_score}/10")

    # if the user fails
    else:
        print(formatter("x", f"YOU FAILED"))
        print(f"Sorry {user}, but you failed you needed to answer 7 or more questions correctly to pass")  # if user fails


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
    player_ready = yes_no("Are you ready to play? (Yes/No): ").lower()  # added lower as some users may be typing in all caps
    if player_ready == "yes":
        quiz()
        print(formatter("*", "Goodbye"))
        break
