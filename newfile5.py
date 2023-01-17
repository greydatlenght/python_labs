from math import *
a = float(input('Введите значение a: '))# -0.9
b = float(input('Введите значение b: '))# 2.7
h = float(input('Введите значение h: '))# 0.3
n = 1
last_value = 0
up_or_down = ' '
max = 0
min = 0
print(f"Начало диапазона: {a} Конец диапазона: {b} Шаг: {h}")
print(f'№\tY\tX\tDif')
while a < 2.7:
    y = (1 - pow(a,2) /4) * cos(a) - a/2 * sin(a)
    y = '{:.2f}'.format(y)
    dif = float(y) - float(last_value)
    dif = '{:.2f}'.format(dif)
    a = float('{:.2f}'.format(a))
    if float(last_value) > float(y):
        up_or_down = 'down'
    else:
        up_or_down = 'up'  
    if n > 9:
        if float(y) < 0:
                print(f'{n}  {y}     {a}    {dif} {up_or_down} ')
        else:
            print(f'{n}  {y}      {a}    {dif} {up_or_down} ')     
    else:
        print(f'{n}   {y}      {a}    {dif} {up_or_down} ')

    if float(y) > float(max):
        max = y
    if float(y) < float(min):
        min = y
    last_value = y
    a = a + h
    n += 1
print(f'max: {max}, min: {min}')