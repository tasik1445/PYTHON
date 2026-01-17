"""Login System (Console)

Based on the class handout: predefined username/password, 3 attempts,
lock account after failed attempts. fileciteturn7file0L26-L41
"""

USERNAME = "admin"
PASSWORD = "1234"


def login(max_attempts: int = 3) -> None:
    attempts_left = max_attempts

    print("🔐 Login System")
    print(f"You have {max_attempts} attempt(s).\n")

    while attempts_left > 0:
        user = input("Enter username: ").strip()
        pwd = input("Enter password: ").strip()

        if user == USERNAME and pwd == PASSWORD:
            print(f"✅ Login successful! Welcome, {user}.")
            return

        attempts_left -= 1
        print(f"❌ Incorrect username or password. Attempts left: {attempts_left}\n")

    print("🚫 Account locked due to too many failed attempts.")


if __name__ == "__main__":
    login()
