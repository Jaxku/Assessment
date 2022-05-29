"""
yes_no_checker_v1
Beginnings of yes/no checker
Basic program, gets the job done but it is not refined.
"""


# Ask the user if they have played before
show_instructions = input('Have you taken this quiz before? (Yes/No): ').lower()

# If they say yes, output "Program Continues"
if show_instructions == 'yes':
    print("Program continues")

# If they say no, output "Display Instructions"
elif show_instructions == 'no':
    print("Instructions for program")

# Otherwise - show error
else:
    print("Error: Please put either Yes or No")
