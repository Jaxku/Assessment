"""Welcome_V3
Refined name usage and added instructions"""


# Formatter function to make any text a little more interesting
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


# Yes/no checker
def yes_no(question_text):
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


print(formatter("-", "Welcome to the Maori Number Quiz!"))  # Uses the formatter function to make the title card a little more interesting
print()
user_name = (input("What is your name? "))  # User inputs their name
print(f"Welcome {user_name} to the Maori Number Quiz!")
inp

