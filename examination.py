#Algorithm

1. Start the program.
2. Input the student's name and number of subjects.
3. For each subject, input the subject name, marks obtained, and maximum marks.
4. Check whether the marks entered are valid.
5. Check whether the student has passed each subject using the minimum pass marks.
6. If the student fails a subject by a small margin, apply grace marks according to the specified policy.
7. Ensure that grace marks do not exceed the maximum marks or the allowed grace limit.
8. Recheck the subject result after applying grace marks.
9. Calculate the total marks, maximum total, and percentage.
10. Determine the final result: Pass if all subjects are passed; otherwise, Fail.
11. If the student passes, assign a classification:
    - 75% and above: Distinction
    - 60% to below 75%: First Class
    - 50% to below 60%: Second Class
    - Below 50%: Pass Class
12. Display subject-wise marks, grace marks awarded, final results, percentage, and classification.
13. Stop the program

#flow chart
             ┌───────────────────┐
             │       START       │
             └─────────┬─────────┘
                       │
             ┌─────────▼─────────┐
             │ Input Student     │
             │ Name and Subjects │
             └─────────┬─────────┘
                       │
             ┌─────────▼─────────┐
             │ Enter Subject     │
             │ Name and Marks    │
             └─────────┬─────────┘
                       │
             ┌─────────▼─────────┐
             │ Are Marks Valid?  │
             └────┬────────┬─────┘
                 No        Yes
                  │         │
          ┌───────▼────┐    │
          │ Re-enter   │    │
          │ Valid Marks│    │
          └───────┬────┘    │
                  │         │
                  └────┬────┘
                       │
             ┌─────────▼─────────┐
             │ Calculate Pass    │
             │ Marks             │
             └─────────┬─────────┘
                       │
             ┌─────────▼─────────┐
             │ Marks Below Pass  │
             │ Marks?            │
             └────┬────────┬─────┘
                 Yes        No
                  │          │
          ┌───────▼──────┐   │
          │ Shortage <= 5?│  │
          └────┬─────┬───┘   │
              Yes    No      │
               │      │      │
       ┌───────▼──┐   │      │
       │ Award     │   │      │
       │ Grace     │   │      │
       │ Marks     │   │      │
       └───────┬───┘   │      │
               │       │      │
               └───┬───┴──────┘
                   │
          ┌────────▼──────────┐
          │ Recheck Subject   │
          │ Pass or Fail      │
          └────────┬──────────┘
                   │
          ┌────────▼──────────┐
          │ More Subjects?    │
          └────┬─────────┬────┘
              Yes         No
               │           │
               │  ┌────────▼────────┐
               │  │ Calculate Total │
               │  │ and Percentage  │
               │  └────────┬────────┘
               │           │
               │  ┌────────▼────────┐
               │  │ Determine Final │
               │  │ Result and      │
               │  │ Classification  │
               │  └────────┬────────┘
               │           │
               │  ┌────────▼────────┐
               │  │ Display Result  │
               │  │ and Grace Marks │
               │  └────────┬────────┘
               │           │
               │  ┌────────▼────────┐
               │  │      STOP       │
               │  └─────────────────┘
               │
               └──── Repeat for
                     next subject
#code

# Examination Result and Grace-Mark Validation

student = input("Enter student name: ")
n = int(input("Enter number of subjects: "))

pass_percentage = 35
grace_limit = 5

total_marks = 0
total_maximum = 0
all_passed = True
results = []

for i in range(n):
    print(f"\nSubject {i + 1}")
    subject = input("Enter subject name: ")
    maximum = float(input("Enter maximum marks: "))
    marks = float(input("Enter marks obtained: "))

    if maximum <= 0 or marks < 0 or marks > maximum:
        print("Invalid marks! Enter valid data.")
        continue

    pass_marks = maximum * pass_percentage / 100
    grace = 0

    if marks < pass_marks:
        shortage = pass_marks - marks

        if shortage <= grace_limit:
            grace = shortage
            marks = min(marks + grace, maximum)

    passed = marks >= pass_marks

    if not passed:
        all_passed = False

    results.append(
        (subject, marks, maximum, grace,
         "Pass" if passed else "Fail")
    )

    total_marks += marks
    total_maximum += maximum

print("\n========== EXAMINATION RESULT ==========")
print(f"Student: {student}")
print(f"{'Subject':<15}{'Marks':>10}{'Grace':>10}{'Result':>10}")

for subject, marks, maximum, grace, status in results:
    print(f"{subject:<15}{marks:>10.2f}"
          f"{grace:>10.2f}{status:>10}")

if total_maximum > 0:
    percentage = total_marks / total_maximum * 100

    print("----------------------------------------")
    print(f"Total Marks: {total_marks:.2f}/{total_maximum:.2f}")
    print(f"Percentage: {percentage:.2f}%")

    if not all_passed:
        classification = "Fail"
    elif percentage >= 75:
        classification = "Distinction"
    elif percentage >= 60:
        classification = "First Class"
    elif percentage >= 50:
        classification = "Second Class"
    else:
        classification = "Pass Class"

    print(f"Final Result: {'Pass' if all_passed else 'Fail'}")
    print(f"Classification: {classification}")
else:
    print("No valid subject marks were entered.")

print("========================================")

#sample output
Enter student name: Rahul
Enter number of subjects: 3

Subject 1
Enter subject name: Maths
Enter maximum marks: 100
Enter marks obtained: 32

Subject 2
Enter subject name: English
Enter maximum marks: 100
Enter marks obtained: 68

Subject 3
Enter subject name: Science
Enter maximum marks: 100
Enter marks obtained: 80

========== EXAMINATION RESULT ==========
Student: Rahul
Subject             Marks     Grace    Result
Maths               35.00      3.00      Pass
English             68.00      0.00      Pass
Science             80.00      0.00      Pass
----------------------------------------
Total Marks: 183.00/300.00
Percentage: 61.00%
Final Result: Pass
Classification: First Class
========================================
