"""
Создать программно файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных свидетельствует пустая строка.
"""
with open("filename.txt", "wt", encoding='UTF-8') as file:
    while True:
        str_file = input('Введите ваши данные:')
        if not str_file:
            break
        file.write(f'{str_file}\n')