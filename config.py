from Operations import *


standard_operations_list = {
    **dict.fromkeys(["1", "sum", "сумма", "сложение", "плюс", "+"], Sum),
    **dict.fromkeys(["2", "sub", "subtract", "отнять", "вычесть", "-"], Sub),
    **dict.fromkeys(["3", "mult", "multiply", "умножить", "произведение", "*"], Mult),
    **dict.fromkeys(["4", "div", "division", "разделить", "деление", "/"], Div),
    **dict.fromkeys(["5", "pow", "exponent", "степень", "возвести", "^"], Pow),
    **dict.fromkeys(["6", "root", "корень", "извлечь", "радикал", "√"], Root)
}
# ^^^ Standard operations list (NOT UPDATING AUTOMATICALLY)
#Ru: Лист арефметических операций (НЕ ОБНОВЛЯЕТСЯ АВТОМАТИЧЕСКИ)
trigonometric_operations_list = {
    **dict.fromkeys(["1", "sin", "sine", "синус"], Sin),
    **dict.fromkeys(["2", "cos", "cosine", "косинус"], Cos),
    **dict.fromkeys(["3", "tan", "tangent", "tg", "тангенс"], Tan),
    **dict.fromkeys(["4", "cot", "cotangent", "ctg", "котангенс"], Cot)
}
#^^^ Trigonometric operations list (NOT UPDATING AUTOMATICALLY)
#Ru: Лист тригонометрических операций  (НЕ ОБНОВЛЯЕТСЯ АВТОМАТИЧЕСКИ)

standard_operations = '''
1. Summarise
2. Subtract
3. Multiply
4. Divide
5. Raise to a degree
6. Root (y-th root of x)
'''
#^^^ Standard operations menu (NOT UPDATING AUTOMATICALLY)
#Ru: Меню арефметических операций  (НЕ ОБНОВЛЯЕТСЯ АВТОМАТИЧЕСКИ)
trigonometric_operations = '''
1. Sin
2. Cos
3. Tan
4. Cot
'''
#^^^ Trigonometric operations menu (NOT UPDATING AUTOMATICALLY)
#Ru: Меню тригонометрических операций (НЕ ОБНОВЛЯЕТСЯ АВТОМАТИЧЕСКИ)

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
