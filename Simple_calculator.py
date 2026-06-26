from Operations import Sum, Sub, Mult, Div, Pow, Root, Sin, Cos, Tan
from utils import *

operations_list = {
    **dict.fromkeys(["1", "sum", "сумма", "сложение", "плюс", "+"], Sum),
    **dict.fromkeys(["2", "mult", "multiply", "умножить", "произведение", "*"], Mult),
    **dict.fromkeys(["3", "div", "division", "разделить", "деление", "/"], Div),
    **dict.fromkeys(["4", "sub", "subtract", "отнять", "вычесть", "-"], Sub),
    **dict.fromkeys(["5", "pow", "exponent", "степень", "возвести", "^"], Pow),
    **dict.fromkeys(["6", "root", "корень", "извлечь", "радикал", "√"], Root),
    **dict.fromkeys(["7", "sin", "синус"], Sin),
    **dict.fromkeys(["8", "cos", "косинус"], Cos),
    **dict.fromkeys(["9", "tan", "tg", "тангенс"], Tan)
}
# ^^^ Available operations list (NOT UPDATING AUTOMATICALLY)

available_operations = '''
1. Summarise
2. Multiply
3. Divide
4. Subtract
5. Raise to a degree
6. Root (y-th root of x)
7. Sin (x)
8. Cos (x)
9. Tan (x)
'''

while True:

    x = get_number("Enter first number: ")
    y = get_number("Enter second number: ")
    #^^^ Input

    print(available_operations)
    #^^^ Shows available operations

    while True:

        while True:
            calc = input("Enter calculation method: ").lower()
            if calc in operations_list:
                break
            print("Invalid operation!")
        #^^^ This cycle stands for choosing an operation

        try:
            result = operations_list[calc](x, y)
            print("=" * 30)
            print(result)
            print("Note: if you choose trigonometric operation, answer is in radians!")
            print("=" * 30)
            break
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        #^^^ Try & Except — tries to output answer, otherwise shows error (ZeroDivisionError / Zero Division Error)

    #^^^ This cycle contains choosing an operation and answer/error output


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
    #^^^ This cycle stands for continuing calculations

# ^^^ Main calculation cycle