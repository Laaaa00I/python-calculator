from Operations import *


standard_operations_list = {
    **dict.fromkeys(["1", "sum", "сумма", "сложение", "плюс", "+"], Sum),
    **dict.fromkeys(["2", "mult", "multiply", "умножить", "произведение", "*"], Mult),
    **dict.fromkeys(["3", "div", "division", "разделить", "деление", "/"], Div),
    **dict.fromkeys(["4", "sub", "subtract", "отнять", "вычесть", "-"], Sub),
    **dict.fromkeys(["5", "pow", "exponent", "степень", "возвести", "^"], Pow),
    **dict.fromkeys(["6", "root", "корень", "извлечь", "радикал", "√"], Root)
}
# ^^^ Standard operations list (NOT UPDATING AUTOMATICALLY)
trigonometric_operations_list = {
    **dict.fromkeys(["1", "sin", "синус"], Sin),
    **dict.fromkeys(["2", "cos", "косинус"], Cos),
    **dict.fromkeys(["3", "tan", "tg", "тангенс"], Tan)
}
#^^^ Trigonometric operations list (NOT UPDATING AUTOMATICALLY)

standard_operations = '''
1. Summarise
2. Multiply
3. Divide
4. Subtract
5. Raise to a degree
6. Root (y-th root of x)
'''
#^^^ Standard operations menu (NOT UPDATING AUTOMATICALLY)
trigonometric_operations = '''
1. Sin
2. Cos
3. Tan
'''
#^^^ Trigonometric operations menu (NOT UPDATING AUTOMATICALLY)

standard_mode = [
    "1", "standard", "стандартный", "обычный"
]
trigonometric_mode = [
    "2", "trigonometric", "тригонометрический", "тригонометрия"
]

YES_ANSWERS = ["1", "y", "yes", "yep", "yeah", "н", "нуы", "нуфр",
               "да", "конечно"]
NO_ANSWERS = ["2", "n", "no", "nah", "т", "тщ", "тфр",
              "нет", "не", "неа"]