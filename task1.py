# Программа по парному умножению элементов списка

def FillListFromUser():
    """ Функция по заполнению созданного списка вручную пользователем"""
    size = int(input("Введите размер создаваемого списка: "))
    any_list = list()
    for i in range(size):
        any_list.append(int(input("Введите элемент списка: ")))
    return any_list

def FillListFromRandom():
    """ Функция по заполнению созданного списка случайно сгенерированными числами"""
    import random
    length = int(input("Введите размер списка: "))
    start = int(input("Введите начало диапазона случайно генерируемых чисел: "))
    end = int(input("Введите конец диапазона случайно генерируемых чисел: "))
    random_list = [random.randint(start, end + 1) for i in range(length)]
    return random_list

def MultOfNumbers(created_list):
    """ Функция по подсчету произведения пар чисел в списке"""
    if len(created_list) % 2 != 0:
        new_list = list()
        for index in range(len(created_list) // 2 + 1):
            new_list.append(created_list[index] * created_list[-1 - index])
    else:
        new_list = list()
        for index in range(len(created_list) // 2):
            new_list.append(created_list[index] * created_list[-1 - index])
    return new_list

choice = int(input("Если вы хотите заполнить список самостоятельно, нажмите 1\nЕсли вы хотите, чтобы список был заполнен"
"случайно сгенерированными числами, нажмите 2:\n"))

user_list = list()

if choice == 1:
    user_list = FillListFromUser()
    print(f"{user_list} -> {MultOfNumbers(user_list)}")
elif choice == 2:
    user_list = FillListFromRandom()
    print(f"{user_list} -> {MultOfNumbers(user_list)}")
else:
    print("Вы ввели неверное число, попробуйте снова")







