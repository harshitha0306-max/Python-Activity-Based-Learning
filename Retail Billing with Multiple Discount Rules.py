# Retail Billing with Multiple Discount Rules

# Category-specific tax rates
tax_rates = {
    "electronics": 18,
    "clothing": 5,
    "food": 0,
    "grocery": 5
}

# Discount rules
discount_threshold = 2000
discount_rate = 10
max_discount = 500

items = []
subtotal = 0
total_tax = 0

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i + 1}")

    name = input("Enter product name: ")
    category = input(
        "Enter category (electronics/clothing/food/grocery): "
    ).lower()
    price = float(input("Enter unit price (Rs.): "))
    quantity = int(input("Enter quantity: "))

    if price < 0 or quantity <= 0:
        print("Invalid price or quantity. Try again.")
        continue

    if category not in tax_rates:
        print("Invalid category. Product skipped.")
        continue

    # Calculate item amount and tax
    amount = price * quantity
    tax = amount * tax_rates[category] / 100

    items.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "amount": amount,
        "tax_rate": tax_rates[category],
        "tax": tax
    })

    subtotal += amount
    total_tax += tax

# Calculate threshold discount
discount = 0

if subtotal >= discount_threshold:
    discount = subtotal * discount_rate / 100
    discount = min(discount, max_discount)

# Calculate final bill
final_total = subtotal - discount + total_tax

# Generate itemized invoice
print("\n" + "=" * 76)
print("                    RETAIL STORE INVOICE")
print("=" * 76)

print(f"{'Product':<16}{'Category':<14}{'Price':>9}"
      f"{'Qty':>5}{'Amount':>10}{'Tax':>7}{'Tax Amt':>10}")
print("-" * 76)

for item in items:
    print(f"{item['name']:<16}"
          f"{item['category']:<14}"
          f"{item['price']:>9.2f}"
          f"{item['quantity']:>5}"
          f"{item['amount']:>10.2f}"
          f"{item['tax_rate']:>6}%"
          f"{item['tax']:>10.2f}")

print("-" * 76)
print(f"{'Subtotal:':<55} Rs. {subtotal:>10.2f}")
print(f"{'Discount:':<55} Rs. {discount:>10.2f}")
print(f"{'Total Tax:':<55} Rs. {total_tax:>10.2f}")
print("=" * 76)
print(f"{'FINAL AMOUNT:':<55} Rs. {final_total:>10.2f}")
print("=" * 76)

if discount > 0:
    print(f"You saved Rs. {discount:.2f}!")
else:
    remaining = max(0, discount_threshold - subtotal)
    print(f"Spend Rs. {remaining:.2f} more to qualify for a discount.")
