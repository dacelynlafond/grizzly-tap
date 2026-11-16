import csv

inventory_file = "inventory.csv" #new way to view inventory
SALES_FILE = "sales.csv" #new way to view sales

inventory = {}
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


# Asks for a whole number greater than 0; returns None if the input is invalid
def get_positive_int(prompt):
    text = input(prompt).strip()
    if text.isdigit() and int(text) > 0:
        return int(text)
    print("Please enter a whole number greater than 0 (no letters).")
    return None

# Restocks an existing item, or asks for details and adds a new item
def add_or_update_item():
    item = input("Item name: ").strip().lower()

        
# Prints all menu options for Grizzly Tap
def show_menu():
    print("\n==== Grizzly Tap Menu ====")
    print("1. View Inventory")
    print("2. Record Customer Order")
    print("3. Add/Restock Item")
    print("4. Show Low Stock Alerts")
    print("5. Weekly Sales Report")
    print("6. Run 30-day Simulation")
    print("7. Exit")


# Runs the main loop until the user chooses Exit
def main():
    running = True
    while running:
        show_menu()
        choice = input("Choose an option (1-7): ").strip()

        if choice == "1":
            view_inventory()
        elif choice == "3":
            add_or_update_item()
        elif choice == "7":
            print("Thank you for visiting Grizzly Tap!")
            running = False
        elif choice in ["2", "4", "5", "6"]:
            print("Coming soon")
        else:
            print("Invalid option. Please enter a number from 1 to 7.")


main()