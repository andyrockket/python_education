'''
Приложение: *.py
Автор: rockket
Назначение: демонстрация применения комментариев
my_variable: str = 42  # Явное указание типа данных int для переменной
print(my_variable)

print("Этот код не выполняется никогда.")
'\nprint("Этот код не выполняется никогда.")\n'
'''

# Example 1. Пример комментария.
# print("Привет от Python!")  # Еще один пример комментария.

# Example 2. Конкатенация

# name = 'Andy'
# tutu: str = 10
# print('Привет, ' + name)
# print('Привет,', name + 'tutu')

# sep (separator – разделитель) и end (окончание).

print('1', '2', '3', sep='*', end='!')

word = 'world'
print(f"Hello {word}", sep='\n', end='\n')