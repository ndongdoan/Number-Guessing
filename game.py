from random import randint

def main():
    welcome_msg()
    chances = get_input()

    play(randint(1,100), chances)

#Welcome message
def welcome_msg() -> None:
    msg = ("Welcome to the Number Guessing Game!\n"
           "I'm thinking of a number between 1 and 100.\n"
           "You have some chances to guess the correct number.\n\n"
        
           "Please select the difficulty level:\n"
           "1. Easy (10 chances)\n"
           "2. Medium (5 chances)\n"
           "3. Hard (3 chances)\n")
    print(msg)

#Get input from user
def get_input() -> int:
    info = {
        "1": ["Easy", 10],
        "2": ["Medium", 5],
        "3": ["Hard", 3],
    }

    while True:
        inp = input("Enter your choice: ")
        if inp not in info.keys():
            print("Invalid input. Try again!\n")
        else:
            break
        
    difficulty, chance = info[inp][0], info[inp][1]

    print(f"\nGreat! You have selected the {difficulty} difficulty level.")
    print(f"You have {chance} chances.")
    print("Let's start the game!\n")
    
    return chance

#Game logic
def play(ans: int, chances: int) -> None:
    attempt = 1

    while attempt <= chances:
        user = int(input("Enter your guess: "))
        if user < 1 or user > 100:
            print("Invalid guess. Try again!\n")
            continue

        if ans < user:
            print("Incorrect! The number is less than", user)
            print(f"You have {chances - attempt} chances left.", "\n")
        elif ans > user:
            print("Incorrect! The number is greater than", user)
            print(f"You have {chances - attempt} chances left.", "\n")
        else:
            print("Congratulations! You guessed the correct number in", attempt,"attempts.")
            return
        attempt += 1
    print("You run out of chances!!! The correct number is", ans)

if __name__ == "__main__":
    main()