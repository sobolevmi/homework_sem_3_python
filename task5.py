# Программа по выводу списка чисел Фибоначчи, в том числе для отрицательных

def Fib(number):
    """ Функция по выводу списка из положительных чисел Фибоначчи"""
    fibo_list = list()
    fibo_list.append(1)
    fibo_list.append(1)
    for i in range(2, number):
        fibo_list.append(fibo_list[i - 1] + fibo_list[i - 2])
    return fibo_list

user_number = int(input("Введите число: "))

plus_fibo_list = Fib(user_number)

minus_fibo_list = plus_fibo_list.copy()
minus_fibo_list.reverse()
minus_fibo_list.append(0)

if user_number % 2 == 0:
    for i in range(0, len(minus_fibo_list), 2):
        minus_fibo_list[i] = -minus_fibo_list[i]
else:
    for i in range(1, len(minus_fibo_list), 2):
        minus_fibo_list[i] = -minus_fibo_list[i]

minus_fibo_list.extend(plus_fibo_list)
print(f"{user_number} -> {minus_fibo_list}")

