import random

def guess_number():
    print("Think of a number between 1 and 100, and I'll try to guess it!")
    low = 1
    high = 100
    attempts = 0

    while True:
        attempts += 1
        guess = random.randint(low, high)
        print(f"My guess is: {guess}")
        feedback = input("Is it too high (H), too low (L), or correct (C)? ").lower()

        if feedback == 'c':
            print(f"I guessed it in {attempts} attempts!")
            break
        elif feedback == 'h':
            high = guess - 1
        elif feedback == 'l':
            low = guess + 1
        else:
            print("Invalid input. Please enter 'H', 'L', or 'C'.")

guess_number()
