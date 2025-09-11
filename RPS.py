import random
import math
user_move = input("enter either r, s or p to select your move ->").lower()


if user_move == "r" or user_move== "s" or user_move == "p":
    print("valid choice")
else:
    print("invalid letter please retry")
    exit()
comp_moves = ["r", "p", "s"] 

move = random.choice(comp_moves) 


if user_move == "p":
    moving1 = "paper"
if user_move == "r":
    moving1 = "rock"
if user_move == "s":
    moving1 = "sissors"
if move == "p":
    moving2= "paper"
if move == "r":
    moving2= "rock"
if move == "s":
    moving2= "sissors"


if move == "r" and user_move == "p":
    print(f"computer used {moving2} while user used {moving1}, user won") 
    who_won = "player"
elif move == "p" and user_move == "s":
    print(f"computer used {moving2} while user used {moving1}, user won") 
    who_won = "player"
elif move == "s" and user_move == "r":
    print(f"computer used {moving2} while user used {moving1}, user won")
    who_won = "player"
elif move == "p" and user_move == "r":
    print(f"computer used {moving2} while user used {moving1}, user lost") 
    who_won = "computer"
elif move == "s" and user_move == "p":
    print(f"computer used {moving2} while user used {moving1}, user lost")
    who_won = "computer" 
elif move == "r" and user_move == "s":
    print(f"computer used {moving2} while user used {moving1}, user lost")
    who_won = "computer" 
elif move == user_move:
    print("computer used the same one as user a tie has been issued")
    who_won = "tie"

if who_won == "player":
    print("1 win, 0 losses, 0 ties")
elif who_won == "computer":
    print("0 wins, 1 loss, 0 ties")
elif who_won == "tie":
    print("wins 0, losses 0, ties 1")

