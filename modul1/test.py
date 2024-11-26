# Создание множества
numbers = {1, 2, 3, 4, 5}

# Добавление элементов
numbers.add(6)

# Удаление элемента
numbers.discard(2)

# Перебор множества
for number in numbers:
    print(number)

# Операции с множествами
another_set = {4, 5, 6, 7}
union_set = numbers.union(another_set)  # Объединение
intersection_set = numbers.intersection(another_set)  # Пересечение

print("Объединение:", union_set)
print("Пересечение:", intersection_set)