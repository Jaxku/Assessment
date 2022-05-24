"""Maori_Quiz_Final
Final File, fixed PEP8, added more comments"""

import re
import random


# function to format text output
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Allows users to input name
def name():
    user_name = input("What is your name? ")  # input for name
    if len(user_name) > 35:
        # checks name if they are at the limit of characters
        print("Please enter a name under 36 characters.")
        return False
    elif len(user_name) < 1:
        print("Please enter a name.")  # if the user inserting nothing
        return False
    elif re.match("^[a-zA-Z -]+$", user_name) is None:
        # the only type of characters allowed
        print("Only A-Z and hyphens are allowed!")
        return False
    else:
        return user_name
        # if the name fits all of the rules it returns the name


# yes/no checking function for instructions
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        yes_responses = ["yes", "a", "ae", "y", "true"]
        no_responses = ["no", "kao", "n", "false"]
        # supports english and te reo maori

        # If they say yes, output "Program Continues"
        if answer in yes_responses:
            return True

        # If they say no, output "Display Instructions"
        if answer in no_responses:
            return False

        # Otherwise - show error
        print("Error: Please put either Yes or No in English or Te Reo Maori.")


# Instructions for the quiz
def instructions():
    print()
    print(formatter("*", "Instructions"))
    print()
    print("You will be tested on Maori numbers 1-10 in"
          " 10 questions these will be randomized")
    print()
    print("Every question you get right will be 1 point. "
          "You need to get 7 points correct to pass.")
    print()
    print("This means you will need to get 7 "
          "Questions correct to pass the quiz")
    print()
    print("To answer question simply type in "
          "your answer and press enter (This quiz is not case sensitive)")
    # Print statements take up two to fit PEP8 standards


#  Quiz also contains score checker
def quiz():
    # This uses two ordinary (1-dimensional) lists
    print("Let's begin.\n"
          "\n"
          "You will be shown numbers in English "
          "and you need to convert them into Maori.\n"
          "\n"  # used to space out each line by another line
          "You don't need to the put the line"
          " (macron) over the letter.\n"
          " ")  # Briefing the user on what is about to happen in the test
    # Print statements take up two lines to fit PEP8 standards

    # 1st list
    numbers_english = ["One", "Two", "Three", "Four", "Five",
                       "Six", "Seven", "Eight", "Nine", "Ten"]
    # 2nd list
    number_maori = ["tahi", "rua", "toru", "wha", "rima", "ono",
                    "whitu", "waru", "iwa", "tekau"]

    rounds_played = 1
    user_score = 0

    while rounds_played < 11:  # Limits quiz to 10 rounds
        question = random.choice(numbers_english)

        print(formatter("-", f"Question {rounds_played}"))
        attempt = input(f"What is the Maori number for {question}: ").lower()

        # Using the index position of the question
        # in one list to find the corresponding
        # index position of the answer
        answer_index = numbers_english.index(question)
        answer = number_maori[answer_index]

        # Compare the attempt to see if it matches the correct answer
        if attempt == answer:
            print(formatter("✓", f"CORRECT"))
            print("You have earned 1 point. Good work!")
            user_score = user_score + 1
            # gives the user a point for getting the question correct
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

        del numbers_english[answer_index]
        del number_maori[answer_index]

    print("You finished the quiz! "
          "Give yourself a pat on the back")
# Print statements take up two lines to fit PEP8 standards

    # gives user a special message if they get 10/10 on the quiz
    if user_score == 10:
        print(formatter("✓", f"Congratulations {user}, you got"
                        f" a perfect score of 10!"))
        # Print statements take up two lines to fit PEP8 standards

    # checks if user scored more than the minimum to pass the test
    # The minimum score to pass is six
    elif user_score > 6:
        print(formatter("✓", f"Congratulations {user}, you passed the test!"))
        print(f"You scored {user_score}/10")

    # if the user fails
    else:
        print(formatter("x", f"YOU FAILED"))
        print(f"Sorry {user}, but you failed. You needed to answer"
              f" 7 or more questions correctly to pass")  # if user fails

    print(f"Your final score was {user_score}/10")


# Main routine
# Initial welcome
print(formatter("-", "Welcome to the Maori Number Quiz"))
print()
while True:
    user = name()
    if user:
        break
print(f"Welcome to the Maori Number Quiz, {user}")
# Ask if the user requires instructions,
# call the instructions function if needed
show_instructions = yes_no("Have you played this "
                           "game before? (Yes/No): ")
if not show_instructions:
    instructions()
    print()
# In initial quiz prompt
while True:
    player_ready = yes_no("Are you ready to play? (Yes/No): ")
    if player_ready:
        quiz()
        break
# Quiz loop with a different question for
# if they would like to take the quiz again
while True:
    player_ready = yes_no("Are you ready to "
                          "play again? (Yes/No): ")
    if player_ready:  # See if the player would like to play again.
        # If they would, run the quiz function,
        # otherwise break with a goodbye message
        quiz()
    else:
        print(formatter("*", "Goodbye"))
        break
