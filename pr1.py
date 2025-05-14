# Список кортежів
data = [('apple', 3), ('banana', 1), ('cherry', 5), ('date', 2)]

# Сортування за другою складовою (індекс 1) у зворотному порядку
sorted_data = sorted(data, key=lambda x: x[1], reverse=True)

# Виведення результату
print(sorted_data)
