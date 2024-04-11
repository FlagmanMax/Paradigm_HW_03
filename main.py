"""
Игра крестики-нолики в императивной парадигме:
используются процедурный и структурный методы
"""

# Инициализация доски
board = [1, 2, 3,
         4, 5, 6,
         7, 8, 9]

# Инициализация победных линий
win =  [[0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
        [0, 3, 6],
        [1, 4, 7],
        [2, 5, 8],
        [0, 4, 8],
        [2, 4, 6]]


# Вывод доски на экран
def print_board():
    for i in range(len(win)+1):
        print(f"{board[i]} ", end=" ")
        if (i+1) % 3 == 0:
            print()

# Сделать ход в ячейку
def step_board(step, symbol):
    ind = board.index(step)
    board[ind] = symbol


# Получить текущий результат игры
def get_result():
    win_string = ""

    for i in win:
        if board[i[0]] == "X" and board[i[1]] == "X" and board[i[2]] == "X":
            win_string = "X"
        if board[i[0]] == "O" and board[i[1]] == "O" and board[i[2]] == "O":
            win_string = "O"

    return win_string


# Основная программа
game_over = False
player1 = True

while game_over == False:

    # 1. Показываем карту
    print_board()

    # 2. Спросим у играющего куда делать ход
    if player1 == True:
        symbol = "X"
        step = int(input("Игрок 1, ваш ход: "))
    else:
        symbol = "O"
        step = int(input("Игрок 2, ваш ход: "))

    step_board(step, symbol)  # делаем ход в указанную ячейку
    win_string = get_result()  # определим победителя
    if win_string != "":
        game_over = True
    else:
        game_over = False

    player1 = not (player1)

# Игра окончена. Покажем карту. Объявим победителя.
print_board()
print("Победил", win_string)