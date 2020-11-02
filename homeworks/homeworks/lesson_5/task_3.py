"""
Создать текстовый файл (не программно), построчно записать фамилии сотрудников и величину их окладов.
Определить, кто из сотрудников имеет оклад менее 20 тыс.,
вывести фамилии этих сотрудников. Выполнить подсчет средней величины дохода сотрудников.
"""
with open('task_3.txt', 'rt', encoding='UTF-8') as file:
    composition = file.readlines()
    number_of_workers = len(composition)
    sum_payment = 0
    for words in composition:
        workers, payment = words.split()
        payment = float(payment)
        sum_payment += payment
        if payment < 20000:
            print(f'{workers} - сотрудники с зарплатой менее 20000')
    print(f'Средняя зарплата составляет {sum_payment / number_of_workers}')