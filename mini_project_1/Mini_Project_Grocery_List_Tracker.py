# 1. Basic Setup
# Initialize an empty grocery list
grocery_list = []

# Some items to start with (optional)
grocery_list = ["milk", "bread", "eggs"]

print("🛒 Welcome to Grocery List Manager!")
print("Current list:", grocery_list)

# 2. Display Menu
# Create a simple menu system
print("\n" + "="*40)
print("GROCERY LIST MANAGER")
print("="*40)
print("Current items:", len(grocery_list))
print("\nWhat would you like to do?")
print("1. View all items")
print("2. Add new item")
print("3. Remove item")
print("4. Check if item exists")
print("5. Clear entire list")
print("6. Exit")

# 3. Complete Program
# Complete Grocery List Manager
grocery_list = ["milk", "bread", "eggs"]

# Program runs until user chooses to exit
keep_running = True

while keep_running:
    # Display menu
    print("\n" + "="*40)
    print("🛒 GROCERY LIST MANAGER")
    print("="*40)
    print(f"Current items in list: {len(grocery_list)}")
    print("\n1. View all items")
    print("2. Add new item")
    print("3. Remove item")
    print("4. Check if item exists")
    print("5. Clear entire list")
    print("6. Sort list alphabetically")
    print("7. Exit")

    # Get user choice
    choice = input("\nEnter your choice (1-7): ")

    # Process the choice
    if choice == "1":
        # View all items
        if len(grocery_list) == 0:
            print("\n❌ Your grocery list is empty!")
        else:
            print("\n📋 Your Grocery List:")
            print("-" * 20)
            # Using for loop with enumerate for numbering
            for index, item in enumerate(grocery_list):
                print(f"{index + 1}. {item}")

    elif choice == "2":
        # Add new item
        new_item = input("\nEnter item to add: ").lower()

        # Check if item already exists
        if new_item in grocery_list:
            print(f"⚠️  '{new_item}' is already in your list!")
        else:
            grocery_list.append(new_item)
            print(f"✅ '{new_item}' added to your list!")

    elif choice == "3":
        # Remove item
        if len(grocery_list) == 0:
            print("\n❌ List is empty! Nothing to remove.")
        else:
            # Show current items first
            print("\nCurrent items:")
            for index, item in enumerate(grocery_list):
                print(f"{index + 1}. {item}")

            item_to_remove = input("\nEnter item name to remove: ").lower()

            if item_to_remove in grocery_list:
                grocery_list.remove(item_to_remove)
                print(f"✅ '{item_to_remove}' removed from list!")
            else:
                print(f"❌ '{item_to_remove}' not found in list!")

    elif choice == "4":
        # Check if item exists
        item_to_check = input("\nEnter item to search: ").lower()

        if item_to_check in grocery_list:
            # Find its position
            position = grocery_list.index(item_to_check)
            print(f"✅ '{item_to_check}' is in your list at position {position + 1}")
        else:
            print(f"❌ '{item_to_check}' is not in your list")

    elif choice == "5":
        # Clear entire list
        confirm = input("\n⚠️  Are you sure you want to clear the entire list? (yes/no): ")
        if confirm.lower() == "yes":
            grocery_list.clear()  # or grocery_list = []
            print("✅ List cleared!")
        else:
            print("❌ Clear cancelled")

    elif choice == "6":
        # Sort list
        grocery_list.sort()
        print("✅ List sorted alphabetically!")
        # Show sorted list
        print("\nSorted list:")
        for item in grocery_list:
            print(f"  • {item}")

    elif choice == "7":
        # Exit
        print("\n👋 Thank you for using Grocery List Manager!")
        print(f"Final list has {len(grocery_list)} items")
        keep_running = False

    else:
        print("\n❌ Invalid choice! Please enter 1-7")

print("\nProgram ended.")

