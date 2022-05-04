"""Welcome_V2
Added input for name"""


def formatter(symbol, text):
    sides = symbol * 3
    formatted_text = f"{sides} {text} {sides}"
    top_bottom = symbol * len(formatted_text)
    return f"{top_bottom}\n{formatted_text}\n{top_bottom}"


print(formatter("-", "Welcome to the Maori Number Quiz!"))
print()
user_name = (input("What is your name? "))  # User inputs their name
print(user_name)  # Prints name will be refined and used for a better purpose in version 3
