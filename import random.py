import random
import math


def get_valid_input():


    """
    this function will have the loop that prompts the user for an r,p, or s 
    and then it will return that string trimmed and lowercased once it has it

    """
    while True:
        user_move = input("enter either r, s or p to select your move ->").lower()
        if user_move == "r" or user_move== "s" or user_move == "p":
            print("valid choice")
            break
        else:
            print("invalid letter please retry")
                
 

    
def convert_letter_to_word(user_move, move, moving1, moving2):
    """ 
    
    this function will accept a string (r/p/s) and return “rock”, “paper” or “scissors” respectively.
    

    """
    user_move = ""
    move = ""
    Round = 1
    print(f"ROUND({Round})")
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

def print_round_result(user_move, move, who_won):
    moving1 = ""
    moving2 = ""
    move = ""
    who_won = ""
    """
    
    this function will just print the result of the round.   

    """
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

def print_series_result(won_points, lost_points, tied_points):
    who_won = "player"
    """
    this function will determine the winner and print the appropriate message.
    
    """
    
    if who_won == "player" :
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
    print(f"user won {won_points} points and the computer won {lost_points} points meaning {winner}")

def main():
    moving1 = ""
    moving2 = ""
    tied_points = 0
    rounds= 5
    won_points = 0
    lost_points = 0
    who_won = print_series_result
    winner = ""
    user_move = get_valid_input()
    move = ""
    who_won
    comp_moves = ["r", "p", "s"]
    for rounds in range(rounds):
        get_valid_input() 
        move = random.choice(comp_moves)
        convert_letter_to_word(user_move, move, moving1, moving2)
        print_round_result(user_move, move, who_won)
        print_series_result(won_points, lost_points, tied_points)

if __name__ == "__main__":
    main()