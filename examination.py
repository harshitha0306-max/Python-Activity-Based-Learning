
def calculate_result(name, subjects, grace_limit=5):
    total_marks = 0
    maximum_total = 0
    grace_used = 0
    subject_results = {}

    for subject, details in subjects.items():
        marks = details["marks"]
        maximum = details["maximum"]
        pass_marks = details["pass_marks"]

        # Validate marks
        if not (0 <= marks <= maximum):
            print(f"Invalid marks entered for {subject}")
            return

        # Calculate grace marks if needed
        grace_needed = max(0, pass_marks - marks)

        if grace_needed > 0 and grace_needed <= grace_limit - grace_used:
            marks += grace_needed
            grace_used += grace_needed

        # Ensure marks never exceed maximum
        marks = min(marks, maximum)

        passed = marks >= pass_marks

        subject_results[subject] = {
            "marks": marks,
            "maximum": maximum,
            "status": "PASS" if passed else "FAIL"
        }

        total_marks += marks
        maximum_total += maximum

    # Determine overall result
    all_passed = all(
        result["status"] == "PASS"
        for result in subject_results.values()
    )

    percentage = (total_marks / maximum_total) * 100

    if not all_passed:
        classification = "FAIL"
    elif percentage >= 75:
        classification = "DISTINCTION"
    elif percentage >= 60:
        classification = "FIRST CLASS"
    elif percentage >= 50:
        classification = "SECOND CLASS"
    else:
        classification = "PASS CLASS"

    # Display result
    print("\n" + "=" * 58)
    print("             EXAMINATION RESULT")
    print("=" * 58)
    print(f"Student Name: {name}")
    print("-" * 58)
    print(f"{'Subject':<15}{'Marks':<12}{'Maximum':<12}{'Status'}")
    print("-" * 58)

    for subject, result in subject_results.items():
        print(
            f"{subject:<15}"
            f"{result['marks']:<12}"
            f"{result['maximum']:<12}"
            f"{result['status']}"
        )

    print("-" * 58)
    print(f"Grace Marks Used : {grace_used}")
    print(f"Total Marks      : {total_marks}/{maximum_total}")
    print(f"Percentage       : {percentage:.2f}%")
    print(f"Final Result     : {classification}")
    print("=" * 58)


# Sample student details
subjects = {
    "English": {"marks": 65, "maximum": 100, "pass_marks": 35},
    "Mathematics": {"marks": 32, "maximum": 100, "pass_marks": 35},
    "Science": {"marks": 70, "maximum": 100, "pass_marks": 35},
    "Computer": {"marks": 80, "maximum": 100, "pass_marks": 35},
    "Social": {"marks": 60, "maximum": 100, "pass_marks": 35}
}

calculate_result("Ravi Kumar", subjects, grace_limit=5)
