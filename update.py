# This file is for getting inputs from users and update the board.
# 🎉 Have fun coding
bord = [[],[],[],[],[],[],[]]
def bord_update (user_choice , turn , has_won):
    if turn == 1:
        bord[user_choice-1].append('X')
    else:
        bord[user_choice-1].append('O')

def check_is_full(n : int):
    if len(bord[n-1]) ==6:
        return False
    else:
        return True    


def game_status():
    pass