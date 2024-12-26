from random import randint
from time import time
from tabulate import tabulate
import json
import tempfile
import shutil
import os

def main() -> None:
    highscore_path = os.path.expanduser("~/highscore.json")
    highscore_data = get_highscore(highscore_path)

    #game loop
    while True:
        welcome_msg()
        diff, chances = get_input()
        new_highscore = play(highscore_data, randint(1,100), diff, chances)
        #small test
        print(new_highscore)
        list_highscore(new_highscore)

        while True:
            play_again = input("Do you want to play again? (y/n): ").strip().lower()
            if play_again == "y":
                break
            elif play_again == "n":
                with tempfile.NamedTemporaryFile(mode = "w", delete = False, suffix=".json") as temp:
                    json.dump(new_highscore, temp, indent = 4)
                shutil.move(temp.name, highscore_path)
                return
            else:
                print("Invalid choice. Try again!\n")
                continue

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
def get_input() -> tuple[str, int]:
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
    
    return difficulty, chance

#Get highscore data
def get_highscore(db_path: str) -> dict[str, int]:
    try:
        with open(db_path) as f:
            highscore = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        highscore = {
            "Easy": None,
            "Medium": None,
            "Hard": None,
        }
    return highscore

#Update new high score and list current high score
def update_highscore(data: dict[str, int], difficulty: str, attempt: int) -> dict[str, int]:
    if not data[difficulty] or data[difficulty] > attempt:
        data[difficulty] = attempt
        print(f"New high score for {difficulty} mode: {attempt} attempts !!!")
    return data

#List current high score:
def list_highscore(data: dict[str, int]) -> None:
    table = []
    for mode, score in data.items():
        if not score:
            score = "No high score yet"
        table.append([mode, score])
    print(tabulate(table, headers=["Difficulty", "High score"], tablefmt="grid"))

#Game logic
def play(data: dict[str, int], ans: int, difficulty: str, chances: int) -> dict[str, int]:
    attempt = 1
    start = time()

    while attempt <= chances:
        try:
            user = int(input("Enter your guess: "))
            if user < 1 or user > 100:
                print("Invalid guess. Try again!\n")
                continue
        except ValueError:
            print("Invalid value entered. Try again!\n")
            continue

        if ans < user:
            print(f"Incorrect! The number is less than {user}.")
            print(f"You have {chances - attempt} chances left.\n")
        elif ans > user:
            print(f"Incorrect! The number is greater than {user}.")
            print(f"You have {chances - attempt} chances left.\n")
        else:
            time_played = time() - start
            print(f"Congratulations! You guessed the correct number in {attempt} attempts.")
            print(f"It takes you {time_played:.2f} seconds to guess the correct number.\n")
            
            return update_highscore(data, difficulty, attempt)
        attempt += 1
    print(f"You run out of chances!!! The correct number is {ans}.\n")
    return data

if __name__ == "__main__":
    main()