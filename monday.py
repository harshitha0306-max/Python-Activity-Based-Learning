
'''# Multi-Plan Telecommunications Cost Optimization

plans = [
    {
        "name": "Basic Plan",
        "price": 199,
        "data": 2,
        "calls": 100,
        "sms": 100,
        "validity": 28,
        "extra_data": 50,   # Cost per extra GB
        "extra_call": 0.50, # Cost per extra minute
        "extra_sms": 0.25
    },
    {
        "name": "Standard Plan",
        "price": 299,
        "data": 3,
        "calls": 300,
        "sms": 100,
        "validity": 28,
        "extra_data": 40,
        "extra_call": 0.40,
        "extra_sms": 0.20
    },
    {
        "name": "Premium Plan",
        "price": 399,
        "data": 5,
        "calls": 500,
        "sms": 200,
        "validity": 56,
        "extra_data": 30,
        "extra_call": 0.30,
        "extra_sms": 0.15
    }
]

# User requirements
data_usage = float(input("Enter required data usage (GB): "))
call_minutes = int(input("Enter required call minutes: "))
sms_count = int(input("Enter required SMS count: "))
required_validity = int(input("Enter required validity (days): "))
budget = float(input("Enter your budget (Rs.): "))

results = []

for plan in plans:
    # Calculate excess usage
    extra_data = max(0, data_usage - plan["data"])
    extra_calls = max(0, call_minutes - plan["calls"])
    extra_sms = max(0, sms_count - plan["sms"])

    excess_cost = (
        extra_data * plan["extra_data"]
        + extra_calls * plan["extra_call"]
        + extra_sms * plan["extra_sms"]
    )

    total_cost = plan["price"] + excess_cost

    # Check validity and budget constraints
    eligible = (
        plan["validity"] >= required_validity
        and total_cost <= budget
    )

    results.append({
        "name": plan["name"],
        "base": plan["price"],
        "excess": excess_cost,
        "total": total_cost,
        "eligible": eligible
    })

# Display comparison
print("\n--- Mobile Plan Comparison ---")
print(f"{'Plan':<16}{'Base (Rs.)':>12}"
      f"{'Excess (Rs.)':>15}{'Total (Rs.)':>13}"
      f"{'Eligible':>12}")

for result in results:
    status = "Yes" if result["eligible"] else "No"
    print(f"{result['name']:<16}"
          f"{result['base']:>12.2f}"
          f"{result['excess']:>15.2f}"
          f"{result['total']:>13.2f}"
          f"{status:>12}")

# Find the most economical eligible plan
eligible_plans = [
    result for result in results if result["eligible"]
]

if eligible_plans:
    best = min(eligible_plans, key=lambda x: x["total"])
    print("\nMost economical eligible plan:", best["name"])
    print(f"Total cost: Rs. {best['total']:.2f}")
    print(f"Excess charges: Rs. {best['excess']:.2f}")
else:
    print("\nNo plan satisfies all the constraints.")


