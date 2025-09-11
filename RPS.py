import random
import math
user_move = input("enter either r, s or p to select your move ->").lower()


if user_move == "r" or "s" or "p":
    print("valid choice")
else:
    print("invalid letter please retry")
comp_moves = ["r", "p", "s"] 

move = random.choice(comp_moves) 
if user_move == "p" and move == "r" or user_move == "s" and move == "p" or user_move == "r" and move == "s":
    who_won = "player"
elif move == "p" and user_move == "r" or move == "s" and user_move == "p" or move == "r" and user_move == "s":
    who_won = "computer"
elif user_move == move:
    who_won = "tie"


if move == "r" and user_move == "p":
    print(f"computer used {move} while user used {user_move}, user won") 
elif move == "p" and user_move == "s":
    print(f"computer used {move} while user used {user_move}, user won") 
elif move == "s" and user_move == "r":
    print(f"computer used {move} while user used {user_move}, user won")
elif move == "p" and user_move == "r":
    print(f"computer used {move} while user used {user_move}, user lost") 
elif move == "s" and user_move == "p":
    print(f"computer used {move} while user used {user_move}, user lost") 
elif move == "r" and user_move == "s":
    print(f"computer used {move} while user used {user_move}, user lost") 
elif move == user_move:
    print("computer used the same one as user a tie has been issued")

if who_won == "player":
    print("1 win, 0 losses, 0 ties")
elif who_won == "computer":
    print("0 wins, 1 loss, 0 ties")
elif who_won == "tie":
    print("wins 0, losses 0, ties 1")