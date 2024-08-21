first_name, last_name = 'Andy', 'Rockket'
print(first_name, last_name) # Множественное присваивание

# == оператор равенства
# = оператор присваивания

# Аналог этой же конструкции
first_name = 'Andy'
last_name = 'Rockket'
print(first_name, last_name)

# То же самое можно написать иначе
# first_name, last_name = input(), input()
# print('Ваше имя:', first_name, 'Ваша фамилия:', last_name)

# Множественно присваивание
one = 'Andy'
two = 'Rockket'
one, two = two, one  # Два пробела отступ от кода
print(one, two)
