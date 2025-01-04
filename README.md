# Number Guessing Game

This is my solution to the [Number Guessing Game](https://roadmap.sh/projects/number-guessing-game) project from [roadmap.sh](https://roadmap.sh/), where you can play a number guessing game on the command-line interface.

## Features

- The game will display a welcome message along with the rules.
- The random number will be between 1 and 100.
- Users can select the difficulty level (Easy, Medium, Hard).
- If user's answer is correct, the game will give a congratulation message, and if it's incorrect, the game will give a hint.
- Users can play multiple rounds if they want.
- Users can see how much time it takes them to guess the number each round.
- Users can see their current high score after each round.

## Installation & Play

### Install via pip

Run the following command to install:

```bash
pip install git+https://github.com/ndongdoan/Number-Guessing.git
```

### Play the game

To play the game, from your terminal, use:

```bash
game
```

### Uninstall

To uninstall the package, run the following command:

```bash
pip uninstall number-guessing
```

## Project & Main Script Structure

### Project Structure

- **number_guessing_game**: Python package folder.
  - **\_\_init__.py**: Initialize this folder as a package and include optional basic metadata (can be left empty).
  - **game.py**: Game script.
- **setup.py**: Allow users to install the game as a package.
- **README.md**: Detailed project's description.

### Main Script Structure

- ```main()```: Create/Get data from a high score database, loop through the game until the user wants to stop, then store the high score in a temporary file. If no error occurs, it will then transfer the high score to the original high score database.
- ```welcome_msg()```: Display a welcome message.
- ```get_input()```: Get difficulty choice from the user and return with the corresponding difficulty and chances.
- ```get_highscore(db_path: str)```: Get high score data from the high score database. Return an empty dictionary if no high score is found.
- ```update_highscore(data: dict[str, int], difficulty: str, attempt: int)```: Update a new high score if the current round attempt is better.
- ```list_highscore(data: dict[str, int])```: Display the current high score as a table.
- ```play(data: dict[str, int], ans: int, difficulty: str, chances: int)```: Main game logic.
