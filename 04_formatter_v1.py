"""Component 5 - statement formatter v1
"""

symbol = "-"
text = "Welcome to the Maori Number Quiz"
sides = symbol * 3

formatted_text = f"{sides} {text} {sides}"
top_bottom = symbol * len(formatted_text)

print(top_bottom)
print(formatted_text)
print(top_bottom)
