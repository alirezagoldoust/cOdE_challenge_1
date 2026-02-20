# This file is for getting inputs from users and update the board.
# 🎉 Have fun coding
bord = [[], [], [], [], [], [], []]


def bord_update(bord: list[list], user_choice: int, turn: int) -> list[list]:
    if check_is_full(user_choice) == True:
        print("This column is full, please choose another one.")
        return True
    elif turn == 1:
        bord[user_choice-1].append('X')
    elif turn == 2:
        bord[user_choice-1].append('O')

    return bord


def check_is_full(n: int) -> bool:
    if len(bord[n-1]) == 6:
        return True
    else:
        return False
