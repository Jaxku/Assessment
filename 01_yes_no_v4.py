"""yes_no_checker_v3
This is the final version of the yes/no checker this version is a function and can be used anywhere in the code
unlike the other versions which were developed with function in mind which is to ask if they have played the quiz before
which was good for testing."""

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
