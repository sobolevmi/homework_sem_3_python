# Программа по вычислению разницы между минимальным и максимальным значением дробной части элементов

def ListFromFractionParts(user_string):
    """ Функция по созданию нового списка из дробных частей элементов ранее созданной строки"""
    user_string = list(user_string.split(sep=","))
    new_list = list()
    for i in range(len(user_string)):
        new_list.append(round(float(user_string[i]) % 1, 2))
    return new_list

def FindDifferenceFromMinMax(random_list):
    """ Функция по поиску минимального и максимального элемента в списке и вычислению разницы между ними"""
    res = round(max(random_list) - min(random_list), 2)
    return res

our_string = str(input("Введите вещественные числа (числа отделяйте запятыми, дробные части - точками:\n"))
user_list = ListFromFractionParts(our_string)
result = FindDifferenceFromMinMax(user_list)
print(f"[{our_string}] -> {result}")