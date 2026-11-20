import csv
import matplotlib.pyplot as plt

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

# Adds up the quantity sold for each item and returns a dictionary
def units_by_item(sales_list):
    totals = {}
    for sale in sales_list:
        item = sale["item"]
        if item in totals:
            totals[item] += sale["quantity"]
        else:
            totals[item] = sale["quantity"]
    return totals

# Adds up the revenue for each date and returns a dictionary
def revenue_by_day(sales_list):
    totals = {}
    for sale in sales_list:
        date = sale["date"]
        if date in totals:
            totals[date] += sale["total"]
        else:
            totals[date] = sale["total"]
    return totals

def show_charts(sales_list):
    if len(sales_list) == 0:
        print("No sales recorded yet. Nothing to chart.")
        return

    # Chart 1: bar chart of units sold by item
    units = units_by_item(sales_list)
    item_names = list(units.keys())
    item_units = list(units.values())

    plt.bar(item_names, item_units)
    plt.title("Units Sold by Item")
    plt.xlabel("Item")
    plt.ylabel("Units Sold")
    plt.savefig("units_by_item.png")
    plt.show()
    plt.close()

    # Chart 2: line chart of revenue by day
    daily = revenue_by_day(sales_list)
    dates = sorted(daily.keys())
    daily_revenue = []
    for date in dates:
        daily_revenue.append(daily[date])

    plt.plot(dates, daily_revenue, marker="o")
    plt.title("Revenue by Day")
    plt.xlabel("Date")
    plt.ylabel("Revenue ($)")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig("revenue_by_day.png")
    plt.show()
    plt.close()

    print("Charts saved: units_by_item.png and revenue_by_day.png")

# Prints a summary of all recorded sales
def show_sales_report(sales_list):
    if len(sales_list) == 0:
        print("No sales recorded yet. Record some orders first.")
        return

    # Total revenue, game day revenue, and normal day revenue
    total_revenue = 0
    game_revenue = 0
    normal_revenue = 0
    for sale in sales_list:
        total_revenue += sale["total"]
        if sale["game_day"] == "yes":
            game_revenue += sale["total"]
        else:
            normal_revenue += sale["total"]

    order_count = len(sales_list)
    average_order = total_revenue / order_count

    # Find the top seller
    units = units_by_item(sales_list)
    top_item = ""
    top_units = 0
    for item in units:
        if units[item] > top_units:
            top_item = item
            top_units = units[item]

    print("\n--- Grizzly Tap Sales Report ---")
    print(f"Orders recorded:   {order_count}")
    print(f"Total revenue:     ${total_revenue:.2f}")
    print(f"Average per order: ${average_order:.2f}")
    print(f"Top seller:        {top_item} ({top_units} sold)")
    print(f"Game day revenue:  ${game_revenue:.2f}")
    print(f"Normal day revenue: ${normal_revenue:.2f}")

    print("\nUnits sold by item:")
    for item in units:
        print(f"   {item}: {units[item]}")

# Prints all menu options for Grizzly Tap
def show_menu():
    print("\n==== Grizzly Tap Menu ====")
    print("1. View Inventory")
    print("2. Record Customer Order")
    print("3. Add/Restock Item")
    print("4. Show Low Stock Alerts")
    print("5. Sales Report")
    print("6. Run 30-day Simulation")
    print("7. Show Charts")
    print("8. Save and Exit")

# Runs the main loop until the user chooses Exit
def main():
    load_inventory()
    load_sales()
    running = True
    while running:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            view_inventory()
        elif choice == "2":
            record_order()
        elif choice == "3":
            add_or_update_item()
        elif choice in ["4", "6"]:
            print("Coming soon")
        elif choice == "5":
            show_sales_report(sales)
        elif choice == "7":
            show_charts(sales)
        elif choice == "8":
            save_inventory()
            save_sales()
            print("Saved. Thank you for visiting Grizzly Tap!")
            running = False
        else:
            print("Invalid option. Please enter a number from 1 to 8.")

main()