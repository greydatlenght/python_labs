import math
a = float(input("Введите число A: ")) 
y = float(input("Введите число B: "))
b = float(input("Введите число C:"))
x = math.fabs(math.cos(a))*(y+3)/(math.fabs(math.cos(a))*(y+3) - b)
print('Значение выражения с числами A B C =', '{:.2f}'.format(x))
