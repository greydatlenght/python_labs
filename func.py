from math import *
def per(a, b):
    return (sqrt(a**2  + b**2) + a + b)
def area(a, b):
    return (a*b/2)
x = int(input('Введите значние первого катета первого треугольника: ')) 
y = int(input('Введите значние второго катета первого треугольника: ')) 
x2 = int(input('Введите значние первого катета второго треугольника: ')) 
y2 = int(input('Введите значние второго катета второго треугольника: ')) 
area = '{:.2f}'.format(area(x2, y2) + area(x, y))
per = '{:.2f}'.format(per(x2, y2) + per(x, y))
print(f'Сумма площадей треугольников: {area}; Сумма периметров треугольников: {per}.')