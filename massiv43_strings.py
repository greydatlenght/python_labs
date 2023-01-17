search_string = input("Введите строку для поиска: ")

symbol_for_search = input("Введите искомый символ: ")

x = 0
for i in search_string:
    if i == symbol_for_search:
        x += 1
    
print(f"Найденное количество символов: {x}")