#Algorithm

1. Start the program.
2. Input the number of students.
3. Enter each student's name and score.
4. Input the required number of groups and the size of each group.
5. Check whether the total group sizes equal the number of students.
6. Sort students in descending order of scores.
7. Initialize empty groups and set each group's total score to zero.
8. Assign each student to the group with the lowest current total score that has not reached its required size.
9. Update the group's score total after every allocation.
10. Display the students assigned to each group and their total scores.
11. Calculate the difference between the highest and lowest group totals.
12. Stop the program
#Flow chart
             ┌──────────────────────┐
             │        START         │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Input Student Names  │
             │ and Scores           │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Input Number of      │
             │ Groups and Group     │
             │ Sizes                │
             └──────────┬───────────┘
                        │
             ┌──────────▼───────────┐
             │ Do Group Sizes Equal │
             │ Number of Students?  │
             └──────┬────────┬──────┘
                   No        Yes
                    │         │
             ┌──────▼─────┐   │
             │ Display    │   │
             │ Invalid    │   │
             │ Group Sizes│   │
             └──────┬─────┘   │
                    │         │
                    │  ┌──────▼──────────┐
                    │  │ Sort Students   │
                    │  │ by Descending   │
                    │  │ Scores          │
                    │  └──────┬──────────┘
                    │         │
                    │  ┌──────▼──────────┐
                    │  │ Initialize Empty│
                    │  │ Groups and      │
                    │  │ Group Totals    │
                    │  └──────┬──────────┘
                    │         │
                    │  ┌──────▼──────────┐
                    │  │ Select Next     │
                    │  │ Student         │
                    │  └──────┬──────────┘
                    │         │
                    │  ┌──────▼──────────┐
                    │  │ Find Group with │
                    │  │ Lowest Total    │
                    │  │ and Available   │
                    │  │ Capacity        │
                    │  └──────┬──────────┘
                    │         │
                    │  ┌──────▼──────────┐
                    │  │ Allocate Student│
                    │  │ and Update Total│
                    │  └──────┬──────────┘
                    │         │
                    │  ┌──────▼──────────┐
                    │  │ More Students?  │
                    │  └────┬───────┬────┘
                    │      Yes       No
                    │       │         │
                    │       └───┐     │
                    │           │ ┌───▼────────────┐
                    │           │ │ Display Groups │
                    │           │ │ and Group Totals│
                    │           │ └───┬────────────┘
                    │           │     │
                    │           │ ┌───▼────────────┐
                    │           │ │ Calculate      │
                    │           │ │ Score Difference│
                    │           │ └───┬────────────┘
                    │           │     │
                    │           │ ┌───▼────────────┐
                    │           │ │      STOP      │
                    │           │ └────────────────┘
                    │           │
                    │           └── Repeat for
                    │               next student
                    │
                    └───────► STOP
#Code

n = int(input("Enter number of students: "))

students = []

for i in range(n):
    name = input(f"Enter student {i + 1} name: ")
    score = float(input(f"Enter {name}'s score: "))
    students.append((name, score))

group_count = int(input("Enter number of groups: "))

group_sizes = []
for i in range(group_count):
    size = int(input(f"Enter size of Group {i + 1}: "))
    group_sizes.append(size)

# Validate group sizes
if (any(size <= 0 for size in group_sizes)
        or sum(group_sizes) != n):
    print("Invalid group sizes! Total size must equal students.")
else:
    # Sort students by descending score
    students.sort(key=lambda student: student[1], reverse=True)

    groups = [[] for _ in range(group_count)]
    totals = [0] * group_count

    # Greedy score-balancing allocation
    for name, score in students:
        eligible_groups = [
            i for i in range(group_count)
            if len(groups[i]) < group_sizes[i]
        ]

        # Select the group with the lowest total score
        best_group = min(
            eligible_groups,
            key=lambda i: totals[i]
        )

        groups[best_group].append((name, score))
        totals[best_group] += score

    # Display group details
    print("\n===== STUDENT GROUP ALLOCATION =====")

    for i in range(group_count):
        print(f"\nGroup {i + 1}:")
        for name, score in groups[i]:
            print(f"{name} - {score:g}")

        print(f"Group Total: {totals[i]:g}")

    difference = max(totals) - min(totals)

    print("\n===== SCORE BALANCE REPORT =====")
    print(f"Highest Group Total: {max(totals):g}")
    print(f"Lowest Group Total: {min(totals):g}")
    print(f"Difference: {difference:g}")

#Sample output
Enter number of students: 8
Enter student 1 name: A
Enter A's score: 90
Enter student 2 name: B
Enter B's score: 85
Enter student 3 name: C
Enter C's score: 80
Enter student 4 name: D
Enter D's score: 75
Enter student 5 name: E
Enter E's score: 70
Enter student 6 name: F
Enter F's score: 65
Enter student 7 name: G
Enter G's score: 60
Enter student 8 name: H
Enter H's score: 55
Enter number of groups: 2
Enter size of Group 1: 4
Enter size of Group 2: 4

===== STUDENT GROUP ALLOCATION =====

Group 1:
A - 90
D - 75
E - 70
H - 55
Group Total: 290

Group 2:
B - 85
C - 80
F - 65
G - 60
Group Total: 290

===== SCORE BALANCE REPORT =====
Highest Group Total: 290
Lowest Group Total: 290
Difference: 0
