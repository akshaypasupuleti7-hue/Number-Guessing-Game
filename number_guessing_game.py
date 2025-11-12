# number_guessing_game.py
import random

def get_int_input(prompt, min_val=None, max_val=None):
    while True:
        try:
            val = int(input(prompt))
            if min_val is not None and val < min_val:
                print(f"Please enter a number >= {min_val}.")
                continue
            if max_val is not None and val > max_val:
                print(f"Please enter a number <= {max_val}.")
                continue
            return val
        except ValueError:
            print("Invalid input — enter an integer.")

def play_game(min_num=1, max_num=100):
    target = random.randint(min_num, max_num)
    attempts = 0
    print(f"\nI have chosen a number between {min_num} and {max_num}. Try to guess it!")

    while True:
        guess = get_int_input("Your guess: ", min_num, max_num)
        attempts += 1
        if guess < target:
            print("Too low. Try again.")
        elif guess > target:
            print("Too high. Try again.")
        else:
            print(f"Correct! You guessed it in {attempts} attempts.")
            return attempts

def choose_difficulty():
    print("\nChoose difficulty:")
    print("1. Easy (1-20)")
    print("2. Medium (1-100)")
    print("3. Hard (1-1000)")
    choice = get_int_input("Select 1, 2, or 3: ", 1, 3)
    if choice == 1:
        return 1, 20
    if choice == 2:
        return 1, 100
    return 1, 1000

def main():
    print("=== Number Guessing Game ===")
    best_score = None

    while True:
        min_num, max_num = choose_difficulty()
        attempts = play_game(min_num, max_num)
        if best_score is None or attempts < best_score:
            best_score = attempts
            print(f"New best score: {best_score} attempts!")

        replay = input("Play again? (y/n): ").strip().lower()
        if replay != 'y':
            print("Thanks for playing! Goodbye.")
            break

if __name__ == "__main__":
    main()