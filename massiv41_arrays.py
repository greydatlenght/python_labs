array = [10, -4, 12, -56, 4, -89, 2]
i = 0
a = 0
x = array[0]
for i in array:
    if i < 0:
        if x > 0:
            x = i
            a += 1
        else:
            x = i
            a = a
    else:
        if x < 0:
            x = i
            a += 1
        else:
            x = i
            a = a
print(f'Исходный массив: {array}')
print(f"Количество раз изменений знака: {a}")
