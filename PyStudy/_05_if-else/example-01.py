# Решаю задачки по условиям

print('Выберите цвет')
print('1 - Красный', '2 - синий', '3 - желтый')

color = int(input())

if color == 1:
    print('Вы выбрали красный')
elif color == 2:
    print('Вы выбрали синий')
elif color == 3:
    print('Вы выбрали желтый')
else:
    print('Вы выбрали неизвестный цвет')