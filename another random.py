import random
import math
def get_valid_input():
    while True:
        user_move = input("enter either r, s or p to select your move ->").lower()
        if user_move == "r" or user_move== "s" or user_move == "p":
            print("valid choice")
            break
        else:
            print("invalid letter please retry")

comp_moves = ["r", "p", "s"] 
move = random.choice(comp_moves) 

def convert_letter_to_word():
    Round += 1
    print(f"ROUND({Round})")
    user_move = get_valid_input(moving1, moving2)
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

def determine_outcome():
    user_move = get_valid_input()
    moving1 = convert_letter_to_word(moving1)
    moving2 = convert_letter_to_word(moving2)
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
    if  who_won == "player" :
        won_points += 1
    elif who_won == "computer":
        lost_points += 1
    elif who_won == "tie":
        tied_points += 1
    print(f"wins({won_points}) losses({lost_points}) ties({tied_points})")
    if won_points > lost_points:
        winner = ("user is the winner")
    elif won_points < lost_points:
        winner = ("computer is the winner")
    elif won_points == lost_points:
        winner = ("the user and the computer ended in a tie")
    print(f"user won {won_points} point and the computer won {lost_points} points meaning {winner}")

def print_series_result(won_points, lost_points, tied_points):
    pass
def main(): 
    tied_points = 0 
    rounds= 5 
    won_points = 0 
    lost_points = 0  
    Round = 0 
    winner = "" 
    user_move = "" 
    move = ""  
    for rounds in range(rounds): 
        get_valid_input() 
        convert_letter_to_word(user_move) 
        determine_outcome() 
    print_series_result(won_points, lost_points, tied_points)

if __name__ == "__main__": 

    main() 