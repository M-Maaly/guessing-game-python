import random

attempts_list = []

def show_score():
    """Display the current high score."""
    print(f"The current high score is {min(attempts_list, default='No high score')} attempts")

def play_game():
    """Play the guessing game."""
    pc_choice = random.randint(1, 10)
    attempt = 0

    while True:
        try:
            guess = int(input("Pick a number between 1 and 10: "))

            if not (1 <= guess <= 10):
                raise ValueError("Please guess a number within the given range")

            attempt += 1

            if guess == pc_choice:
                print(f"Nice! You guessed it in {attempt} attempt(s)")
                attempts_list.append(attempt)

                if input("Would you like to play again? (Enter yes/no): ").lower() == "no":
                    print("Thanks for playing. Have a good day.")
                    break

                show_score()
                pc_choice = random.randint(1, 10)
                attempt = 0
            else:
                print("It's lower!" if guess < pc_choice else "It's higher!")

        except ValueError as err:
            print(err)

def main():
    """Main function to initialize the game."""
    print("Hello player! Welcome to the Guessing game!")
    player_name = input("What's your name? ")

    if input("Would you like to play the guessing game? (Enter yes/no): ").lower() == "yes":
        show_score()
        play_game()
        print("Thanks for playing. Have a good day.")
    else:
        print("Thanks for visiting. Have a good day.")

if __name__ == "__main__":
    main()
