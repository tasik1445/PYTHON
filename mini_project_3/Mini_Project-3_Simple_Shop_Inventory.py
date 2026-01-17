# ✅ Simple Shop Inventory using Dictionary + Sets

# Product prices (dictionary)
products = {
    "Rice": 65,
    "Oil": 180,
    "Sugar": 140,
    "Salt": 35,
    "Milk": 90
}

# Categories (set: avoids duplicates)
categories = {"Food", "Drinks", "Snacks"}

# Stock tracking (sets)
in_stock = set(products.keys())
out_of_stock = set()

print("🏪 Welcome to Simple Shop Inventory!")
print("=" * 40)

keep_running = True
while keep_running:
    print("\nWhat do you want to do?")
    print("1. View all products and prices")
    print("2. Add new product")
    print("3. Update price")
    print("4. Mark product as out of stock")
    print("5. Mark product as back in stock")
    print("6. View stock status")
    print("7. Calculate total value (in-stock only)")
    print("8. Exit")

    choice = input("\nEnter your choice (1-8): ").strip()

    if choice == "1":
        # View all products
        print("\n--- All Products ---")
        if len(products) == 0:
            print("No products in shop!")
        else:
            print(f"{'Product':<15} {'Price (৳)':<10} {'Status'}")
            print("-" * 40)
            for product, price in products.items():
                status = "✅ Available" if product in in_stock else "❌ Out of Stock"
                print(f"{product:<15} {price:<10} {status}")

    elif choice == "2":
        # Add new product
        print("\n--- Add New Product ---")
        product_name = input("Enter product name: ").strip()

        if product_name == "":
            print("❌ Product name cannot be empty!")
            continue

        if product_name in products:
            print(f"⚠️ {product_name} already exists!")
            continue

        price_text = input("Enter price in Taka: ").strip()
        if not price_text.isdigit():
            print("❌ Price must be a number!")
            continue
        price = int(price_text)

        products[product_name] = price

        stock_status = input("Is it in stock? (yes/no): ").strip().lower()
        if stock_status == "yes":
            in_stock.add(product_name)
            out_of_stock.discard(product_name)
        else:
            out_of_stock.add(product_name)
            in_stock.discard(product_name)

        print(f"✅ {product_name} added with price ৳{price}")

    elif choice == "3":
        # Update price
        print("\n--- Update Price ---")
        product_name = input("Enter product name: ").strip()

        if product_name not in products:
            print(f"❌ {product_name} not found!")
            continue

        old_price = products[product_name]
        print(f"Current price: ৳{old_price}")

        new_price_text = input("Enter new price: ").strip()
        if not new_price_text.isdigit():
            print("❌ Price must be a number!")
            continue
        new_price = int(new_price_text)

        products[product_name] = new_price
        print(f"✅ Price updated from ৳{old_price} to ৳{new_price}")

    elif choice == "4":
        # Mark out of stock
        print("\n--- Mark Out of Stock ---")
        product_name = input("Enter product name: ").strip()

        if product_name not in products:
            print(f"❌ {product_name} not found!")
        elif product_name in out_of_stock:
            print(f"⚠️ {product_name} is already out of stock!")
        else:
            in_stock.discard(product_name)
            out_of_stock.add(product_name)
            print(f"✅ {product_name} marked as out of stock")

    elif choice == "5":
        # Mark back in stock
        print("\n--- Mark Back in Stock ---")
        product_name = input("Enter product name: ").strip()

        if product_name not in products:
            print(f"❌ {product_name} not found!")
        elif product_name in in_stock:
            print(f"⚠️ {product_name} is already in stock!")
        else:
            out_of_stock.discard(product_name)
            in_stock.add(product_name)
            print(f"✅ {product_name} is back in stock!")

    elif choice == "6":
        # View stock status
        print("\n--- Stock Status ---")

        print(f"\n✅ In Stock ({len(in_stock)} items):")
        if len(in_stock) == 0:
            print("  No items in stock")
        else:
            for item in in_stock:
                print(f" • {item}: ৳{products[item]}")

        print(f"\n❌ Out of Stock ({len(out_of_stock)} items):")
        if len(out_of_stock) == 0:
            print("  All items are in stock")
        else:
            for item in out_of_stock:
                if item in products:
                    print(f" • {item}: ৳{products[item]}")

    elif choice == "7":
        # Calculate total value (in-stock only)
        print("\n--- Shop Value ---")
        total_value = 0
        for product in in_stock:
            total_value += products[product]

        print(f"Total value of in-stock items: ৳{total_value}")
        print(f"Number of products in stock: {len(in_stock)}")
        print(f"Number of products out of stock: {len(out_of_stock)}")

    elif choice == "8":
        print("\n👋 Thank you for using Shop Inventory!")
        keep_running = False

    else:
        print("❌ Invalid choice! Please enter 1-8")

print("\nProgram ended.")
