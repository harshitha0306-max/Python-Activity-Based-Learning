#Algorithm

1. Start the program.
2. Read the number of products.
3. For each product, input its name, category, price, and quantity.
4. Calculate the subtotal for each product using price × quantity.
5. Calculate tax based on the product category.
6. Add all product subtotals to obtain the total subtotal.
7. Calculate the discount based on the bill amount and discount thresholds.
8. Apply the maximum concession limit to the discount.
9. Calculate the final bill by adding taxes and subtracting the discount.
10. Display the itemized invoice, including product details, taxes, discount, and final amount.
11. Stop the program.

#flow chart
          ┌──────────────────┐
          │      START       │
          └────────┬─────────┘
                   │
          ┌────────▼─────────┐
          │ Enter Number of  │
          │ Months           │
          └────────┬─────────┘
                   │
          ┌────────▼─────────┐
          │ Enter Month and  │
          │ Units Consumed   │
          └────────┬─────────┘
                   │
          ┌────────▼─────────┐
          │ Calculate Energy │
          │ Charges by Slabs │
          └────────┬─────────┘
                   │
          ┌────────▼─────────┐
          │ Add Fixed Charges│
          └────────┬─────────┘
                   │
          ┌────────▼─────────┐
          │ Calculate        │
          │ Surcharge        │
          └────────┬─────────┘
                   │
          ┌────────▼─────────┐
          │ Check Rebate     │
          │ Eligibility      │
          └────────┬─────────┘
                   │
          ┌────────▼─────────┐
          │ Calculate Final  │
          │ Electricity Bill │
          └────────┬─────────┘
                   │
          ┌────────▼─────────┐
          │ Are More Months  │
          │ Remaining?       │
          └────┬────────┬────┘
               │        │
             YES        NO
               │        │
        ┌──────▼────┐   │
        │ Enter Next│   │
        │ Month     │   │
        └──────┬────┘   │
               │        │
               └───↺    ▼
                 ┌─────────────────┐
                 │ Compare Monthly │
                 │ Bills           │
                 └────────┬────────┘
                          │
                 ┌────────▼────────┐
                 │ Is Increase     │
                 │ More Than 20%?  │
                 └────┬────────┬───┘
                      │        │
                     YES       NO
                      │        │
             ┌────────▼───┐ ┌──▼────────────┐
             │ Mark as    │ │ Normal Bill   │
             │ Unusual    │ │ Change        │
             └──────┬─────┘ └──────┬────────┘
                    │              │
                    └──────┬───────┘
                           │
                  ┌────────▼────────┐
                  │ Display Monthly │
                  │ Bills and Report│
                  └────────┬────────┘
                           │
                  ┌────────▼────────┐
                  │      STOP       │
                  └─────────────────┘
#code

tax_rates = {
    "electronics": 18,
    "clothing": 12,
    "groceries": 5,
    "other": 10
}

products = []
total_subtotal = 0
total_tax = 0

n = int(input("Enter number of products: "))

for i in range(n):
    print(f"\nProduct {i + 1}")

    name = input("Enter product name: ")
    category = input("Enter category (electronics/clothing/groceries/other): ").lower()
    price = float(input("Enter unit price: "))
    quantity = int(input("Enter quantity: "))

    if category not in tax_rates:
        print("Invalid category! Using 10% tax.")
        category = "other"

    subtotal = price * quantity
    tax = subtotal * tax_rates[category] / 100

    products.append({
        "name": name,
        "category": category,
        "price": price,
        "quantity": quantity,
        "subtotal": subtotal,
        "tax": tax
    })

    total_subtotal += subtotal
    total_tax += tax

# Apply threshold discount
if total_subtotal >= 5000:
    discount = total_subtotal * 0.10
elif total_subtotal >= 2000:
    discount = total_subtotal * 0.05
else:
    discount = 0

# Apply maximum concession limit
discount = min(discount, 1000)

final_amount = total_subtotal + total_tax - discount

# Print itemized invoice
print("\n========== RETAIL INVOICE ==========")
print(f"{'Product':<15}{'Qty':>5}{'Subtotal':>12}{'Tax':>10}")

for p in products:
    print(f"{p['name']:<15}{p['quantity']:>5}"
          f"{p['subtotal']:>12.2f}{p['tax']:>10.2f}")

print("------------------------------------")
print(f"Subtotal       : Rs. {total_subtotal:.2f}")
print(f"Total Tax      : Rs. {total_tax:.2f}")
print(f"Discount       : Rs. {discount:.2f}")
print(f"Final Amount   : Rs. {final_amount:.2f}")
print("====================================")

#sample output
Enter number of products: 3

Product 1
Enter product name: Laptop
Enter category (electronics/clothing/groceries/other): electronics
Enter unit price: 50000
Enter quantity: 1

Product 2
Enter product name: Shirt
Enter category (electronics/clothing/groceries/other): clothing
Enter unit price: 1000
Enter quantity: 2

Product 3
Enter product name: Rice
Enter category (electronics/clothing/groceries/other): groceries
Enter unit price: 200
Enter quantity: 5
