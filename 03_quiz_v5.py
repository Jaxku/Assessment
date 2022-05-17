"""03_quiz_v5
Adding end screen, formatting"""

import random


def formatter(symbol, text):  # Formatter script for text, needed for testing but not directly apart of the quiz function
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


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

play_again = " "
rounds_played = 1
user_score = 0

while rounds_played < 10:  # Limits quiz to 10 rounds
    question = random.choice(numbers_english)
    print(formatter("✓", f"Question {rounds_played}"))
    attempt = input(f"What is the Maori number for {question}: ").lower()

    # Using the index position of the question in one list to find the corresponding
    # index position of the answer
    answer_index = numbers_english.index(question)
    answer = number_maori[answer_index]
    # Compare the attempt to see if it matches the correct answer
    if attempt == answer:
        print(formatter("-", f"CORRECT"))
        print("You have earned 1 point. Good work!")
        user_score = user_score + 1  # gives the user a point for getting the question correct
        print(f"Your current score is {user_score}")
        print(f"You are on round {rounds_played}/10")
        rounds_played += 1  # keep track of rounds
        print()  # adds some spacing between questions
    else:
        print("XXXXX INCORRECT! XXXXX\n")
        print("No points have been awarded, better luck next time.")
        print(f"Your current score is {user_score}")
        print(f"You are on round {rounds_played}/10")
        rounds_played += 1  # keep track of rounds
        print()  # adds some spacing between questions
