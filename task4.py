# Программа по переводу числа из десятичной системы счисления в двоичную

def TenToTwo(old_number, result = 1):
    """ Рекурсивная функция по переводу числа из десятичной системы счисления в двоичную"""
    if old_number > 0:
        return (old_number % 2) * result + TenToTwo(old_number // 2, result * 10)
    else:
        return 0

user_number = int(input('Введите десятичное число: '))
print(f"{user_number} -> {TenToTwo(user_number)}")