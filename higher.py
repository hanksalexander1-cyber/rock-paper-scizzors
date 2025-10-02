import random
def main_code():
    """picks a random number between 0 and 100 (inclusive) and has the user continuously guess until they guess what number it is"""
    computer_num = random.randint(1, 100)
    tries = 1
    while True:
        print(computer_num)
        try:
            user_num = int(input("Input a number between 1 and 100 -> "))
        except ValueError:
            print("not a number between 1 and 100")
            continue
        if user_num != str and user_num != float and 1 <= user_num <= 100:
            print("valid number")
        else:
            print("not a number between 1 and 100")
        if user_num == computer_num:
            print(f"You got it in {tries} tries")
            print(f"the number was {computer_num}")
            break
        tries += 1

def retry():
    """"""
    confirm = input("would you like to retry y/n -> ").lower().strip()
    if confirm == "y":
        while True:
            main_code()
            retry()
    if confirm == "n":
        StopIteration


def main():
    main_code()
    retry()


if __name__ == "__main__":
    main()