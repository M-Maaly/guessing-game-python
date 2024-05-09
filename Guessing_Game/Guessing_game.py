import random

attempts_list = []

### It's check if found score in attempts_list ? if there score in attempts_list take minimum value 
def show_score(): 
    if not attempts_list:
        print("There's currently no high score, Start playing!")
    else:
        print(f"The currently high a score is {min(attempts_list)} attempts")

attempt = 0
pc_choice = random.randint(1, 10) ### pc choose randomly between 1-10

### Quest player his/her name and if want to play.
print("Hello player! Welcome to the Guessing game!")
player_name = input("what's your name? ")
wanna_game = input(
    f"Hi {player_name}, would you like to play the guessing game?"
    " (Enter yes/no) "
).lower()

### if player write no exit from game
if wanna_game == "no":
    print("Thanks")
    exit()
else:
    show_score()

while wanna_game == "yes":
    try:
        guess = int(input("Pick a number between (1 - 10)===>>> "))

        if (guess < 1 or guess > 10):
            raise ValueError("Please guess a number within the given range")
        else:
            attempt += 1

            if (guess == pc_choice):
                print("Nice!, you do it!")
                print(f"It took you {attempt} attempt")
                wanna_game = input("Would you play again (Enter yes/no): ").lower()
                attempts_list.append(attempt)

                if (wanna_game == "no"):
                    print("Have a good day.")
                    break
                else:
                    pc_choice = random.randint(1, 10)
                    attempt = 0
                    show_score()
                    continue

            elif (guess < pc_choice):
                print("It's lower!")
            elif (guess > pc_choice):
                print("It's higher!")

    except ValueError as err:
        print(err)




