
def form_balanced_groups(students, group_sizes):
    # Validate group sizes
    if any(size <= 0 for size in group_sizes):
        print("Error: Group sizes must be positive.")
        return

    if sum(group_sizes) != len(students):
        print("Error: Total group sizes must equal the number of students.")
        return

    # Sort students by score in descending order
    students = sorted(students, key=lambda x: x[1], reverse=True)

    # Initialize groups and their total scores
    groups = [
        {"students": [], "total": 0}
        for _ in group_sizes
    ]

    # Allocate each student to the eligible group
    # with the lowest current total score
    for student in students:
        eligible = [
            i for i in range(len(groups))
            if len(groups[i]["students"]) < group_sizes[i]
        ]

        best_group = min(
            eligible,
            key=lambda i: groups[i]["total"]
        )

        groups[best_group]["students"].append(student)
        groups[best_group]["total"] += student[1]

    # Display results
    print("\nSTUDENT GROUP FORMATION")
    print("=" * 45)

    for i, group in enumerate(groups, start=1):
        print(f"\nGroup {i}:")
        for name, score in group["students"]:
            print(f"  {name}: {score}")

        print(f"Total Score: {group['total']}")
        print(f"Average Score: {group['total'] / len(group['students']):.2f}")

    totals = [group["total"] for group in groups]
    print("\n" + "=" * 45)
    print(f"Highest Group Total: {max(totals)}")
    print(f"Lowest Group Total : {min(totals)}")
    print(f"Score Difference   : {max(totals) - min(totals)}")


# Sample student scores
students = [
    ("Asha", 95),
    ("Rahul", 88),
    ("Priya", 82),
    ("Kiran", 78),
    ("Ravi", 75),
    ("Sneha", 70),
    ("Arun", 65),
    ("Divya", 60)
]

# Create two groups of four students each
group_sizes = [4, 4]

form_balanced_groups(students, group_sizes)
