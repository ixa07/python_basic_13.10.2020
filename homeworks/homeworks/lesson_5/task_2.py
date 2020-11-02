"""
Создать текстовый файл (не программно), сохранить в нем несколько строк,
 выполнить подсчет количества строк, количества слов в каждой строке.
"""
with open('task_2.txt', 'rt', encoding='UTF-8') as file:
    composition = file.readlines()
    print(f'Число строк: {len(composition)}')
    for ind, line in enumerate(composition, 1):
        print(f'В строке номер {ind} количество слов {len(line.split())}')