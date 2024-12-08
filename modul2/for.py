numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

# Создаем пустые списки для простых и непростых чисел
primes = []
not_primes = []

# Перебор чисел из списка numbers
for number in numbers:
    if number < 2:
        not_primes.append(number)  # Число 1 не является простым
        continue

    is_prime = True  # Предполагаем, что число простое
    for i in range(2, int(number ** 0.5) + 1):  # Проверяем делители до корня из числа
        if number % i == 0:  # Если число делится на i
            is_prime = False  # Число не простое
            break  # Прерываем цикл, если нашли делитель

    if is_prime:
        primes.append(number)  # Добавляем в список простых
    else:
        not_primes.append(number)  # Добавляем в список непростых

# Выводим результаты на экран
print("Primes:", primes)
print("Not Primes:", not_primes)