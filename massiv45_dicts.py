dict = {
    "Russia": "Moscow",
    "USA": "Missuri",
    "UK": "Temza"
}

list = ['Moscow', 'Missuri', 'Temza']

#print(dict, list)

print(f'Соотношение стран и рек в этих странах: {dict.items()}')

x = input("Введите название реки, которую хотите проверить на наличие в словаре: ")

if x in dict.values():
    print(f'Река "{x}" есть в этом словаре.')
elif x not in dict.values():
    print(f'Реки "{x}" нет в этом словаре.')

y = input("Введите ключ новой пары словаря: ")
y2 = input("Введите значение этого включа в словарь: ")

dict[f"{y}"] = f"{y2}"

print(dict)
print(f"В словарь была добавлена пара ('{y}': '{y2}'). ")

z = input("Введите название реки, которую выхотите удалить: ")

for k, v, in dict.items():
    if v == z:
        z2 = k

        dict.pop(z2)

print(dict)
print(f'Вы удалили реку с названием: {z}.')