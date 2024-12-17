# NumberGuessingGameSolution
Solution to the Number Guessing Game: (https://roadmap.sh/projects/number-guessing-game) for the Python: (https://roadmap.sh/python) roadmap on Roadmap.sh: (https://roadmap.sh/)

Project URL: https://github.com/FerGRodz/NumberGuessingGameSolution


Number Guessing Game

Build a simple number guessing game to test your luck.

You are required to build a simple number guessing game where the computer randomly selects a number and the user has to guess it. The user will be given a limited number of chances to guess the number. If the user guesses the number correctly, the game will end, and the user will win. Otherwise, the game will continue until the user runs out of chances.
Requirements

It is a CLI-based game, so you need to use the command line to interact with the game. The game should work as follows:

    When the game starts, it should display a welcome message along with the rules of the game.
    The computer should randomly select a number between 1 and 100.
    User should select the difficulty level (easy, medium, hard) which will determine the number of chances they get to guess      the number.
    The user should be able to enter their guess.
    If the user’s guess is correct, the game should display a congratulatory message along with the number of attempts it took     to guess the number.
    If the user’s guess is incorrect, the game should display a message indicating whether the number is greater or less than      the user’s guess.
    The game should end when the user guesses the correct number or runs out of chances.

How to Play

    Run the game by executing the Python file.
    You will be presented with a welcome message and a prompt to select the difficulty level.
    Choose the difficulty level by entering 1 for Easy, 2 for Medium, or 3 for Hard.
    Once you've selected the difficulty level, you will be prompted to enter your guess.
    Enter a number between 1 and 100.
    If your guess is incorrect, you will receive a hint indicating whether the correct number is higher or lower than your         guess.
    Keep guessing until you correctly guess the number or run out of attempts.

Difficulty Levels

    Easy: 10 attempts to guess the correct number.
    Medium: 5 attempts to guess the correct number.
    Hard: 3 attempts to guess the correct number.

Technical Details

This game is built using   and the readline module for handling user input. The game logic is implemented in JavaScript, and the code is organized into separate functions for each difficulty level and for handling user input.
