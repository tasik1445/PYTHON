# Simple Shop Inventory (Python)

A beginner-friendly **menu-driven console app** for managing a small shop inventory using:
- **Dictionary** for `product -> price`
- **Sets** to track **in-stock** and **out-of-stock** items

The program lets you add products, update prices, manage stock status, and calculate inventory statistics. fileciteturn6file0

---

## Features

- 📦 View all products with price + stock status
- ➕ Add new product (with input validation)
- ✏️ Update product price
- ❌ Mark a product as out of stock
- ✅ Mark a product as back in stock
- 📋 View stock summary (in-stock vs out-of-stock)
- 🧮 Calculate total inventory value (in-stock only)
- 💰 Find most expensive product
- 🪙 Find cheapest product
- 📌 Count products under ৳100
- 🚪 Exit

---

## Requirements

- Python 3.x

---

## How to Run

Open a terminal in the project folder and run:

```bash
python Mini_Project-3_Simple_Shop_Inventory_Updated.py
```

---

## Menu Options

1. View all products and prices  
2. Add new product  
3. Update price  
4. Mark product as out of stock  
5. Mark product as back in stock  
6. View stock status  
7. Calculate total value (in-stock only)  
8. Find most expensive product  
9. Find cheapest product  
10. Count products under 100  
11. Exit  

---

## Data Structures Used

### Dictionary (`products`)
Stores product prices:
```python
products = {"Rice": 65, "Oil": 180, "Sugar": 140}
```

### Sets (`in_stock`, `out_of_stock`)
Track product availability:
- `in_stock` contains product names currently available
- `out_of_stock` contains product names currently not available

---

## Notes
- Input validation is included (empty name check, numeric price check).
- Total value uses **in-stock products only**.

---

## License
Free to use for learning and practice.
