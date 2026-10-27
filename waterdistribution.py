
# Water Distribution Fairness Analysis

# Water data in litres: area -> daily demand and supply
water_data = {
    "Area A": {
        "demand": [1000, 1200, 1100],
        "supply": [900, 1000, 950]
    },
    "Area B": {
        "demand": [1500, 1400, 1600],
        "supply": [1000, 1100, 1050]
    },
    "Area C": {
        "demand": [800, 900, 850],
        "supply": [750, 850, 800]
    },
    "Area D": {
        "demand": [1200, 1300, 1250],
        "supply": [600, 700, 650]
    }
}

area_summary = {}

total_demand = 0
total_supply = 0

print("=" * 85)
print("             WATER DISTRIBUTION FAIRNESS REPORT")
print("=" * 85)

print(
    f"{'Area':<12}{'Demand':<12}{'Supply':<12}"
    f"{'Shortage':<12}{'Fulfilment %':<15}{'Status'}"
)
print("-" * 85)

# Analyse each area across all days
for area, data in water_data.items():
    demand = sum(data["demand"])
    supply = sum(data["supply"])

    if len(data["demand"]) != len(data["supply"]):
        print(f"Invalid data for {area}: day counts do not match.")
        continue

    if any(x < 0 for x in data["demand"] + data["supply"]):
        print(f"Invalid data for {area}: negative values found.")
        continue

    shortage = max(0, demand - supply)
    fulfilment = (supply / demand * 100) if demand > 0 else 0

    if fulfilment < 60:
        status = "CRITICAL"
    elif fulfilment < 80:
        status = "UNDERSERVED"
    elif fulfilment < 100:
        status = "LOW"
    else:
        status = "ADEQUATE"

    area_summary[area] = {
        "demand": demand,
        "supply": supply,
        "shortage": shortage,
        "fulfilment": fulfilment
    }

    total_demand += demand
    total_supply += supply

    print(
        f"{area:<12}{demand:<12}{supply:<12}"
        f"{shortage:<12}{fulfilment:<15.2f}{status}"
    )

print("-" * 85)

# Overall distribution analysis
overall_shortage = max(0, total_demand - total_supply)
overall_fulfilment = (
    total_supply / total_demand * 100 if total_demand > 0 else 0
)

print(f"Total Demand       : {total_demand} litres")
print(f"Total Supply       : {total_supply} litres")
print(f"Total Shortage     : {overall_shortage} litres")
print(f"Overall Fulfilment : {overall_fulfilment:.2f}%")

# Identify areas with the largest shortage
if area_summary:
    most_underserved = max(
        area_summary,
        key=lambda area: area_summary[area]["shortage"]
    )

    lowest_fulfilment = min(
        area_summary,
        key=lambda area: area_summary[area]["fulfilment"]
    )

    print("\nMOST UNDERSERVED AREAS")
    print("-" * 45)
    print(
        f"Largest shortage: {most_underserved} "
        f"({area_summary[most_underserved]['shortage']} litres)"
    )
    print(
        f"Lowest fulfilment: {lowest_fulfilment} "
        f"({area_summary[lowest_fulfilment]['fulfilment']:.2f}%)"
    )

    print("\nPRIORITY RANKING (LOWEST FULFILMENT FIRST)")
    print("-" * 45)

    ranked_areas = sorted(
        area_summary.items(),
        key=lambda item: item[1]["fulfilment"]
    )

    for rank, (area, details) in enumerate(ranked_areas, start=1):
        print(
            f"{rank}. {area}: "
            f"{details['fulfilment']:.2f}% fulfilment, "
            f"{details['shortage']} litres shortage"
        )

print("=" * 85)
