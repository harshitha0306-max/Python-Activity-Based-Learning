#Algorithm

1. Start the program.
2. Input the user's monthly call usage, data usage, required validity, and budget.
3. Input the number of mobile plans to compare.
4. For each plan, enter its name, price, included call minutes, included data, validity, and excess usage charges.
5. Calculate excess call charges if call usage exceeds the included minutes.
6. Calculate excess data charges if data usage exceeds the included data allowance.
7. Calculate the total cost of each plan, including excess charges.
8. Check whether the plan meets the required validity and budget.
9. Mark the plan as eligible if it satisfies both conditions; otherwise, mark it as ineligible.
10. Compare the total costs of all eligible plans.
11. Identify the eligible plan with the lowest total cost.
12. Display the cost comparison, excess charges, eligibility status, and most economical plan.
13. Stop the program

#Flow chart
             ┌──────────────────────┐
             │        START         │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Enter Usage, Budget  │
             │ and Required Validity│
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Enter Number of      │
             │ Mobile Plans         │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Enter Plan Details   │
             │ Price, Calls, Data   │
             │ and Validity         │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Calculate Excess     │
             │ Call and Data Charges│
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Calculate Total Cost │
             │ of the Plan          │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Does Plan Meet Budget│
             │ and Validity Limits? │
             └──────┬────────┬──────┘
                   Yes       No
                    │         │
          ┌─────────▼────┐ ┌──▼───────────┐
          │ Mark Plan as │ │ Mark Plan as │
          │ Eligible     │ │ Ineligible   │
          └─────────┬────┘ └──┬───────────┘
                    │         │
                    └────┬────┘
                         │
             ┌───────────▼──────────┐
             │ Are More Plans Left? │
             └──────┬─────────┬─────┘
                   Yes        No
                    │          │
                    │  ┌───────▼─────────┐
                    │  │ Compare Costs   │
                    │  │ of Eligible     │
                    │  │ Plans           │
                    │  └───────┬─────────┘
                    │          │
                    │  ┌───────▼─────────┐
                    │  │ Identify Lowest │
                    │  │ Cost Plan       │
                    │  └───────┬─────────┘
                    │          │
                    │  ┌───────▼─────────┐
                    │  │ Display Plan    │
                    │  │ Comparison and  │
                    │  │ Best Plan       │
                    │  └───────┬─────────┘
                    │          │
                    │  ┌───────▼─────────┐
                    │  │      STOP       │
                    │  └─────────────────┘
                    │
                    └── Repeat for
                        next plan

#Code

call_usage = float(input("Enter required call minutes: "))
data_usage = float(input("Enter required data usage (GB): "))
required_validity = int(input("Enter required validity (days): "))
budget = float(input("Enter maximum budget (Rs.): "))

n = int(input("Enter number of plans to compare: "))

plans = []

for i in range(n):
    print(f"\nEnter details for Plan {i + 1}")

    name = input("Plan name: ")
    price = float(input("Plan price (Rs.): "))
    included_calls = float(input("Included call minutes: "))
    included_data = float(input("Included data (GB): "))
    validity = int(input("Validity (days): "))
    call_rate = float(input("Excess call charge per minute (Rs.): "))
    data_rate = float(input("Excess data charge per GB (Rs.): "))

    excess_calls = max(0, call_usage - included_calls)
    excess_data = max(0, data_usage - included_data)

    call_charge = excess_calls * call_rate
    data_charge = excess_data * data_rate
    total_cost = price + call_charge + data_charge

    eligible = (
        validity >= required_validity
        and total_cost <= budget
    )

    plans.append({
        "name": name,
        "price": price,
        "call_charge": call_charge,
        "data_charge": data_charge,
        "total_cost": total_cost,
        "validity": validity,
        "eligible": eligible
    })

print("\n========== PLAN COMPARISON ==========")
print(f"{'Plan':<12}{'Base':>8}{'Excess':>10}"
      f"{'Total':>10}{'Status':>14}")

for p in plans:
    excess = p["call_charge"] + p["data_charge"]
    status = "Eligible" if p["eligible"] else "Ineligible"

    print(f"{p['name']:<12}{p['price']:>8.2f}"
          f"{excess:>10.2f}{p['total_cost']:>10.2f}"
          f"{status:>14}")

eligible_plans = [p for p in plans if p["eligible"]]

print("\n========== FINAL RESULT ==========")

if eligible_plans:
    best = min(eligible_plans, key=lambda p: p["total_cost"])
    print(f"Most economical plan: {best['name']}")
    print(f"Total cost: Rs. {best['total_cost']:.2f}")
    print(f"Validity: {best['validity']} days")
else:
    print("No plan satisfies the budget and validity requirements.")

print("==================================")

#Sample output
Enter required call minutes: 500
Enter required data usage (GB): 2
Enter required validity (days): 28
Enter maximum budget (Rs.): 300
Enter number of plans to compare: 3

Enter details for Plan 1
Plan name: Basic
Plan price (Rs.): 199
Included call minutes: 300
Included data (GB): 1.5
Validity (days): 28
Excess call charge per minute (Rs.): 0.5
Excess data charge per GB (Rs.): 20

Enter details for Plan 2
Plan name: Smart
Plan price (Rs.): 249
Included call minutes: 500
Included data (GB): 2
Validity (days): 28
Excess call charge per minute (Rs.): 0.5
Excess data charge per GB (Rs.): 20

Enter details for Plan 3
Plan name: Value
Plan price (Rs.): 279
Included call minutes: 1000
Included data (GB): 3
Validity (days): 56
Excess call charge per minute (Rs.): 0.5
Excess data charge per GB (Rs.): 20

========== PLAN COMPARISON ==========
Plan            Base    Excess     Total        Status
Basic         199.00    110.00    309.00    Ineligible
Smart         249.00      0.00    249.00      Eligible
Value         279.00      0.00    279.00      Eligible

========== FINAL RESULT ==========
Most economical plan: Smart
Total cost: Rs. 249.00
Validity: 28 days
==================================
