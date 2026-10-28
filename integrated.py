#Algorithm

1. Start the program.
2. Input the number of students.
3. For each student, enter the student ID, name, total fees, fees paid, attendance percentage, and internal marks.
4. Calculate the outstanding fee as total fees minus fees paid.
5. Check whether the outstanding fee is greater than zero.
6. Check whether attendance is below the minimum requirement of 75%.
7. Check whether internal marks are below the minimum requirement of 40%.
8. Record all outstanding conditions for each student.
9. If no conditions are outstanding, mark the student as eligible for the examination.
10. Otherwise, mark the student as having eligibility issues and list the reasons.
11. Repeat the process for all students.
12. Display the student-wise audit report and a summary of eligible and ineligible students.
13. Stop the program.
#Flowchart 
             ┌────────────────────┐
             │       START        │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │ Enter Number of    │
             │ Students           │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │ Enter Student      │
             │ Details            │
             │ Fee, Attendance,   │
             │ Internal Marks     │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │ Calculate          │
             │ Outstanding Fee   │
             └─────────┬──────────┘
                       │
             ┌─────────▼──────────┐
             │ Is Fee Payment     │
             │ Pending?           │
             └────┬─────────┬─────┘
                 Yes         No
                  │           │
          ┌───────▼─────┐     │
          │ Record Fee  │     │
          │ Issue       │     │
          └───────┬─────┘     │
                  └─────┬─────┘
                        │
             ┌──────────▼─────────┐
             │ Is Attendance      │
             │ Below 75%?         │
             └────┬─────────┬─────┘
                 Yes         No
                  │           │
          ┌───────▼─────┐     │
          │ Record      │     │
          │ Attendance  │     │
          │ Issue       │     │
          └───────┬─────┘     │
                  └─────┬─────┘
                        │
             ┌──────────▼─────────┐
             │ Are Internal Marks │
             │ Below 40?          │
             └────┬─────────┬─────┘
                 Yes         No
                  │           │
          ┌───────▼─────┐     │
          │ Record      │     │
          │ Marks Issue │     │
          └───────┬─────┘     │
                  └─────┬─────┘
                        │
             ┌──────────▼─────────┐
             │ Any Outstanding    │
             │ Conditions?        │
             └────┬─────────┬─────┘
                 Yes         No
                  │           │
          ┌───────▼─────┐ ┌───▼──────────┐
          │ Mark as     │ │ Mark as      │
          │ NOT ELIGIBLE│ │ ELIGIBLE     │
          └───────┬─────┘ └───┬──────────┘
                  │           │
                  └─────┬─────┘
                        │
             ┌──────────▼─────────┐
             │ More Students?     │
             └────┬─────────┬─────┘
                 Yes         No
                  │           │
                  │   ┌───────▼────────┐
                  │   │ Generate Audit │
                  │   │ Report and     │
                  │   │ Summary        │
                  │   └───────┬────────┘
                  │           │
                  │   ┌───────▼────────┐
                  │   │      STOP      │
                  │   └────────────────┘
                  │
                  └──── Repeat for
                        next student
#Code 

# Integrated University Fee and Eligibility Audit

MIN_ATTENDANCE = 75
MIN_INTERNAL_MARKS = 40

students = []
n = int(input("Enter number of students: "))

for i in range(n):
    print(f"\nEnter details for Student {i + 1}")

    student_id = input("Student ID: ")
    name = input("Student Name: ")
    total_fee = float(input("Total Fee: "))
    fee_paid = float(input("Fee Paid: "))
    attendance = float(input("Attendance Percentage: "))
    internal_marks = float(input("Internal Marks (out of 100): "))

    reasons = []

    # Fee validation
    if total_fee < 0 or fee_paid < 0 or fee_paid > total_fee:
        reasons.append("Invalid fee records")
        outstanding_fee = 0
    else:
        outstanding_fee = total_fee - fee_paid

        if outstanding_fee > 0:
            reasons.append("Fee payment pending")

    # Attendance validation
    if attendance < 0 or attendance > 100:
        reasons.append("Invalid attendance records")
    elif attendance < MIN_ATTENDANCE:
        reasons.append("Attendance below 75%")

    # Internal marks validation
    if internal_marks < 0 or internal_marks > 100:
        reasons.append("Invalid internal marks")
    elif internal_marks < MIN_INTERNAL_MARKS:
        reasons.append("Internal marks below 40")

    eligible = len(reasons) == 0

    students.append({
        "id": student_id,
        "name": name,
        "outstanding": outstanding_fee,
        "attendance": attendance,
        "internal": internal_marks,
        "eligible": eligible,
        "reasons": reasons
    })

# Generate audit report
print("\n========== UNIVERSITY AUDIT REPORT ==========")

eligible_count = 0
ineligible_count = 0

for s in students:
    print(f"\nStudent ID: {s['id']}")
    print(f"Name: {s['name']}")
    print(f"Outstanding Fee: Rs. {s['outstanding']:.2f}")
    print(f"Attendance: {s['attendance']:.1f}%")
    print(f"Internal Marks: {s['internal']:.1f}/100")

    if s["eligible"]:
        print("Status: ELIGIBLE")
        print("Reasons: None")
        eligible_count += 1
    else:
        print("Status: NOT ELIGIBLE")
        print("Outstanding Conditions:")
        for reason in s["reasons"]:
            print(f"- {reason}")
        ineligible_count += 1

print("\n=============== SUMMARY ===============")
print(f"Total Students: {n}")
print(f"Eligible Students: {eligible_count}")
print(f"Students with Issues: {ineligible_count}")
print("=======================================")

#Sample output
Enter number of students: 3

Enter details for Student 1
Student ID: 101
Student Name: Ravi
Total Fee: 50000
Fee Paid: 50000
Attendance Percentage: 85
Internal Marks (out of 100): 75

Enter details for Student 2
Student ID: 102
Student Name: Priya
Total Fee: 50000
Fee Paid: 40000
Attendance Percentage: 68
Internal Marks (out of 100): 35

Enter details for Student 3
Student ID: 103
Student Name: Arun
Total Fee: 50000
Fee Paid: 50000
Attendance Percentage: 80
Internal Marks (out of 100): 55

========== UNIVERSITY AUDIT REPORT ==========

Student ID: 101
Name: Ravi
Outstanding Fee: Rs. 0.00
Attendance: 85.0%
Internal Marks: 75.0/100
Status: ELIGIBLE
Reasons: None

Student ID: 102
Name: Priya
Outstanding Fee: Rs. 10000.00
Attendance: 68.0%
Internal Marks: 35.0/100
Status: NOT ELIGIBLE
Outstanding Conditions:
- Fee payment pending
- Attendance below 75%
- Internal marks below 40

Student ID: 103
Name: Arun
Outstanding Fee: Rs. 0.00
Attendance: 80.0%
Internal Marks: 55.0/100
Status: ELIGIBLE
Reasons: None

=============== SUMMARY ===============
Total Students: 3
Eligible Students: 2
Students with Issues: 1
=======================================
