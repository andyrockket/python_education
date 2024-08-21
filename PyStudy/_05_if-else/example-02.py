# ================================================== Пример с условиями
#
# name = 'Andy'
#
# if name == 'Andy':
#     print('Hello, Andy')
# else:
#     print('У нач чужакк')

'''

Проверка условий и принятие решений по результатам этой проверки называется ветвлением
(branching). Программа таким способом выбирает, по какой из возможных ветвей ей двигаться
дальше.
Двоеточие (:) в конце строки с инструкцией if сообщает интерпретатору Python, что дальше
находится блок команд. В блок команд входят все строки с отступом под строкой с инструкцией
if, вплоть до следующей строки без отступа.

В Python отступы это неотъемлемая часть кода. Именно отступ сообщает интерпретатору
Python, где начинается и где заканчивается блок кода.

Не стоит путать оператор присваивания (=) с условным оператором (==).

if x > 7	если x БОЛЬШЕ 7
if x < 7	если x МЕНЬШЕ 7
if x >= 7	если x БОЛЬШЕ или РАВЕН 7
if x <= 7	если x МЕНЬШЕ или РАВЕН 7
if x == 7	если x РАВЕН 7
if x != 7	если x НЕ РАВЕН 7

'''

# Example 1
# age = int(input('Сколько вам лет? -> '))
# if 3 <= age <= 6:
#     print('Вы ребёнок')
# else:
#     print('Вы явно не ребенок')

# Example 2
# if a == b == c:
#     print('числа равны')
# else:
#     print('числа не равны')

# Example 3
# word = input('Ваш любимый язык программирования?')
#
# if word == 'Python':
#     print('Верно! И это круто')
# else:
#     print('Python все равно круче')

# Example 4
# num = int(input('Введите 2х значеное число'))
#
# one_number = num % 10
# two_number = num // 10
#
# if one_number == two_number:
#     print('Числа совпадают')
# else:
#     print('нет')

# num = int(input())
#
# if num % 2 == 0:
#     print('Четное')
# else:
#     print('Нечетное')


# num1 = int(input())
# num2 = int(input())
# num3 = int(input())
#
# if num2 - num1 == num3 - num2:
#     print("YES")
# else:
#     print("NO")

'''
Напишите программу, которая определяет наименьшее из двух чисел.
На вход программе подаётся два различных целых числа.
Программа должна вывести наименьшее из двух чисел.
'''
# a, b = 26, 25  # int(input()), int(input())
#
# if a < b:
#     print(a)
# else:
#     print(b)


# name = 'Андрей'
# pwd = 'рыба-меч'
# if name == 'Андрей':
#     print('Привет, ' + name)
#     if pwd == 'рыба-меч':
#         print('Доступ предоставлен')
#     else:
#         print('Неверный пароль')

# name = 'Alice'
#
# if name == 'Alice':
#     print('Hi, Alice.')
# else:
#     print('У нас чужак!')

# variable = 42 == 40
# print(variable)

a = [1, 2, 3]
b = 1.2
c = 11
print(a, b, c)
