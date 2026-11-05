# Main data: each menu item with its price, cost, quantity on hand, and reorder level
inventory = {
    "wings": {"price": 12.50, "cost": 5.00, "quantity": 100, "reorder": 30},
    "nachos": {"price": 9.00, "cost": 3.00, "quantity": 55, "reorder": 15},
    "burgers": {"price": 14.00, "cost": 6.00, "quantity": 40, "reorder": 10},
    "soda": {"price": 3.00, "cost": 0.75, "quantity": 80, "reorder": 20}
}
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

    try:
        if item in inventory:
            amount = int(input("How many to add? "))
            inventory[item]["quantity"] += amount
            print("Restocked.", item, "now has", inventory[item]["quantity"])
        else:
            print("New item! Enter its details.")
            price = float(input("Menu price: $"))
            cost = float(input("Cost to make: $"))
            quantity = int(input("Starting quantity: "))
            reorder = int(input("Reorder level: "))
            inventory[item] = {"price": price, "cost": cost,
                               "quantity": quantity, "reorder": reorder}
            print("Added", item)
    except ValueError:
        print("Please enter numbers only. Nothing was changed.")
        
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