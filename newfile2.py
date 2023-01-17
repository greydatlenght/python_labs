import math
z = float(input('Введите с клавиатуры значение переменной z: '))
if z >= 1: # Если z >= 1, то выполнится код снизу
   x = z + math.log1p(z)
else: # Если z > 0, то вып. код снизу
   x = z*z*z + 0.2
y = math.pow(math.cos(x*x*x), 3) + math.pow(math.sin(x*x), 2)
print('y =', '{:.2f}'.format(y), 'при z =', z)