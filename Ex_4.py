S_F_A = 43560
print('Enter light, foot: ')
l = float(input())
print('Enter width, foot: ')
w = float(input())
square = l * w / S_F_A
print(f'Square =  {round(square, 3)} acre')