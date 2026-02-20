from datetime import datetime
import os

# ======= FILE PATHS =======
BOOKS_FILE = "data/books.txt"
GENRES_FILE = "data/genres.txt"
REPORT_FILE = "reports/library_report.txt"

SEPARATOR = "|"

VALID_STATUSES = ["Available", "Reading", "Finished"]


# ============================================
#  FILE SETUP
# ============================================

def setup_files():
    """Check if data files/folders exist. If not, create them with defaults."""
    # Ensure folders exist
    os.makedirs(os.path.dirname(BOOKS_FILE), exist_ok=True)    # data/
    os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)   # reports/

    # --- Create genres.txt if missing ---
    try:
        with open(GENRES_FILE, "r", encoding="utf-8") as file:
            _ = file.read()
    except Exception:
        try:
            with open(GENRES_FILE, "w", encoding="utf-8") as file:
                file.write(
                    "Fiction\nNon-Fiction\nSci-Fi\nSelf-Help\nProgramming\nHistory\nBiography\nOther\n"
                )
            print("✓ Genres file created")
        except Exception as error:
            print(f"⚠ Could not create genres file: {error}")

    # --- Create books.txt if missing ---
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            _ = file.readline()
    except Exception:
        try:
            with open(BOOKS_FILE, "w", encoding="utf-8") as file:
                file.write("Title|Author|Genre|Year|Status\n")
            print("✓ Books file created")
        except Exception as error:
            print(f"⚠ Could not create books file: {error}")


# ============================================
#  LOAD DATA FUNCTIONS
# ============================================

def load_genres():
    """Load all genres from genres.txt and return as a list."""
    genres = []
    try:
        with open(GENRES_FILE, "r", encoding="utf-8") as file:
            for line in file.readlines():
                line = line.strip()
                if line:
                    genres.append(line)
        return genres
    except FileNotFoundError:
        print("⚠ Genres file not found!")
        return []
    except Exception as error:
        print(f"⚠ Error reading genres file: {error}")
        return []


def load_all_books():
    """Load all books from books.txt and return as a list of lists (5 fields each)."""
    books = []
    try:
        with open(BOOKS_FILE, "r", encoding="utf-8") as file:
            lines = file.readlines()

        if not lines:
            return []

        # Skip header (first line)
        for line in lines[1:]:
            line = line.strip()
            if not line:
                continue
            parts = line.split(SEPARATOR)
            # Only accept valid rows
            if len(parts) == 5:
                books.append([p.strip() for p in parts])

        return books

    except FileNotFoundError:
        # If books file missing, create it
        setup_files()
        return []
    except Exception as error:
        print(f"⚠ Error loading books: {error}")
        return []


# ============================================
#  HELPER / VALIDATION FUNCTIONS
# ============================================

def display_menu():
    """Show the main menu."""
    print("\n" + "=" * 50)
    print("       📚 LIBRARY BOOK MANAGER 📚")
    print("=" * 50)
    print("1. Add a Book")
    print("2. View All Books")
    print("3. Search Books")
    print("4. Update Book Status")
    print("5. Delete a Book")
    print("6. Reading Statistics")
    print("7. Generate Library Report")
    print("8. Exit")
    print("=" * 50)


def get_non_empty_input(prompt):
    """Ask input until user gives a non-empty value."""
    while True:
        value = input(prompt).strip()
        if value:
            return value
        print("⚠ This field cannot be empty!")


def get_valid_genre(genres):
    """Show genre list and let user pick one. Return the chosen genre."""
    print("\nAvailable Genres:")
    for i, genre in enumerate(genres, start=1):
        print(f"  {i}. {genre}")

    while True:
        try:
            choice = int(input(f"Select genre (1-{len(genres)}): "))
            if 1 <= choice <= len(genres):
                return genres[choice - 1]
            else:
                print(f"⚠ Please enter a number between 1 and {len(genres)}")
        except ValueError:
            print("⚠ Please enter a valid number!")


def get_valid_year():
    """Ask user for a year and validate it."""
    current_year = datetime.now().year
    while True:
        try:
            year = int(input("Enter publication year: "))
            if 1000 <= year <= current_year:
                return str(year)
            print(f"⚠ Year must be between 1000 and {current_year}")
        except ValueError:
            print("⚠ Please enter a valid year!")


