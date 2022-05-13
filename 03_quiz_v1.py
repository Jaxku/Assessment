import random
def get_name():
    name_local=input("What is your name: ")
    return name_local
def get_age():
    age_local=int(input("How old are you: "))
    return age_local
#Main routine
name=get_name ()#1st function
age=get_age()#2nd function
print(f"\nHi {name}. At {age} years old, you might find thisabit easy. \n"
      "\nAnyway, this isatest about days of the week. \n"
      "You will need to enter the abbreviation which applies
      "e.g. Fri for Friday \n")
days=[["Monday", "Mon"], ["Tuesday", "Tue"], ["Wednesday", "Wed"]]
random.shuffle(days)
foriin days:
    answer=input (f"Enter the abbreviation which applies to {i[0]}: ")
                  i[1]:
        print("##### CORRECT! ######\n")
    if answer ==
    else:
        print("XXXXX INCORRECT! XXXXX\n")
