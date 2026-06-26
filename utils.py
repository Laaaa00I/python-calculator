def get_number(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a number")
# ^^^ This function prevents program from using noninteger variable

YES_ANSWERS = ["1", "y", "yes", "yeah", "н", "нуы", "нуфр",
               "да", "конечно"]
NO_ANSWERS = ["2", "n", "no", "nah", "т", "тщ", "тфр",
              "нет", "не", "неа"]