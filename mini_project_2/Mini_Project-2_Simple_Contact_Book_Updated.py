# ✅ Extended Contact Book (Dictionary + Set)

contacts = {
    "Rahim": "017-1234567",
    "Fatema": "018-5551234",
    "Karim": "019-8888999",
}

unique_numbers = set(contacts.values())

print("📱 Welcome to Simple Contact Book!")
print("=" * 40)

keep_running = True
while keep_running:
    print("\nMenu:")
    print("1. View all contacts")
    print("2. Add new contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Count total contacts ✅")          # NEW
    print("6. Show all names only ✅")           # NEW
    print("7. Show all phone numbers only ✅")   # NEW
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ").strip()

    if choice == "1":
        print("\n--- All Contacts ---")
        if not contacts:
            print("No contacts saved yet.")
        else:
            for name, number in contacts.items():
                print(f"• {name}: {number}")

    elif choice == "2":
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
        print("\n--- Search Contact ---")
        search_name = input("Enter name to search: ").strip()
        if search_name in contacts:
            print(f"✅ Found: {search_name} → {contacts[search_name]}")
        else:
            print("❌ Contact not found!")

    elif choice == "4":
        print("\n--- Delete Contact ---")
        name = input("Enter name to delete: ").strip()
        if name in contacts:
            deleted_number = contacts[name]
            del contacts[name]
            unique_numbers = set(contacts.values())  # rebuild for accuracy
            print(f"✅ Deleted: {name} ({deleted_number})")
        else:
            print("❌ Contact not found!")

    elif choice == "5":
        # ✅ NEW: Count total contacts
        print(f"\n📌 Total contacts: {len(contacts)}")

    elif choice == "6":
        # ✅ NEW: Show names only
        print("\n--- Names Only ---")
        if not contacts:
            print("No contacts saved yet.")
        else:
            for name in contacts.keys():  # hint used
                print(f"• {name}")

    elif choice == "7":
        # ✅ NEW: Show phone numbers only
        print("\n--- Phone Numbers Only ---")
        if not contacts:
            print("No contacts saved yet.")
        else:
            for number in contacts.values():  # hint used
                print(f"• {number}")

    elif choice == "8":
        print("\n👋 Goodbye!")
        keep_running = False

    else:
        print("❌ Invalid choice! Please enter 1-8")

print("\nProgram ended.")
