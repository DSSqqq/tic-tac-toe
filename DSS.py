def greet():
    print("-------------------")
    print("  Приветсвуем вас  ")
    print("      в игре       ")
    print("  крестики-нолики  ")
    print("-------------------")
    print(" формат ввода: x y ")
    print(" x - номер строки  ")
    print(" y - номер столбца ")
greet()

cells = [[" "] * 3 for i in range(3)]
# [["","",""],
# ["","",""],
# ["","",""]]

def show():
    print()
    for i in range(3):
        row_info = " ".join(cells[i])
        print(f"{i} {row_info} ") # {cells[i][0]} {cells[i][1]} {cells[i][2]}
        print("  --------------- ")

def show():
    print()
    print("    | 0 | 1 | 2 | ")
    print("  --------------- ")
    for i, row in enumerate(cells):
        row_str = f"  {i} | {' | '.join(row)} | "
        print(row_str)
        print("  --------------- ")
    print()

# выигрышные комбинации

def check_win():
    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(cells[i][j])
    if symbols == ["X","X","X"]:
        return True



    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(cells[j][i])
    if symbols == ["X","X","X"]:
        return True



    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(cells[i][i])
    if symbols == ["X","X","X"]:
        return True



    for i in range(3):
        symbols = []
        for j in range(3):
            symbols.append(cells[i][2-i])
    if symbols == ["X","X","X"]:
        return True

    return False
def check_win():
    win_cord = (((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2)),
                ((0, 2), (1, 1), (2, 0)), ((0, 0), (1, 1), (2, 2)), ((0, 0), (1, 0), (2, 0)),
                ((0, 1), (1, 1), (2, 1)), ((0, 2), (1, 2), (2, 2)))
    for cord in win_cord:
        symbols = []
        for c in cord:
            symbols.append(cells[c[0]][c[1]])
        if symbols == ["X", "X", "X"]:
            print("Выиграл X!!!")
            return True
        if symbols == ["0", "0", "0"]:
            print("Выиграл 0!!!")
            return True
    return False
def ask():
    while True:
        cords = input("         Ваш ход: ").split()

        if len(cords) != 2: # если не 2 координаты вывод сообщения и continue
            print(" Введите 2 координаты! ")
            continue

        x, y = cords

        if not (x.isdigit()) or not (y.isdigit()): # проверка на числа isdigit()
            print(" Введите числа! ")
            continue

        x, y = int(x), int(y)

        if 0 > x or x > 2 or 0 > y or y > 2: # проверка координат
            print(" Координаты вне диапазона! ")
            continue

        if cells[x][y] != " ": # проверка не занята ли клетка
            print(" Клетка занята! ")
            continue

        return x, y
num = 0
while True:
    num += 1
    show()
    if num % 2 == 1:
        print("Ходит крестик")
    else:
        print("Ходит нолик")
    x,y = ask()
    if num % 2 == 1:
        cells[x][y] = "X"
    else:
        cells[x][y] = "0"

    if check_win():
        print("Победа")
        break

    if num == 9:
        print("Ничья")
        break



