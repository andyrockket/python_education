# Написать пример с выбором фильмов

print('1. Комедии. 2. Боевики. 3. Драмы. 4. Триллеры. 5. Фантастика.')

choice = int(input(''))

if choice == 1:
    print('Вы выбрали комедии')
elif choice == 2:
    print('Вы выбрали боевики')
elif choice == 3:
    print('Вы выбрали драмы')
else:
    print('Вы выбрали неизвестный жанр')

