UNI_GAS_CONCT = 8.314

pressure = float(input('Введите давление, Па: '))
capacity = float(input('Введите объём, л: '))
temperature = float(input('Введите температуру, С: '))
temp_C_K = 273.15 + temperature
print('Количество газа %.3f моль' % ((pressure * capacity) / (UNI_GAS_CONCT * temp_C_K)))