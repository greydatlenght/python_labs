from math import sqrt, cos, fabs #импортируем ф-ии из библиотеки
C = float(input('Введите значение С: ')) # вводим значение первой переменной с клавиатуры
P = float(input('Введите значение P: ')) # вводим значение второй переменной с клавиатуры
D = float(input('Введите значение D: ')) # вводим значение третьей переменной с клавиатуры
a = (sqrt(C) + sqrt(P) + sqrt(D)) # складываем значения корней квадратных
b = (C * P * D) # получаем произведение переменных
print('Сумма корней этих чисел: ', '{:.2f}'.format(a), ', ', 'произведение этих чисел: ', '{:.2f}'.format(b), '.') 