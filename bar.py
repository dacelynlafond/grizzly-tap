import csv

inventory_file = "inventory.csv" #new way to view inventory
SALES_FILE = "sales.csv" #new way to view sales

sales = []

# Main data: each menu item with its price, cost, quantity on hand, and reorder level
inventory = {} #load invetory function will fill this with csv data

#loads the inventory from the csv file into the inventory dictionary changes text to int or float
def load_inventory():
    with open (inventory_file, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            inventory[row["item"]] = {
                    "price": float(row["price"]),
                    "cost": float(row["cost"]),
                    "quantity": int(row["quantity"]),
                    "reorder": int(row["reorder"])}

#loads inventory dictionary from the csv file      
def save_inventory():
    with open(inventory_file, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["item", "price", "cost", "quantity", "reorder"])
        for item, info in inventory.items():
            writer.writerow([item, info["price"], info["cost"],
                             info["quantity"], info["reorder"]])
            
# Adds inventory option to menu
def view_inventory():
    print(f"\n{'Item':<10}{'Price':>8}{'Cost':>8}{'Qty':>6}{'Reorder':>9}")
    for item, info in inventory.items():
        print(f"{item:<10}${info['price']:>7.2f}${info['cost']:>7.2f}"
              f"{info['quantity']:>6}{info['reorder']:>9}")

#loads sales list from the sales csv file
def load_sales():
    with open(SALES_FILE, "r") as f:
        reader = csv.DictReader(f)
        for row in reader:
            sales.append({
                "date": row["date"],
                 "item": row["item"],
                 "quantity": int(row["quantity"]),
                 "total": float(row["total"]),
                 "game_day": row["game_day"]})

#writes a new sale to the sales csv
def save_sales():
    with open(SALES_FILE, "w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["date", "item", "quantity", "total", "game_day"])
        for sale in sales:
            writer.writerow([sale["date"], sale["item"], sale["quantity"],
                             sale["total"], sale["game_day"]])
            
# Asks for a whole number greater than 0; returns None if the input is invalid
def get_positive_int(prompt):
    while True:
        text = input(prompt).strip()
        if text.isdigit() and int(text) > 0:
            return int(text)
        print("Please enter a whole number greater than 0 (no letters).")

# Keeps asking until the user enters a number (like 12.50) greater than 0
def get_positive_float(prompt):
    while True:
        text = input(prompt).strip()
        if text.replace(".", "", 1).isdigit() and float(text) > 0:
            return float(text)
        print("Please enter a number greater than 0 (no letters).")

# Restocks an existing item, or asks for details and adds a new item
def add_or_update_item():
    item = input("Item name: ").strip().lower()

    if item in inventory:
        amount = get_positive_int("How many to add? ")
        inventory[item]["quantity"] += amount
        print("Restocked.", item, "now has", inventory[item]["quantity"])
    else:
        print("New item! Enter its details.")
        price = get_positive_float("Menu price: $")
        cost = get_positive_float("Cost to make: $")
        quantity = get_positive_int("Starting quantity: ")
        reorder = get_positive_int("Reorder level: ")
        inventory[item] = {"price": price, "cost": cost,
                           "quantity": quantity, "reorder": reorder}
        print("Added", item)

# Records a customer order, checks the input, lowers stock, and adds it to the sales list
def record_order():
    date = input("Date (YYYY-MM-DD): ").strip()
    parts = date.split("-")
    if len(parts) != 3 or not "".join(parts).isdigit():
        print("Please enter the date in the format of YYYY-MM-DD. Nothing was recorded.")
        return

    item = input("Item ordered: ").strip().lower()
    if item not in inventory:
        print("That item is not on the menu. Nothing was recorded.")
        return

    quantity = get_positive_int("Quantity ordered: ")

    if quantity > inventory[item]["quantity"]:
        print("Not enough in stock. Only", inventory[item]["quantity"], "left.")
        return

    game_day = input("Was it a game day? (yes/no): ").strip().lower()
    if game_day != "yes" and game_day != "no":
        print("Please enter yes or no. Nothing was recorded.")
        return

    inventory[item]["quantity"] -= quantity
    total = quantity * inventory[item]["price"]
    sales.append({"date": date, "item": item, "quantity": quantity,
                  "total": total, "game_day": game_day})
    print(f"Order recorded: {quantity} {item} = ${total:.2f}")