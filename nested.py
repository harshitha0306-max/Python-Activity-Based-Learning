
# Nested List Examination Seating Validation

# Seating matrix: None represents an empty seat
seating_matrix = [
    [101, 102, 103, None],
    [104, 105, 101, 106],
    [107, -1, 108, 109],
    [110, 111, None, 112]
]

# -1 represents a reserved position
reserved_positions = [(2, 1)]

# Valid roll numbers
valid_roll_numbers = set(range(101, 113))

seen_roll_numbers = set()
duplicates = []
empty_seats = []
invalid_allocations = []
reserved_violations = []

rows = len(seating_matrix)
cols = len(seating_matrix[0]) if rows > 0 else 0

# Validate matrix dimensions
if any(len(row) != cols for row in seating_matrix):
    print("Error: Seating matrix must be rectangular.")
else:
    for i in range(rows):
        for j in range(cols):
            roll = seating_matrix[i][j]
            position = (i, j)

            # Check reserved positions
            if position in reserved_positions:
                if roll != -1:
                    reserved_violations.append((position, roll))
                continue

            # Check empty seats
            if roll is None:
                empty_seats.append(position)
                continue

            # Check invalid allocations
            if not isinstance(roll, int) or roll not in valid_roll_numbers:
                invalid_allocations.append((position, roll))
                continue

            # Check duplicate roll numbers
            if roll in seen_roll_numbers:
                duplicates.append((position, roll))
            else:
                seen_roll_numbers.add(roll)

    # Display seating matrix
    print("\nEXAMINATION SEATING MATRIX")
    print("=" * 45)

    for row in seating_matrix:
        print(row)

    print("\nVALIDATION REPORT")
    print("=" * 45)

    print("\n1. Duplicate Roll Numbers:")
    print(duplicates if duplicates else "None")

    print("\n2. Reserved Position Violations:")
    print(reserved_violations if reserved_violations else "None")

    print("\n3. Empty Seats:")
    print(empty_seats if empty_seats else "None")

    print("\n4. Invalid Student Allocations:")
    print(invalid_allocations if invalid_allocations else "None")

    print("\n5. Final Status:")
    if not any([
        duplicates,
        reserved_violations,
        empty_seats,
        invalid_allocations
    ]):
        print("Seating matrix is VALID.")
    else:
        print("Seating matrix is INVALID. Please correct the issues.")

    print("=" * 45)
