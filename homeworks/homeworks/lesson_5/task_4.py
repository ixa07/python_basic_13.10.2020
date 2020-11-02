"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
with open('task_4_part_1.txt', 'rt', encoding='UTF-8') as file_one:
    with open('task_4_part_2.txt', 'wt', encoding='UTF-8') as file_two:
        composition = file_one.readlines()
        for str in composition:
            str = str.replace("One", "Один", 1)
            str = str.replace("Two", "Два", 1)
            str = str.replace("Three", "Три", 1)
            str = str.replace("Four", "Четыре", 1)
            file_two.write(str)
