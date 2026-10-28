#Algorithm

1. Start the program.
2. Input the number of rows and columns in the seating matrix.
3. Input the seating arrangement using a nested list.
4. Input the list of valid student roll numbers.
5. Input the positions reserved for special purposes, such as staff desks or aisles.
6. Traverse each seat using nested loops.
7. Check whether each reserved position is occupied. If occupied, report an invalid allocation.
8. Check whether any non-reserved seat is empty. If empty, report an empty seat.
9. Check whether each assigned roll number belongs to the valid student list.
10. Check whether any roll number appears more than once. If repeated, report a duplicate.
11. Collect all validation errors.
12. Display the seating matrix, errors, and overall validation status.
13. Stop the program.

#Flow chart
                 ┌─────────────────────┐
             │        START        │
             └──────────┬──────────┘
                        │
             ┌──────────▼──────────┐
             │ Input Rows, Columns │
             │ and Seating Matrix  │
             └──────────┬──────────┘
                        │
             ┌──────────▼──────────┐
             │ Input Valid Roll    │
             │ Numbers and Reserved│
             │ Positions           │
             └──────────┬──────────┘
                        │
             ┌──────────▼──────────┐
             │ Traverse Matrix     │
             │ Using Nested Loops  │
             └──────────┬──────────┘
                        │
             ┌──────────▼──────────┐
             │ Is Seat Reserved?   │
             └──────┬────────┬─────┘
                   Yes       No
                    │         │
             ┌──────▼─────┐   │
             │ Is Reserved│   │
             │ Seat Empty?│   │
             └──────┬─────┘   │
                    │         │
             ┌──────▼─────┐   │
             │ Report     │   │
             │ Occupied   │   │
             │ Reserved   │   │
             │ Seat       │   │
             └──────┬─────┘   │
                    │         │
                    └────┬────┘
                         │
             ┌───────────▼─────────┐
             │ Is Non-Reserved     │
             │ Seat Empty?         │
             └──────┬────────┬─────┘
                   Yes       No
                    │         │
             ┌──────▼─────┐   │
             │ Report     │   │
             │ Empty Seat │   │
             └──────┬─────┘   │
                    │         │
                    └────┬────┘
                         │
             ┌───────────▼─────────┐
             │ Is Roll Number      │
             │ Valid?              │
             └──────┬────────┬─────┘
                   No        Yes
                    │         │
             ┌──────▼─────┐   │
             │ Report     │   │
             │ Invalid    │   │
             │ Allocation │   │
             └──────┬─────┘   │
                    │         │
                    └────┬────┘
                         │
             ┌───────────▼─────────┐
             │ Is Roll Number      │
             │ Duplicated?         │
             └──────┬────────┬─────┘
                   Yes       No
                    │         │
             ┌──────▼─────┐   │
             │ Report     │   │
             │ Duplicate  │   │
             └──────┬─────┘   │
                    │         │
                    └────┬────┘
                         │
             ┌───────────▼─────────┐
             │ More Seats to Check?│
             └──────┬────────┬─────┘
                   Yes       No
                    │         │
                    │  ┌──────▼──────────┐
                    │  │ Display Errors  │
                    │  │ and Validation  │
                    │  │ Status          │
                    │  └──────┬──────────┘
                    │         │
                    │  ┌──────▼──────────┐
                    │  │      STOP       │
                    │  └─────────────────┘
                    │
                    └── Repeat for
                        next seat
        
#Code

rows = int(input("Enter number of rows: "))
cols = int(input("Enter number of columns: "))

seating = []

print("Enter seating matrix (0 for empty seat):")
for i in range(rows):
    row = list(map(int, input().split()))
    seating.append(row)

valid_rolls = list(map(
    int, input("Enter valid roll numbers: ").split()
))

reserved_count = int(input("Enter number of reserved positions: "))
reserved = set()

for i in range(reserved_count):
    r, c = map(
        int,
        input("Enter reserved row and column: ").split()
    )
    reserved.add((r - 1, c - 1))

errors = []
seen = set()

# Validate matrix dimensions
for i in range(rows):
    if len(seating[i]) != cols:
        errors.append(f"Row {i + 1} has invalid column count")

# Validate seats
for i in range(rows):
    for j in range(cols):
        if j >= len(seating[i]):
            continue

        roll = seating[i][j]
        position = (i, j)

        if position in reserved:
            if roll != 0:
                errors.append(
                    f"Reserved seat ({i + 1},{j + 1}) is occupied"
                )
            continue

        if roll == 0:
            errors.append(
                f"Empty seat at ({i + 1},{j + 1})"
            )

        elif roll not in valid_rolls:
            errors.append(
                f"Invalid roll number {roll} at "
                f"({i + 1},{j + 1})"
            )

        if roll != 0:
            if roll in seen:
                errors.append(f"Duplicate roll number: {roll}")
            else:
                seen.add(roll)

# Display report
print("\n===== SEATING VALIDATION REPORT =====")
print("Seating Matrix:")

for row in seating:
    print(row)

if errors:
    print("\nValidation Errors:")
    for error in errors:
        print("-", error)

    print("\nStatus: INVALID SEATING ARRANGEMENT")
else:
    print("\nNo validation errors found.")
    print("Status: VALID SEATING ARRANGEMENT")

print("=====================================")

#Sample output
Enter number of rows: 2
Enter number of columns: 3
Enter seating matrix (0 for empty seat):
101 102 0
101 999 105
Enter valid roll numbers: 101 102 103 104 105
Enter number of reserved positions: 1
Enter reserved row and column: 1 3
===== SEATING VALIDATION REPORT =====
Seating Matrix:
[101, 102, 0]
[101, 999, 105]

Validation Errors:
- Duplicate roll number: 101
- Invalid roll number 999 at (2,2)

Status: INVALID SEATING ARRANGEMENT
=====================================