def get_valid_status():
    """Let user pick a book status: Available, Reading, or Finished."""
    print("\nBook Status:")
    for i, status in enumerate(VALID_STATUSES, start=1):
        print(f"  {i}. {status}")

    while True:
        try:
            choice = int(input("Select status (1-3): "))
            if 1 <= choice <= len(VALID_STATUSES):
                return VALID_STATUSES[choice - 1]
            print("⚠ Please enter 1, 2, or 3")
        except ValueError:
            print("⚠ Please enter a valid number!")


def save_book(title, author, genre, year, status):
    """Append one book to books.txt."""
    try:
        with open(BOOKS_FILE, "a", encoding="utf-8") as file:
            line = SEPARATOR.join([title, author, genre, year, status])
            file.write(line + "\n")
        print("✓ Book saved successfully!")
        return True
    except Exception as error:
        print(f"⚠ Error saving book: {error}")
        return False


def save_all_books(books):
    """Rewrite the entire books.txt with header + all books in the list.
    Use this when you update or delete a book."""
    try:
        with open(BOOKS_FILE, "w", encoding="utf-8") as file:
            file.write("Title|Author|Genre|Year|Status\n")  # Header
            for book in books:
                line = SEPARATOR.join(book)
                file.write(line + "\n")
        return True
    except Exception as error:
        print(f"⚠ Error saving books: {error}")
        return False


def print_book(book, idx=None):
    """Pretty print a single book record."""
    title, author, genre, year, status = book
    if idx is None:
        print(f"Title : {title}")
    else:
        print(f"[{idx}] {title}")
    print(f"Author: {author}")
    print(f"Genre : {genre}")
    print(f"Year  : {year}")
    print(f"Status: {status}")


def pick_book_index(books):
    """Ask user to pick a book index (1..len) and return 0-based index."""
    while True:
        try:
            choice = int(input(f"Select a book (1-{len(books)}): "))
            if 1 <= choice <= len(books):
                return choice - 1
            print(f"⚠ Please enter a number between 1 and {len(books)}")
        except ValueError:
            print("⚠ Please enter a valid number!")


# ============================================
#  MAIN FEATURES
# ============================================

def add_book():
    """Feature 1: Add a new book."""
    print("\n=== ADD A BOOK ===")
    genres = load_genres()
    if not genres:
        print("⚠ No genres available!")
        return

    title = get_non_empty_input("Enter book title: ")
    author = get_non_empty_input("Enter author name: ")
    genre = get_valid_genre(genres)
    year = get_valid_year()
    status = get_valid_status()

    save_book(title, author, genre, year, status)


