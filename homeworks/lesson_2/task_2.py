"""
Для списка реализовать обмен значений соседних элементов, т.е.
Значениями обмениваются элементы с индексами 0 и 1, 2 и 3 и т.д.
При нечетном количестве элементов последний сохранить на своем месте.
Для заполнения списка элементов необходимо использовать функцию input()
"""
user_str = input("Введите строку элементов!\n")
new_list = list(user_str)        #делаем из пользовательской строки список
if len(new_list) % 2 == 0:       #задаем условие четного/нечетного количества элементов
    i = 0                        #начинаем с нулевого элемента
    while i < len(new_list):     #задаем цикл, с выходом при превышении числа элементов
        el = new_list[i]
        new_list[i] = new_list[i+1]
        new_list[i+1] = el
        i += 2
else:
    i = 0
    while i < len(new_list) - 1:  #иначе, в случае нечетного числа элементов
        el = new_list[i]
        new_list[i] = new_list[i + 1]
        new_list[i + 1] = el
        i += 2
print(new_list)