import random

def get_valid_input():
    """
    Prompt the user for a valid input: 'r', 'p', or 's'.
    Returns the input in lowercase and trimmed.
    """
    while True:
        choice = input("Enter either 'r', 'p', or 's' to select your move -> ").strip().lower()
        if choice in ['r', 'p', 's']:
            return choice
        else:
            print("Invalid letter. Please retry.")

def convert_letter_to_word(letter):
    """
    Convert a letter to the full word version.
    r = rock, p = paper, s = scissors.
    """
    if letter == 'r':
        return "rock"
    elif letter == 'p':
        return "paper"
    elif letter == 's':
        return "scissors"
    else:
        raise ValueError("Invalid value passed in. Must be 'r', 'p', or 's'.")

def determine_outcome(user, comp):
    """
    Determine if the user won, lost, or tied based on the rules.
    Returns 'won', 'lost', or 'tied'.
    """
    if user == comp:
        return "tied"
    elif (user == 'r' and comp == 's') or \
         (user == 'p' and comp == 'r') or \
         (user == 's' and comp == 'p'):
        return "won"
    else:
        return "lost"

def print_round_result(user, comp, result):
    """
    Print the result of the round.
    """
    user_word = convert_letter_to_word(user)
    comp_word = convert_letter_to_word(comp)
    print(f"Computer used {comp_word} while user used {user_word}. Result: {result.upper()}.")

def print_series_results(user_wins, comp_wins, ties):
    """
    Print the final result after all rounds are completed.
    """
    print(f"Final Score -> User Wins: {user_wins}, Computer Wins: {comp_wins}, Ties: {ties}")
    if user_wins > comp_wins:
        print("User is the winner of the series!")
    elif user_wins < comp_wins:
        print("Computer is the winner of the series!")
    else:
        print("The user and the computer ended in a tie!")

def main():
    """
    Main function to run the Rock, Paper, Scissors game.
    """
    rounds = 5
    user_wins = 0
    comp_wins = 0
    ties = 0

    for round_num in range(1, rounds + 1):
        print(f"\nROUND {round_num}")
        user_move = get_valid_input()
        comp_move = random.choice(['r', 'p', 's'])
        result = determine_outcome(user_move, comp_move)
        print_round_result(user_move, comp_move, result)

        if result == "won":
            user_wins += 1
        elif result == "lost":
            comp_wins += 1
        else:
            ties += 1

        print(f"Score -> User Wins: {user_wins}, Computer Wins: {comp_wins}, Ties: {ties}")

    print("\nFINAL RESULTS")
    print_series_results(user_wins, comp_wins, ties)

if __name__ == "__main__":
    main()