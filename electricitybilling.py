
def calculate_bill(units):
    # Progressive electricity slab rates
    if units <= 100:
        energy_charge = units * 1.50
    elif units <= 200:
        energy_charge = 100 * 1.50 + (units - 100) * 2.50
    elif units <= 300:
        energy_charge = 100 * 1.50 + 100 * 2.50 + (units - 200) * 4.00
    else:
        energy_charge = (
            100 * 1.50
            + 100 * 2.50
            + 100 * 4.00
            + (units - 300) * 6.00
        )

    fixed_charge = 100
    surcharge = energy_charge * 0.05

    # Rebate for consumption up to 100 units
    rebate = 50 if units <= 100 else 0

    total_bill = (
        energy_charge + fixed_charge + surcharge - rebate
    )

    return round(total_bill, 2)


# Monthly electricity consumption
months = ["January", "February", "March", "April", "May"]
consumption = [80, 120, 180, 250, 400]

bills = []

print("MONTHLY ELECTRICITY BILL")
print("-" * 55)
print(f"{'Month':<12}{'Units':<10}{'Bill (Rs.)':<15}{'Change (%)'}")
print("-" * 55)

for i in range(len(months)):
    bill = calculate_bill(consumption[i])
    bills.append(bill)

    if i == 0:
        change = 0
        change_text = "N/A"
    else:
        change = (
            (bill - bills[i - 1]) / bills[i - 1]
        ) * 100
        change_text = f"{change:.2f}%"

    print(
        f"{months[i]:<12}{consumption[i]:<10}"
        f"{bill:<15.2f}{change_text}"
    )

    # Identify unusual increases above 30%
    if i > 0 and change > 30:
        print("  WARNING: Unusual bill increase detected!")

print("-" * 55)
print(f"Total electricity cost: Rs. {sum(bills):.2f}")
print(f"Average monthly bill: Rs. {sum(bills) / len(bills):.2f}")

highest_index = bills.index(max(bills))
print(f"Highest bill: {months[highest_index]} - Rs. {bills[highest_index]:.2f}")
