result = 9**0.5*5 #worck 1
print(result)

worck = (9.99>9.98) and (1000 != 1000.1)#worck 2
print(worck) #ожидаем резкльтат True

# 3rd program
without_priority = 2 * 2 + 2
with_priority = 2 * (2 + 2)

print(without_priority)  # Вывод: 6
print(with_priority)      # Вывод: 8
print(without_priority == with_priority)  # Ожидаемый результат: False

number_str = '123.456'
number_float = float(number_str)  # Преобразование в дробное число
shifted_number = number_float * 10  # Умножаем на 10
first_after_decimal = int(shifted_number) % 10  # Получаем первую цифру после точки

print(first_after_decimal)  # Ожидаемый результат: 4