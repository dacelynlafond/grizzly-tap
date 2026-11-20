import matplotlib.pyplot as plt

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