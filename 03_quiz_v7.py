"""03_quiz_v7
Tells user the final score
Deletes questions after they have been asked so they are not reused
Based on 03_quiz_v6
"""

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

        del numbers_english[answer_index]
        del number_maori[answer_index]

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

    print(f"Your final score was {user_score}/10")
