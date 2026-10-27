
# Smart Canteen Order and Stock Management

# Initial inventory: item -> [price, available quantity]
inventory = {
    "Burger": [80, 20],
    "Pizza": [120, 15],
    "Sandwich": [50, 25],
    "Juice": [30, 30],
    "Coffee": [25, 20]
}

daily_sales = 0
total_orders = 0
successful_orders = 0
rejected_items = 0


def display_menu():
    print("\n------ CANTEEN MENU ------")
    print(f"{'Item':<12}{'Price (Rs.)':<15}{'Stock'}")
    print("-" * 35)

    for item, details in inventory.items():
        print(f"{item:<12}{details[0]:<15}{details[1]}")


def process_order(customer, orders):
    global daily_sales, total_orders
    global successful_orders, rejected_items

    total_orders += 1
    bill = 0
    valid_items = []

    print(f"\nOrder for: {customer}")
    print("-" * 40)

    # Validate the complete order before updating stock
    for item, quantity in orders.items():
        if quantity <= 0:
            print(f"Rejected: Invalid quantity for {item}")
            rejected_items += 1
        elif item not in inventory:
            print(f"Rejected: {item} is not on the menu")
            rejected_items += 1
        elif quantity > inventory[item][1]:
            print(
                f"Rejected: {item} - requested {quantity}, "
                f"available {inventory[item][1]}"
            )
            rejected_items += 1
        else:
            valid_items.append((item, quantity))

    # Process valid items
    for item, quantity in valid_items:
        price = inventory[item][0]
        amount = price * quantity

        inventory[item][1] -= quantity
        bill += amount

        print(f"{item:<12} x {quantity:<3} = Rs. {amount:.2f}")

    if bill > 0:
        successful_orders += 1
        daily_sales += bill

    print("-" * 40)
    print(f"Total Bill: Rs. {bill:.2f}")


# Display initial menu
display_menu()

# Successive customer orders
orders_list = [
    ("Customer 1", {"Burger": 2, "Juice": 3}),
    ("Customer 2", {"Pizza": 2, "Coffee": 2}),
    ("Customer 3", {"Sandwich": 4, "Juice": 40}),
    ("Customer 4", {"Burger": 25, "Coffee": 1}),
    ("Customer 5", {"Sandwich": 2, "Juice": 2})
]

for customer, orders in orders_list:
    process_order(customer, orders)

# Daily summary
print("\n" + "=" * 45)
print("          DAILY SALES SUMMARY")
print("=" * 45)
print(f"Total Orders       : {total_orders}")
print(f"Orders with Sales  : {successful_orders}")
print(f"Rejected Items     : {rejected_items}")
print(f"Total Daily Sales  : Rs. {daily_sales:.2f}")

print("\nREMAINING INVENTORY")
print("-" * 35)
print(f"{'Item':<12}{'Price':<10}{'Stock'}")

for item, details in inventory.items():
    print(f"{item:<12}{details[0]:<10}{details[1]}")

print("=" * 45)
