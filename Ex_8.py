mass_suv = 75
mass_trifle = 112
n = int(input('Введите количество сувениров: '))
m = int(input('Введите количество безделушек: '))
weight_suv = n * mass_suv
weight_trifle = m * mass_trifle
print(f'Общий вес посылки: {weight_suv + weight_trifle} г.')
