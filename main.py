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
        elif choice == "7":
            print("Thank you for visiting Grizzly Tap!")
            running = False
        elif choice in ["1", "2", "3", "4", "5", "6"]:
            print("Coming soon")
        else:
            print("Invalid option. Please enter a number from 1 to 7.")


main()