firs = int(input('Введите число'))
second = int(input('Введите число'))
third = int(input('Введите число'))
if firs == second == third:
    print(3)
elif firs == second or firs == third or second == third:
    print(2)
else:
    print(0)


