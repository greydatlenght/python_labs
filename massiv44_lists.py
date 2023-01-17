number = "0"
list = []

while number != '':
    number = input("Введите целое число: ")
    if number == '':
        continue
    list.append(int(number))

list.sort()

print(f"Список всех значений: {list}.")

for i in list:
    print(i)

