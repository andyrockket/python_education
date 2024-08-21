car_names = ['bmw', 'mercedes', 'audi', 'toyota', 'subaru', 'volkswagen']

for car_name in car_names:
    if car_name == 'bmw':
        print('Нам попалась машина' + car_name)
    elif car_name == 'mercedes':
        print('Это невероятно круто, но у нас мерс, авто марки ' + car_name)
    else:
        print('Авто другой марки' + car_name)