#Algorithm
1. Start the program.
2. Input the number of areas and the number of days.
3. Enter each area's name.
4. For each area, input the daily water demand and actual water supplied for every day.
5. Calculate the total demand and total supply for each area.
6. Calculate the water shortage using:
   
   Shortage = Total Demand − Total Supply
   
   If the supply exceeds demand, treat the shortage as zero.
7. Calculate the supply percentage for each area:
   
   Supply Percentage = (Total Supply / Total Demand) × 100
8. Compare supply percentages to identify differences in water distribution.
9. Identify the most underserved area as the area with the lowest supply percentage.
10. Display total demand, total supply, shortage, supply percentage, and the most underserved area.
11. Stop the program.
#Flow chart
             ┌───────────────┐
             │     START     │
             └───────┬───────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │ Input number of areas     │
       │ and number of days        │
       └─────────────┬─────────────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │ Input area name, daily    │
       │ water demand and supply   │
       └─────────────┬─────────────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │ Calculate total demand    │
       │ and total water supply    │
       └─────────────┬─────────────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │ Calculate water shortage  │
       │ and supply percentage     │
       └─────────────┬─────────────┘
                     │
                     ▼
             ◇────────────────◇
            /  Are all areas   \
           <    processed?      >
            \                  /
             ◇────────┬───────◇
                  No  │  Yes
             ┌────────┘    └────────┐
             │                     │
             ▼                     ▼
       ┌───────────────┐  ┌──────────────────────┐
       │ Input data    │  │ Compare supply       │
       │ for next area │  │ percentages          │
       └───────┬───────┘  └──────────┬───────────┘
               │                     │
               └── Return to          ▼
                   input     ┌──────────────────────┐
                             │ Identify the most    │
                             │ underserved area     │
                             └──────────┬───────────┘
                                        │
                                        ▼
                             ┌──────────────────────┐
                             │ Display distribution │
                             │ report and shortage  │
                             └──────────┬───────────┘
                                        │
                                        ▼
                                ┌───────────────┐
                                │     STOP      │
                                └───────────────┘
#Code
# Water Distribution Fairness Analysis

areas = int(input("Enter number of areas: "))
days = int(input("Enter number of days: "))

records = []

for i in range(areas):
    name = input(f"\nEnter area {i + 1} name: ")

    total_demand = 0
    total_supply = 0

    for day in range(days):
        print(f"Day {day + 1} for {name}:")
        demand = float(input("Enter water demand: "))
        supply = float(input("Enter water supplied: "))

        total_demand += demand
        total_supply += supply

    shortage = max(0, total_demand - total_supply)

    if total_demand > 0:
        percentage = (total_supply / total_demand) * 100
    else:
        percentage = 0

    records.append({
        "name": name,
        "demand": total_demand,
        "supply": total_supply,
        "shortage": shortage,
        "percentage": percentage
    })

# Display analysis report
print("\n===== WATER DISTRIBUTION REPORT =====")
print("Area\tDemand\tSupply\tShortage\tSupply %")

for area in records:
    print(
        f"{area['name']}\t"
        f"{area['demand']:g}\t"
        f"{area['supply']:g}\t"
        f"{area['shortage']:g}\t\t"
        f"{area['percentage']:.2f}%"
    )

# Identify most underserved area
underserved = min(records, key=lambda x: x["percentage"])
best_served = max(records, key=lambda x: x["percentage"])

print("\n===== FAIRNESS ANALYSIS =====")
print("Most underserved area:", underserved["name"])
print("Best served area:", best_served["name"])
print(
    "Supply percentage difference:",
    f"{best_served['percentage'] - underserved['percentage']:.2f}%"
)

#Sample output
Enter number of areas: 3
Enter number of days: 2

Enter area 1 name: Area A
Day 1 for Area A:
Enter water demand: 100
Enter water supplied: 90
Day 2 for Area A:
Enter water demand: 100
Enter water supplied: 80

Enter area 2 name: Area B
Day 1 for Area B:
Enter water demand: 100
Enter water supplied: 70
Day 2 for Area B:
Enter water demand: 100
Enter water supplied: 60

Enter area 3 name: Area C
Day 1 for Area C:
Enter water demand: 100
Enter water supplied: 95
Day 2 for Area C:
Enter water demand: 100
Enter water supplied: 90

===== WATER DISTRIBUTION REPORT =====
Area    Demand  Supply  Shortage    Supply %
Area A  200     170     30          85.00%
Area B  200     130     70          65.00%
Area C  200     185     15          92.50%

===== FAIRNESS ANALYSIS =====
Most underserved area: Area B
Best served area: Area C
Supply percentage difference: 27.50%
