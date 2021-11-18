import math
a = int(input('Введите число'))
b = int(input('Введите число'))
c = int(input('Введите число'))

D = b ** 2 - 4 * a * c
if D > 0:
    x1 = (-b + math.sqrt(D)) / (2 * a)
    x2 = (-b - math.sqrt(D)) / (2 * a)

elif D == 0:
    x = -b / (2 * a)

else:
    print('Корней нет')