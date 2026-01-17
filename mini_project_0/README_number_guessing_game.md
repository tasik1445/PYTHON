# Number Guessing Game (Python)

A simple console game where the computer selects a random number and you try to guess it within a limited number of attempts.

## Features
- Random secret number (default range: **1–100**)
- Hints after each guess: **Too low** / **Too high**
- Input validation (rejects non-numbers and out-of-range guesses)
- Limited attempts (default: **7**)

## Requirements
- Python 3.x

## How to Run
```bash
python number_guessing_game.py
```

## How to Play
1. Run the program.
2. Enter a number when prompted.
3. Use the hints to adjust your next guess.
4. Win by guessing the correct number before attempts run out.

## Customize (Optional)
In the code you can change:
- `min_n`, `max_n` (number range)
- `max_attempts` (allowed tries)

Example:
```python
play_number_guessing_game(min_n=1, max_n=50, max_attempts=5)
```

## License
Free to use for learning and practice.
