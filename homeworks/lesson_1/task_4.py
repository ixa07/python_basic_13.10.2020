"""
Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
Для решения используйте цикл while и арифметические операции.
"""
number_user = int(input("Введите любое целое положительное число\n"))
number_max = number_user % 10
surplus = number_user // 10
while surplus > 0:
    if surplus % 10 > number_max:
        number_max = surplus % 10
    surplus = surplus // 10
print('Самая большая цифра в введенном Вами числе - это',number_max)