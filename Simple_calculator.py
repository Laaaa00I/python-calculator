from utils import *
from config import *


while True:
    is_trigonometric = False
    print("Select calculation mode:"
          "\n1. Standard"
          "\n2. Trigonometric")

    while True:
        mode = input().lower()
        if mode in standard_mode:
            x = get_number("Enter first number: ")
            y = get_number("Enter second number: ")
            break
        if mode in trigonometric_mode:
            is_trigonometric = True
            x = get_number("Enter number: ")
            y = 0
            break
        print("Invalid input!")
    #^^^ Mode selection
    # Ru: Выбор режима

    if mode in standard_mode:
        print(standard_operations)
    if mode in trigonometric_mode:
        print(trigonometric_operations)
    #^^^ Shows available operations
    # Ru: Показывает доступные операции

    while True:

        while True:
            calc = input("Enter calculation method: ").lower()
            if calc in standard_operations_list or calc in trigonometric_operations_list:
                break
            print("Invalid operation!")
        #^^^ Operation selection cycle
        # Ru: Выбор операции

        try:
            if is_trigonometric:
                result = trigonometric_operations_list[calc](x, y)
            else:
                result = standard_operations_list[calc](x, y)
            if not is_trigonometric:
                print("=" * 30)
                print(result)
                print("=" * 30)
            if is_trigonometric:
                print("=" * 30)
                print(result)
                print("Note: answer is in radians!")
                print("=" * 30)
            break
        except ZeroDivisionError as e:
            print(f"Error: {e}")
        except ValueError as e:
            print(f"Error: {e}")
        #^^^ Try & Except — tries to output answer, otherwise shows error (Zero Division Error)
        #Ru: Try & Except — пытается вывести ответ, в противном случае отображается ошибка (ошибка деления на ноль)

    #^^^ This cycle contains operation selection and answer/error output
    # Ru: Этот цикл содержит выбор операции и вывод ответа/ошибки

    continue_cycle()

# ^^^ Main calculation cycle
#Ru: Основной цикл расчетов
