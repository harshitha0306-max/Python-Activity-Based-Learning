#Algorithm

1. Start the program.
2. Initialize the canteen menu with item names, prices, and available stock.
3. Initialize total daily sales to zero.
4. Input the number of customer orders.
5. For each customer, display the menu and enter the requested item and quantity.
6. Check whether the item exists in the menu.
7. Check whether the requested quantity is positive and available in stock.
8. If the item is unavailable or the quantity exceeds the stock, reject the order.
9. Otherwise, calculate the bill using price multiplied by quantity.
10. Deduct the ordered quantity from the available stock.
11. Add the bill amount to total daily sales.
12. Repeat the process for all customers.
13. Display the daily sales total and remaining stock for each item.
14. Stop the program
#Flow chart
             ┌──────────────────────┐
             │        START         │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Initialize Menu,     │
             │ Prices and Stock     │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Enter Number of      │
             │ Customer Orders      │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Enter Item Name and  │
             │ Required Quantity    │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Is Item Available    │
             │ in Menu?             │
             └──────┬─────────┬─────┘
                   No         Yes
                    │          │
             ┌──────▼─────┐    │
             │ Reject     │    │
             │ Order      │    │
             └──────┬─────┘    │
                    │    ┌─────▼──────────┐
                    │    │ Is Quantity    │
                    │    │ Positive?      │
                    │    └─────┬─────┬────┘
                    │         No     Yes
                    │          │      │
                    │   ┌──────▼──┐   │
                    │   │ Reject  │   │
                    │   │ Order   │   │
                    │   └──────┬──┘   │
                    │          │  ┌───▼────────────┐
                    │          │  │ Is Quantity    │
                    │          │  │ in Stock?      │
                    │          │  └───┬────────┬───┘
                    │          │     No        Yes
                    │          │      │         │
                    │          │  ┌───▼────┐ ┌──▼──────────┐
                    │          │  │ Reject │ │ Calculate   │
                    │          │  │ Order  │ │ Bill Amount│
                    │          │  └───┬────┘ └──┬──────────┘
                    │          │      │         │
                    │          │      │  ┌──────▼────────┐
                    │          │      │  │ Update Stock  │
                    │          │      │  │ and Daily     │
                    │          │      │  │ Sales         │
                    │          │      │  └──────┬────────┘
                    │          │      │         │
                    └──────────┴──────┴─────────┘
                               │
                    ┌──────────▼───────────┐
                    │ More Orders Left?    │
                    └────────┬────────┬────┘
                            Yes       No
                             │         │
                             │  ┌──────▼──────────┐
                             │  │ Display Daily   │
                             │  │ Sales and       │
                             │  │ Remaining Stock │
                             │  └──────┬──────────┘
                             │         │
                             │  ┌──────▼──────────┐
                             │  │      STOP       │
                             │  └─────────────────┘
                             │
                             └── Repeat for
                                 next order
#Code

menu = {
    "dosa": {"price": 30, "stock": 10},
    "tea": {"price": 10, "stock": 20},
    "sandwich": {"price": 50, "stock": 5},
    "samosa": {"price": 15, "stock": 8}
}

total_sales = 0
successful_orders = 0
rejected_orders = 0

print("========== CANTEEN MENU ==========")
for item, details in menu.items():
    print(f"{item.title():<12} Price: Rs.{details['price']}"
          f"  Stock: {details['stock']}")

n = int(input("\nEnter number of customer orders: "))

for i in range(n):
    print(f"\nCustomer Order {i + 1}")
    item = input("Enter item name: ").lower()
    quantity = int(input("Enter quantity: "))

    if item not in menu:
        print("Order rejected: Item not available in menu.")
        rejected_orders += 1

    elif quantity <= 0:
        print("Order rejected: Quantity must be positive.")
        rejected_orders += 1

    elif quantity > menu[item]["stock"]:
        print("Order rejected: Insufficient stock.")
        print("Available stock:", menu[item]["stock"])
        rejected_orders += 1

    else:
        price = menu[item]["price"]
        bill = price * quantity

        menu[item]["stock"] -= quantity
        total_sales += bill
        successful_orders += 1

        print("Order accepted.")
        print(f"Item: {item.title()}")
        print(f"Quantity: {quantity}")
        print(f"Bill Amount: Rs.{bill:.2f}")

print("\n========== DAILY SALES REPORT ==========")
print(f"Successful Orders: {successful_orders}")
print(f"Rejected Orders: {rejected_orders}")
print(f"Total Daily Sales: Rs.{total_sales:.2f}")

print("\nRemaining Stock:")
for item, details in menu.items():
    print(f"{item.title():<12}: {details['stock']} units")

print("========================================")

#Sample output
========== CANTEEN MENU ==========
Dosa         Price: Rs.30  Stock: 10
Tea          Price: Rs.10  Stock: 20
Sandwich     Price: Rs.50  Stock: 5
Samosa       Price: Rs.15  Stock: 8

Enter number of customer orders: 3

Customer Order 1
Enter item name: dosa
Enter quantity: 2
Order accepted.
Item: Dosa
Quantity: 2
Bill Amount: Rs.60.00

Customer Order 2
Enter item name: tea
Enter quantity: 3
Order accepted.
Item: Tea
Quantity: 3
Bill Amount: Rs.30.00

Customer Order 3
Enter item name: sandwich
Enter quantity: 6
Order rejected: Insufficient stock.
Available stock: 5

========== DAILY SALES REPORT ==========
Successful Orders: 2
Rejected Orders: 1
Total Daily Sales: Rs.90.00

Remaining Stock:
Dosa        : 8 units
Tea         : 17 units
Sandwich    : 5 units
Samosa      : 8 units
========================================
