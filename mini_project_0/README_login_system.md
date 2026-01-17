# Login System (Python)

A beginner-friendly console program that simulates a simple login system using a fixed username and password.

## Features
- Predefined username & password
- Maximum attempts (default: **3**)
- Locks the user out after too many failed attempts

## Requirements
- Python 3.x

## How to Run
```bash
python login_system.py
```

## Default Credentials
The credentials are set in the code:

- Username: `admin`
- Password: `1234`

> You can change them in `login_system.py` by editing the `USERNAME` and `PASSWORD` variables.

## Customize (Optional)
Change the number of allowed tries:
```python
login(max_attempts=5)
```

## License
Free to use for learning and practice.
