import random

array = []
arrayin = []
while len(array) < 25:
    while len(arrayin) < 36:
        arrayin.append(random.randint(0, 1))
    array.append(arrayin)

i = 0
x = 0
while i < 36:
    if array[12][i] == 1:
        x += 1
    i += 1

print(f'Число купленых билетов: {x}')