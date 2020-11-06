"""
Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
Атрибут реализовать как приватный.
В рамках метода реализовать переключение светофора в режимы: красный, желтый, зеленый.
Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего (зеленый) —
на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый,
зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.
"""
import time

class TrafficLight:
    color = 'red'
    color_dic = [('red', 'yellow', 'green'), (7, 2, 6)]

    def running(self):
        print(self.color)
        time.sleep(self.color_dic[1][self.color_dic[0].index(self.color)])
        self.color = self.color_dic[0][((self.color_dic[0].index(self.color)) + 1) % 3]

TrafficLightOperation = TrafficLight()
correct_behavior = ('red', 'yellow', 'green')
index = correct_behavior.index(TrafficLightOperation.color)

while True:
    TrafficLightOperation.running()
    if (correct_behavior.index(TrafficLightOperation.color) - index) % 3 == 1:
        index = correct_behavior.index(TrafficLightOperation.color)
    else:
        print("Цветовая очерёдность нарушена")
        break