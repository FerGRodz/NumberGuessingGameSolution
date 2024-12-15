import random

while True:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("You have up to 10 chances to guess the correct number, based on the difficulty you choose.")
    print("\n")
    print("Please select the difficulty level: ")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")
    print("\n")

    # Get difficulty level
    difficulty = input("Please enter your choice: ")
    
    if difficulty.isdigit():
        difficulty = int(difficulty)
    else:
        print("Invalid input, please enter a number.")
        continue
    
    if difficulty == 1:
        print("Great! You have selected the easy difficulty.")
        tries = 10
    elif difficulty == 2:
        print("Great! You have selected the medium difficulty.")
        tries = 5
    elif difficulty == 3:
        print("Great! You have selected the hard difficulty.")
        tries = 3
    else:
        print("Invalid choice, please try again.")
        continue

    # Generate a random number between 1 and 100
    random_number = random.randint(1, 100)
    guesses = 0

    # Start the guessing loop
    while guesses < tries:
        user_guess = input(f"Guess a number (You have {tries - guesses} tries left): ")

        if user_guess.isdigit():
            user_guess = int(user_guess)
        else:
            print("Please type a number next time.")
            continue

        guesses += 1

        if user_guess == random_number:
            print(f"You got it right! The number was {random_number}.")
            break
        elif user_guess > random_number:
            print("You were above the number.")
        else:
            print("You were below the number.")

        if guesses == tries:
            print(f"Sorry, you've run out of tries. The number was {random_number}.")
            break

    # Ask if the user wants to play again
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != 'yes':
        print("Thanks for playing! Goodbye!")
        break
