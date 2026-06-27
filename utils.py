from config import YES_ANSWERS, NO_ANSWERS


def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number")
# ^^^ Prevents program from using noninteger variable

def continue_cycle():
    while True:
        again = input("Would you like to continue?"
                      "\n1. Yes"
                      "\n2. No"
                      "\n").lower()
        if again in YES_ANSWERS:
            break
        elif again in NO_ANSWERS:
            print("Goodbye!")
            exit()
        else:
            print("Invalid input!")
#^^^ Stands for continuing calculations

