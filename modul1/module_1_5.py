immutable_var = (1, 2, 'a', 'b')
print("Кортеж immutable_var:", immutable_var)
try:
    immutable_var[0] = 10
except TypeError as e:
    print("Ошибка:", e)
    print("Нельзя изменить элементы кортежа, так как кортежи являются неизменяемыми объектами в Python.")

immutable_var = [1, 2, 'a', 'b', 'Modified']
print(immutable_var)
immutable_var[0] = 10
immutable_var[4] = "world"
print("Изменённый список:", immutable_var)


