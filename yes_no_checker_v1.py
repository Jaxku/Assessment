"""yes_no_checker_v1
Yes no checker"""

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
