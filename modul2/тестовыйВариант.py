def print_board(b):
    print("\n".join(" | ".join(r) for r in b), "\n---------")

def check_winner(b):
    return next((l[0] for l in b + list(zip(*b)) + [[b[i][i] for i in range(3)]] + [[b[i][2-i] for i in range(3)]] if l[0] != " " and l[0] == l[1] == l[2]), None)

def tic_tac_toe():
    b, p = [[" "] * 3 for _ in range(3)], "X"  # Инициализация доски и текущего игрока
    while True:
        print_board(b)  # Печать текущей доски
        try:
            r, c = map(int, input(f"Игрок {p}, введите строку и столбец: ").split())  # Ввод координат
            if b[r][c] != " ": raise ValueError  # Проверка на занятость клетки
        except:
            print("Некорректный ввод. Попробуйте снова."); continue  # Обработка ошибок ввода
        b[r][c] = p  # Установка символа текущего игрока
        if (w := check_winner(b)):  # Проверка на победителя
            print_board(b); print(f"Игрок {w} выиграл!"); break
        if all(cell != " " for row in b):  # Проверка на ничью
            print_board(b); print("Ничья!"); break
        p = "O" if p == "X" else "X"  # Смена игрока

if __name__ == "__main__": tic_tac_toe()  # Запуск игры