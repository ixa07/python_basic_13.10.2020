"""
Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел.
 У пользователя необходимо запрашивать новый элемент рейтинга.
 Если в рейтинге существуют элементы с одинаковыми значениями,
 то новый элемент с тем же значением должен разместиться после них.
Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
Набор натуральных чисел можно задать непосредственно в коде, например, my_list = [7, 5, 3, 3, 2]
"""
my_list = [7, 5, 3, 3, 2]
new_element = int(input("Введите новый элемент рейтинга!\n"))
quantity_item = my_list.count(new_element)
for element in my_list:
    if quantity_item > 0:
        old_position = my_list.index(new_element)
        my_list.insert(old_position+quantity_item, new_element)
        break
    else:
        if new_element > element:
            new_position = my_list.index(element)
            my_list.insert(new_position, new_element)
            break
        elif new_element < my_list[len(my_list) - 1]:
            my_list.append(new_element)
print(my_list)



