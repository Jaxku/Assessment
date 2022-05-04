"""instructions_V1
Base instructions for game in final code this will be used a function so it can be called in with the main routine"""


# this function not apart of this code but is necessary for testing this code and for it to operate this function will be placed appropriately in the final Quiz file
def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


def instructions():
    print()
    print(formatter("*", "Instructions"))
    print()
    print("You will be tested on Maori numbers 1-10 in 10 questions these will be randomized")
    print()
    print("Every question you get right will be 1 point. You need to get 7 points correct to pass.")
    print()
    print("This means you will need to get 7 Questions correct to pass the quiz")
    print()
    print("To answer question simply type in your answer and press enter (This quiz is not case sensitive)")


# main routine (This is required to test the code since the Instructions code is a function)
instructions()
