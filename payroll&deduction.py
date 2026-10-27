
def calculate_payroll(name, employee_id, basic, allowances,
                      overtime_hours, overtime_rate, incentives):

    # Calculate salary components
    overtime_pay = overtime_hours * overtime_rate
    gross_salary = basic + allowances + overtime_pay + incentives

    # Progressive deductions based on gross salary
    if gross_salary <= 20000:
        tax = gross_salary * 0.05
    elif gross_salary <= 40000:
        tax = 20000 * 0.05 + (gross_salary - 20000) * 0.10
    else:
        tax = (20000 * 0.05
               + 20000 * 0.10
               + (gross_salary - 40000) * 0.15)

    # Other deductions
    provident_fund = basic * 0.12
    insurance = 500

    total_deductions = tax + provident_fund + insurance
    net_salary = gross_salary - total_deductions

    # Formatted salary statement
    print("\n" + "=" * 45)
    print("           EMPLOYEE SALARY STATEMENT")
    print("=" * 45)
    print(f"Employee Name       : {name}")
    print(f"Employee ID         : {employee_id}")
    print("-" * 45)
    print(f"Basic Pay           : Rs. {basic:,.2f}")
    print(f"Allowances           : Rs. {allowances:,.2f}")
    print(f"Overtime Pay         : Rs. {overtime_pay:,.2f}")
    print(f"Incentives           : Rs. {incentives:,.2f}")
    print("-" * 45)
    print(f"Gross Salary         : Rs. {gross_salary:,.2f}")
    print("\nDEDUCTIONS")
    print("-" * 45)
    print(f"Progressive Tax      : Rs. {tax:,.2f}")
    print(f"Provident Fund (12%) : Rs. {provident_fund:,.2f}")
    print(f"Insurance            : Rs. {insurance:,.2f}")
    print("-" * 45)
    print(f"Total Deductions     : Rs. {total_deductions:,.2f}")
    print(f"NET SALARY           : Rs. {net_salary:,.2f}")
    print("=" * 45)


# Sample employee details
calculate_payroll(
    name="Ravi Kumar",
    employee_id="EMP101",
    basic=25000,
    allowances=5000,
    overtime_hours=10,
    overtime_rate=200,
    incentives=3000
)
