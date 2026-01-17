# ✅ Extended Shop Inventory (Dictionary + Sets)

products = {
    "Rice": 65,
    "Oil": 180,
    "Sugar": 140,
    "Salt": 35,
    "Milk": 90
}

in_stock = set(products.keys())
out_of_stock = set()

print("🏪 Welcome to Simple Shop Inventory!")
print("=" * 40)

keep_running = True
while keep_running:
    print("\nMenu:")
    print("1. View all products and prices")
    print("2. Add new product")
    print("3. Update price")
    print("4. Mark product as out of stock")
    print("5. Mark product as back in stock")
    print("6. View stock status")
    print("7. Calculate total value (in-stock only)")
    print("8. Find most expensive product ✅")   # NEW
    print("9. Find cheapest product ✅")         # NEW
    print("10. Count products under 100 ✅")     # NEW
    print("11. Exit")

    choice = input("\nEnter your choice (1-11): ").strip()

    if choice == "1":
        print("\n--- All Products ---")
        if not products:
            print("No products in shop!")
        else:
            print(f"{'Product':<15} {'Price(৳)':<10} {'Status'}")
            print("-" * 40)
            for product, price in products.items():
                status = "✅ Available" if product in in_stock else "❌ Out of Stock"
                print(f"{product:<15} {price:<10} {status}")

    elif choice == "2":
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
        print("\n--- Update Price ---")
        product_name = input("Enter product name: ").strip()
        if product_name not in products:
            print(f"❌ {product_name} not found!")
            continue

        old_price = products[product_name]
        new_price_text = input(f"Current price is ৳{old_price}. Enter new price: ").strip()
        if not new_price_text.isdigit():
            print("❌ Price must be a number!")
            continue

        products[product_name] = int(new_price_text)
        print("✅ Price updated!")

    elif choice == "4":
        print("\n--- Mark Out of Stock ---")
        product_name = input("Enter product name: ").strip()
        if product_name not in products:
            print("❌ Product not found!")
        else:
            in_stock.discard(product_name)
            out_of_stock.add(product_name)
            print(f"✅ {product_name} marked out of stock")

    elif choice == "5":
        print("\n--- Mark Back In Stock ---")
        product_name = input("Enter product name: ").strip()
        if product_name not in products:
            print("❌ Product not found!")
        else:
            out_of_stock.discard(product_name)
            in_stock.add(product_name)
            print(f"✅ {product_name} is back in stock")

    elif choice == "6":
        print("\n--- Stock Status ---")
        print(f"✅ In Stock ({len(in_stock)}): {sorted(in_stock)}")
        print(f"❌ Out of Stock ({len(out_of_stock)}): {sorted(out_of_stock)}")

    elif choice == "7":
        print("\n--- Total Value (In-stock only) ---")
        total_value = sum(products[p] for p in in_stock if p in products)
        print(f"Total value: ৳{total_value}")

    elif choice == "8":
        # ✅ NEW: Most expensive product
        if not products:
            print("❌ No products available!")
        else:
            name, price = max(products.items(), key=lambda item: item[1])
            print(f"💰 Most expensive: {name} = ৳{price}")

    elif choice == "9":
        # ✅ NEW: Cheapest product
        if not products:
            print("❌ No products available!")
        else:
            name, price = min(products.items(), key=lambda item: item[1])
            print(f"🪙 Cheapest: {name} = ৳{price}")

    elif choice == "10":
        # ✅ NEW: Count products under 100 Taka
        count_under_100 = sum(1 for price in products.values() if price < 100)
        print(f"📌 Products under ৳100: {count_under_100}")

    elif choice == "11":
        print("\n👋 Thank you for using Inventory!")
        keep_running = False

    else:
        print("❌ Invalid choice! Please enter 1-11")

print("\nProgram ended.")
