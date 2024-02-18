temper = float(input('Введите температуру воздуха, С: '))
speed_vind = float(input('Введите скорость ветра, км/ч: '))
wind_chill_coefficient = 13.12 + 0.6215 * temper - 11.37 * speed_vind ** 0.16 + 0.3965 * temper\
    * speed_vind ** 0.16
print('Коэффициент охлаждения ветром равен', round(wind_chill_coefficient))