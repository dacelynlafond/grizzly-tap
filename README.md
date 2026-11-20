# Grizzly Tap

## Business Problem
Grizzly Tap is a sports bar near campus. On big game days it needs more food
and staff than on a normal night, but planning is done by guesswork. This app
keeps inventory and order records in one place so the manager can plan.

## Business Question
How much food and staff do we need on a game day compared to a normal night?

## How to Run
1. Open the project folder in VS Code
2. Run `main.py`
3. Choose an option from the menu

## Menu Options
1. View Inventory
2. Record Customer Order
3. Add/Restock Item
4. Show Low Stock Alerts (coming soon)
5. Weekly Sales Report (coming soon)
6. Run 30-day Simulation
7. Show Charts
8. Save and Exit

## Files
- `main.py` - runs the menu
- `inventory.csv` - menu items, prices, costs, stock, and reorder levels
- `sales.csv` - customer orders that have been recorded
- `employees.csv` - employee data
- `units_by_item.png` - units sold by item chart
-`revenue_by_day.png` - revenue by day chart

## Charts

[Units sold by item](units_by_item.png)

Beer is the most sold item and should be reordered most frequently.

[Revenue by day](revenue_by_day.png)

Saturdays have the most revenue making it the busiest day, so the bar should be staffed more on Saturdays.

## Author
Dacelyn LaFond