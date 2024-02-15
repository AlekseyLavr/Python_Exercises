import math
t_1 = float(input('Введите широту 1-й точки: '))
g_1 = float(input('Введите долготу 1-й точки: '))
t_2 = float(input('Введите широту 2-й точки: '))
g_2 = float(input('Введите долготу 2-й точки: '))
AVERAGE_RAD = 6371.01
t_1_rad = math.radians(t_1)
g_1_rad = math.radians(g_1)
t_2_rad = math.radians(t_2)
g_2_rad = math.radians(g_2)
print(f'Кратчайшее расстояние между точками:\
      {AVERAGE_RAD * math.acos(math.sin(t_1_rad) * math.sin(t_2_rad) + math.cos(t_1_rad) * math.cos(t_2_rad) * math.cos(g_1_rad - g_2_rad))} км.')