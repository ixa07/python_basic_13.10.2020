"""
Создать (не программно) текстовый файл, в котором каждая строка должна содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1 ООО 10000 5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчет средней прибыли ее не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить ее в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджеры контекста.
"""
import json
with open('task_7.txt', 'rt', encoding='UTF-8') as file:
    composition = file.readlines()
    quantity = len(composition)
    sum_income = 0
    search = [{}, {}]
    for str in composition:
        str_firm = str.split()
        key = str_firm[0]
        income = int(str_firm[2]) - int(str_firm[3])
        if income > 0:
            sum_income += income
        search[0][key] = income
    search[1]["sr_income"] = sum_income / quantity
    with open("task_7.json", "wt") as new_file:
        json.dump(search, new_file)





