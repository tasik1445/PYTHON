# ✅ Simple Contact Book using Dictionary + Set

contacts = {
    "Rahim": "017-1234567",
    "Fatema": "018-5551234",
    "Karim": "019-8888999",
}

# Track unique phone numbers (no duplicates)
unique_numbers = set(contacts.values())

print("📱 Welcome to Simple Contact Book!")
print("=" * 40)

keep_running = True
while keep_running:
    print("\nWhat do you want to do?")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("\nEnter your choice (1-5): ").strip()

    if choice == "1":
        # View all contacts
        print("\n--- All Contacts ---")
        if len(contacts) == 0:
            print("No contacts saved yet.")
        else:
            for name, number in contacts.items():
                print(f"• {name}: {number}")
            print(f"\nTotal contacts: {len(contacts)}")
            print(f"Unique phone numbers: {len(unique_numbers)}")

    elif choice == "2":
        # Add new contact
        print("\n--- Add New Contact ---")
        name = input("Enter name: ").strip()

        if name == "":
            print("❌ Name cannot be empty!")
            continue

        if name in contacts:
            print(f"⚠️ {name} already exists with number: {contacts[name]}")
            continue

        number = input("Enter phone number: ").strip()

        if number == "":
            print("❌ Phone number cannot be empty!")
            continue

        contacts[name] = number
        unique_numbers.add(number)
        print(f"✅ Contact saved: {name} → {number}")

    elif choice == "3":
        # Search contact
        print("\n--- Search Contact ---")
        search_name = input("Enter name to search: ").strip()

        if search_name in contacts:
            print(f"✅ Found: {search_name} → {contacts[search_name]}")
        else:
            print("❌ Contact not found!")

    elif choice == "4":
        # Delete contact
        print("\n--- Delete Contact ---")
        name = input("Enter name to delete: ").strip()

        if name in contacts:
            deleted_number = contacts[name]
            del contacts[name]

            # Rebuild unique set to stay accurate (simple + safe)
            unique_numbers = set(contacts.values())

            print(f"✅ Deleted contact: {name} ({deleted_number})")
        else:
            print("❌ Contact not found!")

    elif choice == "5":
        print("\n👋 Goodbye!")
        keep_running = False

    else:
        print("❌ Invalid choice! Please enter 1-5")

print("\nProgram ended.")
