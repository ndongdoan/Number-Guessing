from random import randint

def init() -> None:
    print("""Welcome to the Number Guessing Game!
I'm thinking of a number between 1 and 100.
You have some chances to guess the correct number.\n
Please select the difficulty level:
1. Easy (10 chances)
2. Medium (5 chances)
3. Hard (3 chances)\n""")
    
    info = difficulty()
    inp = input("Enter your choice: ")
    diff, chance = info[inp][0], info[inp][1]

    print("Great! You have selected the", diff, "difficulty level.\n" +
          "Let's start the game!\n")
    
    compare(randint(1,100), chance)

#Return number of chances
def difficulty() -> dict[str, list]:
    return {
        "1": ["Easy", 10],
        "2": ["Medium", 5],
        "3": ["Hard", 3],
    }

def compare(ans: int, chances: int) -> None:
    attempt = 1
    while attempt <= chances:
        user = int(input("Enter your guess: "))
        if ans < user:
            print("Incorrect! The number is less than", user, "\n")
        elif ans > user:
            print("Incorrect! The number is greater than", user, "\n")
        else:
            print("Congratulations! You guessed the correct number in", attempt,"attempts.")
            return
        attempt += 1
    print("You run out of chances!!! The correct number is", ans)
    return

init()