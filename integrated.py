
# Integrated University Fee and Eligibility Audit

# University eligibility rules
MIN_ATTENDANCE = 75
MIN_INTERNAL_MARKS = 40

# Student records
students = [
    {
        "id": "S101",
        "name": "Ravi",
        "total_fee": 50000,
        "paid_fee": 50000,
        "attendance": 85,
        "internal_marks": 75,
        "documents_submitted": True
    },
    {
        "id": "S102",
        "name": "Priya",
        "total_fee": 50000,
        "paid_fee": 35000,
        "attendance": 80,
        "internal_marks": 65,
        "documents_submitted": True
    },
    {
        "id": "S103",
        "name": "Arun",
        "total_fee": 50000,
        "paid_fee": 50000,
        "attendance": 68,
        "internal_marks": 55,
        "documents_submitted": True
    },
    {
        "id": "S104",
        "name": "Sneha",
        "total_fee": 50000,
        "paid_fee": 50000,
        "attendance": 90,
        "internal_marks": 32,
        "documents_submitted": True
    },
    {
        "id": "S105",
        "name": "Kiran",
        "total_fee": 50000,
        "paid_fee": 40000,
        "attendance": 65,
        "internal_marks": 35,
        "documents_submitted": False
    }
]

reason_counts = {}
eligible_count = 0
ineligible_count = 0

print("=" * 90)
print("          INTEGRATED UNIVERSITY FEE AND ELIGIBILITY AUDIT")
print("=" * 90)

print(
    f"{'ID':<8}{'Name':<10}{'Due Fee':<12}"
    f"{'Attend %':<12}{'Marks':<10}{'Result'}"
)
print("-" * 90)

for student in students:
    reasons = []

    # Fee validation
    if student["paid_fee"] < 0 or student["total_fee"] < 0:
        reasons.append("Invalid fee record")
        due_fee = None
    else:
        due_fee = max(
            0, student["total_fee"] - student["paid_fee"]
        )
        if student["paid_fee"] < student["total_fee"]:
            reasons.append("Outstanding fee")

    # Attendance validation
    if not 0 <= student["attendance"] <= 100:
        reasons.append("Invalid attendance record")
    elif student["attendance"] < MIN_ATTENDANCE:
        reasons.append("Low attendance")

    # Internal marks validation
    if not 0 <= student["internal_marks"] <= 100:
        reasons.append("Invalid internal marks")
    elif student["internal_marks"] < MIN_INTERNAL_MARKS:
        reasons.append("Low internal marks")

    # Document validation
    if not student["documents_submitted"]:
        reasons.append("Documents pending")

    # Determine examination eligibility
    status = "ELIGIBLE" if not reasons else "NOT ELIGIBLE"

    if status == "ELIGIBLE":
        eligible_count += 1
    else:
        ineligible_count += 1

    # Count each reason
    for reason in reasons:
        reason_counts[reason] = reason_counts.get(reason, 0) + 1

    due_display = (
        f"{due_fee:.0f}" if due_fee is not None else "Invalid"
    )

    print(
        f"{student['id']:<8}{student['name']:<10}"
        f"{due_display:<12}"
        f"{student['attendance']:<12}"
        f"{student['internal_marks']:<10}"
        f"{status}"
    )

    # Print individual audit reasons
    if reasons:
        for reason in reasons:
            print(f"  -> {reason}")

# Final summary
print("\n" + "=" * 90)
print("                    AUDIT SUMMARY")
print("=" * 90)
print(f"Total Students       : {len(students)}")
print(f"Eligible Students    : {eligible_count}")
print(f"Not Eligible         : {ineligible_count}")

print("\nREASON-WISE REPORT")
print("-" * 45)

if reason_counts:
    for reason, count in sorted(reason_counts.items()):
        print(f"{reason:<25}: {count} student(s)")
else:
    print("No outstanding conditions found.")

print("=" * 90)
