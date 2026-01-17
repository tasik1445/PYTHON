"""Number Guessing Game (Console)

Based on the class handout: random number 1–100, hints (too high/low),
maximum attempts, loop + break/continue. fileciteturn7file0L10-L25
"""

import random


def play_number_guessing_game(min_n: int = 1, max_n: int = 100, max_attempts: int = 7) -> None:
    secret = random.randint(min_n, max_n)
    attempts = 0

    print("🎯 Number Guessing Game")
    print(f"I'm thinking of a number between {min_n} and {max_n}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        raw = input(f"Guess ({min_n}-{max_n}): ").strip()

        # Basic validation
        try:
            guess = int(raw)
        except ValueError:
            print("⚠️ Please enter a valid integer.")
            continue

        if guess < min_n or guess > max_n:
            print(f"⚠️ Out of range! Enter a number between {min_n} and {max_n}.")
            continue

        attempts += 1

        if guess == secret:
            print(f"✅ Correct! 🎉 You guessed it in {attempts} attempt(s).")
            return
        elif guess < secret:
            print("⬇️ Too low!")
        else:
            print("⬆️ Too high!")

        print(f"Attempts left: {max_attempts - attempts}\n")

    print(f"❌ Sorry, you lost. The number was: {secret}")


if __name__ == "__main__":
    play_number_guessing_game()
