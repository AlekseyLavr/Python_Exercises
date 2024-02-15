distance_ft = float(input('Введите расстояние в футах: '))
MILE_FOOT = 5280
YARD_FOOT = 3
FOOT_INCH = 0.083333
print(f'{distance_ft // MILE_FOOT} миль')
distance_ft = distance_ft % MILE_FOOT
print(f'{distance_ft // YARD_FOOT} ярдов')
distance_ft = distance_ft % YARD_FOOT

print(f'{distance_ft // FOOT_INCH} дюймов')