"""
Реализовать базовый класс Worker (работник), в котором определить атрибуты:
name, surname, position (должность), income (доход).
Последний атрибут должен быть защищенным и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus}. Создать класс Position (должность) на базе класса Worker.
В классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с учетом премии
(get_total_income). Проверить работу примера на реальных данных (создать экземпляры класса Position,
передать данные, проверить значения атрибутов, вызвать методы экземпляров).
"""
class Worker:
    name = ''
    surname = ''
    position = ''
    income = {"wage": 0, "prepayment": 0}

class Position(Worker):
    def get_name_surname(self):
        return self.name + ' ' + self.surname

    def get_total_income(self):
        return self.income["wage"] + self.income["prepayment"]

PositionInstance = Position()

PositionInstance.name = 'Bill'
PositionInstance.surname = 'Tramp'
PositionInstance.position = 'Manager'
PositionInstance.income["wage"] = 350
PositionInstance.income["prepayment"] = 50

print(PositionInstance.get_name_surname())
print(PositionInstance.get_total_income())