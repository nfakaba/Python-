import random

# First guessing game
secretnumber = random.randint(1, 40)  # Random number between 1 and 40
print('I am thinking of a number between 1 and 40.')

for i in range(1, 6):  #Allow 5 guesses in the first game
    print('Take a guess:')
    try:
        guess = int(input())  # Ensure the input is an integer
    except ValueError:  # Handle invalid inputs
        print('Please put a valid number.')  # Inform the user
        continue  # Skip to the next iteration and ask again

    # Check if the guess is too low, too high, or correct
    if guess < secretnumber:
        print('Your guess is too low.')
    elif guess > secretnumber:
        print('Your guess is too high.')
    else:
        # Correct guess in the first game
        print(f'Good job! You guessed it in {i} guesses. Now let\'s move on to the next round.')

        # Second guessing game starts here
        while True: # Infinite loop for the second game; breaks after completion
            secretnumber2 = random.randint(40, 100)  # Random number for the second game
            print('I am thinking of a number between 40 and 100.')

            for s in range(1, 6):  # Allow 5 guesses in the second game
                print('Take a guess:')
                try:
                    guess2 = int(input())  # Ensure the input is an integer
                except ValueError:  # Handle invalid inputs
                    print('Please put a valid number.')
                    continue  # Skip to the next iteration and ask again

                # Check if the guess is too high, too low, or correct
                if guess2 > secretnumber2:
                    print('Your guess is too high.')
                elif guess2 < secretnumber2:
                    print('Your guess is too low.')
                else:
                    # Correct guess in the second game
                    print(f'Good job! You guessed it in {s} guesses. Well done!')
                    break  # Exit the second game's loop
            else:
                # Executes only if the second game's loop completes without a correct guess
                print(f'Nope. The number I was thinking of was {secretnumber2}.')
            break  # Exit the while loop for the second game
        break  # Exit the first game's loop after transitioning to the second game

else:
    # Executes only if the first game's loop completes without a correct guess
    print(f'Nope. The number I was thinking of was {secretnumber}.')