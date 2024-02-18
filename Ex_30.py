COEFF_C_K = 273.15
COEFF_C_F_1 = 9 / 5
COEFF_C_F_2 = 32
temperature_C = float(input('Введите температуру, С: '))
temperature_K = temperature_C + COEFF_C_K
temperature_F = temperature_C * COEFF_C_F_1 + COEFF_C_F_2
print(f'Температура по шкале Кельвина равна {temperature_K};\n\
Температура по шкале Фаренгейта равна {temperature_F}.')