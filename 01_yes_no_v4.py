"""yes_no_checker_v4
This function works fine and gets the job done, but it can work better. May refine it later on.
"""

# yes/no checking function
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
