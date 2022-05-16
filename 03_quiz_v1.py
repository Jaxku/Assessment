# Using a template provided I have adjusted it to fit the Maori Number Quiz
import random

# This uses two ordinary (1-dimensional) lists

print("Let's begin.\n"
      "\n"
      "You will be shown numbers in English and you need to convert them into Maori.\n"
      "\n"
      "You don't need to the put the line (macron) over the letter.\n"
      " ")

# 1st list
numbers_english = ["One", "Two", "Three", "Four", "Five", "Six", "Seven", "Eight", "Nine", "Ten"]
# 2nd list
number_maori = ["tahi", "rua", "toru", "wha", "rima", "ono", "whitu", "waru", "iwa", "tekau"]

question = random.choice(numbers_english)
attempt = input(f"What is the Maori number for {question}: ").lower()

# Using the index position of the question in one list to find the corresponding
# index position of the answer
answer_index = numbers_english.index(question)
answer = number_maori[answer_index]
# Compare the attempt to see if it matches the correct answer
if attempt == answer:
    print("##### CORRECT! ######\n")
else:
    print("XXXXX INCORRECT! XXXXX\n")
