# 5. Написать программу, содержащую функцию вычисления суммы чисел, не
# превосходящих заданного числа M.

# def sum(m):
#     a = 0
#     for i in range(0, (m + 1)):
#         a += i
#     return a

# x = int(input('input number: '))

# print(sum(x))

#3. Найти все трехзначные простые числа. (Определить функцию, позволяющую
#распознавать простые числа.)

def check(x):
        x = [int(a) for a in str(x)]
        a = 3
        for i in x:
            if i // 2 == 0 and i // 3 == 0 and i // 5 == 0 and i // 7 == 0:
                a -= 1          
        if a == 3:
            return '1'
        else:
            return '2'
    
for i in (100, 1000):
    if check(i) == '1':
        print(i)