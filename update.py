# This file is for getting inputs from users and update the board.
# 🎉 Have fun coding
bord = [[],[],[],[],[],[],[]]
def bord_update (user_choice , turn , has_won):

    winner =''
    if has_won ==True:
        winner=turn
    else:
         if len(bord[user_choice-1]) ==5:
             pass
         else:
             bord[user_choice].append(turn)

def check_is_full(n : int):
    pass    


def game_status():
    pass