def view_all_books():
    """Feature 2: View all books sorted by title."""
    print("\n=== ALL BOOKS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    # Sort alphabetically by title (index 0)
    books.sort(key=lambda b: b[0].lower())

    for i, book in enumerate(books, start=1):
        print("-" * 50)
        print_book(book, idx=i)

    print("-" * 50)
    print(f"Total Books: {len(books)}")


def search_books():
    """Feature 3: Search books by keyword."""
    print("\n=== SEARCH BOOKS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    keyword = input("Enter search keyword: ").strip().lower()
    if not keyword:
        print("⚠ Keyword cannot be empty!")
        return

    matches = []
    for book in books:
        title, author, genre, year, status = book
        if (keyword in title.lower()) or (keyword in author.lower()) or (keyword in genre.lower()):
            matches.append(book)

    if len(matches) == 0:
        print("No results found")
        return

    print(f"\nFound {len(matches)} result(s):")
    for i, book in enumerate(sorted(matches, key=lambda b: b[0].lower()), start=1):
        print("-" * 50)
        print_book(book, idx=i)
    print("-" * 50)


def update_book_status():
    """Feature 4: Update a book's reading status."""
    print("\n=== UPDATE BOOK STATUS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    # Show all books with numbers
    books.sort(key=lambda b: b[0].lower())
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book[0]}  ({book[4]})")

    index = pick_book_index(books)
    print("\nSelected book:")
    print("-" * 50)
    print_book(books[index])
    print("-" * 50)
    print(f"Current status: {books[index][4]}")

    new_status = get_valid_status()
    books[index][4] = new_status

    if save_all_books(books):
        print("✓ Status updated successfully!")


def delete_book():
    """Feature 5: Delete a book with confirmation."""
    print("\n=== DELETE A BOOK ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    # Show all books with numbers
    books.sort(key=lambda b: b[0].lower())
    for i, book in enumerate(books, start=1):
        print(f"{i}. {book[0]}  ({book[1]})")

    index = pick_book_index(books)

    print("\nYou are about to delete:")
    print("-" * 50)
    print_book(books[index])
    print("-" * 50)

    while True:
        confirm = input("Are you sure? (y/n): ").strip().lower()
        if confirm in ("y", "n"):
            break
        print("⚠ Please type 'y' or 'n'")

    if confirm == "y":
        books.pop(index)
        if save_all_books(books):
            print("✓ Book deleted successfully!")
    else:
        print("ℹ Delete cancelled.")


def reading_statistics():
    """Feature 6: Show reading stats and genre breakdown."""
    print("\n=== READING STATISTICS ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    # --- Count by status ---
    available_count = 0
    reading_count = 0
    finished_count = 0

    for book in books:
        status = book[4]
        if status == "Available":
            available_count += 1
        elif status == "Reading":
            reading_count += 1
        elif status == "Finished":
            finished_count += 1

    total = len(books)

    print("\nStatus Breakdown")
    print("-" * 50)
    print(f"Available: {available_count}")
    print(f"Reading  : {reading_count}")
    print(f"Finished : {finished_count}")
    print(f"Total    : {total}")

    # --- Genre breakdown ---
    genre_counts = {}
    for book in books:
        genre = book[2]
        genre_counts[genre] = genre_counts.get(genre, 0) + 1

    print("\nGenre Breakdown")
    print("-" * 50)
    # Print genres sorted by count desc then name
    for genre, count in sorted(genre_counts.items(), key=lambda x: (-x[1], x[0].lower())):
        print(f"{genre}: {count}")


def generate_report():
    """Feature 7: Generate and save a library report."""
    print("\n=== GENERATE LIBRARY REPORT ===")
    books = load_all_books()

    if len(books) == 0:
        print("No books found!")
        return

    genres = load_genres()
    print("\nReport Options:")
    print("1. Show ALL books")
    print("2. Filter by GENRE")

    choice = input("Choose (1-2): ").strip()

    filtered = books
    selected_genre = None

    if choice == "2":
        if not genres:
            print("⚠ No genres available!")
            return
        selected_genre = get_valid_genre(genres)
        filtered = [b for b in books if b[2] == selected_genre]

        if len(filtered) == 0:
            print(f"⚠ No books found for genre: {selected_genre}")
            return

    # Compute stats for filtered books
    status_counts = {"Available": 0, "Reading": 0, "Finished": 0}
    for b in filtered:
        if b[4] in status_counts:
            status_counts[b[4]] += 1

    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    header = "LIBRARY REPORT"
    scope = "ALL BOOKS" if selected_genre is None else f"GENRE: {selected_genre}"

    lines = []
    lines.append(header)
    lines.append(f"Generated: {now}")
    lines.append(f"Scope    : {scope}")
    lines.append("=" * 60)
    lines.append(f"Total Books: {len(filtered)}")
    lines.append("")
    lines.append("Status Breakdown:")
    for s in VALID_STATUSES:
        lines.append(f"  - {s}: {status_counts.get(s,0)}")
    lines.append("=" * 60)
    lines.append("Book List (sorted by title)")
    lines.append("-" * 60)

    for title, author, genre, year, status in sorted(filtered, key=lambda x: x[0].lower()):
        lines.append(f"{title} | {author} | {genre} | {year} | {status}")

    report_text = "\n".join(lines) + "\n"

    # Save report
    try:
        os.makedirs(os.path.dirname(REPORT_FILE), exist_ok=True)
        with open(REPORT_FILE, "w", encoding="utf-8") as file:
            file.write(report_text)
        print(f"✓ Report saved to: {REPORT_FILE}")
    except Exception as error:
        print(f"⚠ Error saving report: {error}")


# ============================================
#  MAIN PROGRAM
# ============================================

def main():
    setup_files()
    print("\n🎉 Welcome to Library Book Manager!")

    while True:
        display_menu()

        try:
            choice = input("\n👉 Enter your choice (1-8): ").strip()

            if choice == "1":
                add_book()

            elif choice == "2":
                view_all_books()

            elif choice == "3":
                search_books()

            elif choice == "4":
                update_book_status()

            elif choice == "5":
                delete_book()

            elif choice == "6":
                reading_statistics()

            elif choice == "7":
                generate_report()

            elif choice == "8":
                print("\n👋 Thank you for using Library Book Manager!")
                print("📚 Happy Reading! Goodbye!")
                break

            else:
                print("⚠ Invalid choice! Please enter a number between 1-8")

        except KeyboardInterrupt:
            print("\n👋 Program interrupted. Goodbye!")
            break

        except Exception as error:
            print(f"⚠ An error occurred: {error}")


if __name__ == "__main__":
    main()
