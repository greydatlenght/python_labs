from math import *
A = int(input('Введите число: '))
print(f'Делители числа {A}: ')
for i in range(1, A + 1):
    if A % i == 0:
        print(i)