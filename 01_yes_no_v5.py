"""yes_no_checker_v5
This is the final version of the yes/no checker this version is a function and can be used anywhere in the code
unlike the other versions which were developed with function in mind which is to ask if they have played the quiz before
which was good for testing. Now supports Te Reo Maori as well as English since this is a Maori quiz."""


# yes/no checking function for instructions
def yes_no(question_text):
    while True:

        # Ask the user if they have played before
        answer = input(question_text).lower()

        yes_responses = ["yes", "a", "ae", "y", "true"]  # supports english and te reo
        no_responses = ["no", "kao", "n", "false"]  # supports english and te reo

        # If they say yes, output "Program Continues"
        if answer in yes_responses:
            return True

        # If they say no, output "Display Instructions"
        if answer in no_responses:
            return False

        # Otherwise - show error
        print("Error: Please put either Yes or No in English or Te Reo Maori.")
