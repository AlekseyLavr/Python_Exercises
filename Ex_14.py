growth_ft = int(input('Введите рост в футах: '))
growth_inch = int(input('Введите рост в дюймах: '))
FOOT = 12 # Перевод футов в дюймы
INCH = 2.54 # Перевод дюймов в см
growth_ft_inch = growth_ft * 12
print(f'Рост человека в см: {(growth_ft_inch + growth_inch) * INCH}')