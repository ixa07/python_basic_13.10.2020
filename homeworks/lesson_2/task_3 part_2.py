"""
Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц (зима, весна, лето, осень).
Напишите решения через list и через dict.
"""
#РЕШЕНИЕ ЧЕРЕЗ СЛОВАРИ
number = int(input("Введите любой месяц года в виде его порядкового номера\n"))
winter = {1: 1, 2: 2, 3: 12}
spring = {1: 3, 2: 4, 3: 5}
summer = {1: 6, 2: 7, 3: 8}
autumn = {1: 9, 2: 10, 3: 11}
if number in winter.values():
    print("Это зимний месяц!")
else:
    if number in spring.values():
        print("Это весенний месяц!")
    else:
        if number in summer.values():
            print("Это летний месяц!")
        else:
            if number in autumn.values():
                print("Это осенний месяц!")