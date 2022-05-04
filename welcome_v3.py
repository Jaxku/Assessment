"""Welcome_V3
Refined name usage and added instructions. This code (besides the formatter and yes_no functions won't be a function and will be used in the main routine"""

# Functions are needed for the code to work and test


# Formatter function to make any text a little more interesting
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Yes/no checker
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


print(formatter("-", "Welcome to the Maori Number Quiz!"))  # Uses the formatter function to make the title card a little more interesting
print()
user_name = (input("What is your name? "))  # User inputs their name
print(f"Welcome {user_name} to the Maori Number Quiz!")

show_instructions = yes_no("Have you played this quiz before")
if show_instructions == "No":
    print("-Instructions will show-")  # in the final code this line will be replaced with "instructions()" so the code and pull the instructions function
