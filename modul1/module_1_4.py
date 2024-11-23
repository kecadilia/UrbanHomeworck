my_string = input("Введите произвольный текст")
print(f"Количество символов в введённом тексте:{len(my_string)}")
print(f"Строка в верхнем регистре:{my_string.upper()}")
print(f"Строка в вверхнем регистре:{my_string.lower()}")
my_string_no_spaces = my_string.replace(" ", "")
print(f"Строка без пробелов: {my_string_no_spaces}")
if my_string:
    print(f"Первый символ:{my_string[0]}")
else:
    print("Строка пустая, нет первого символа.")
if my_string:
    print(f"Последний символ: {my_string[-1]} ")
else:
    print("строка прустая,нет последнего символа.")