import bar
import reports

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
    bar.load_inventory()
    bar.load_sales()
    running = True
    while running:
        show_menu()
        choice = input("Choose an option (1-8): ").strip()

        if choice == "1":
            bar.view_inventory()
        elif choice == "2":
            bar.record_order()
        elif choice == "3":
            bar.add_or_update_item()
        elif choice in ["4", "6"]:
            print("Coming soon")
        elif choice == "5":
            reports.show_sales_report(bar.sales)
        elif choice == "7":
            reports.show_charts(bar.sales)
        elif choice == "8":
            bar.save_inventory()
            bar.save_sales()
            print("Saved. Thank you for visiting Grizzly Tap!")
            running = False
        else:
            print("Invalid option. Please enter a number from 1 to 8.")

main()