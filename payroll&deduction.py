#Algorithm
1. Start the program.
2. Input the employee's name and basic salary.
3. Input allowances, overtime hours, overtime rate per hour, and incentives.
4. Calculate overtime pay:
   
   Overtime Pay = Overtime Hours × Overtime Rate
5. Calculate gross salary:
   
   Gross Salary = Basic Salary + Allowances + Overtime Pay + Incentives
6. Calculate progressive deductions using the following example rules:
   - First ₹10,000 of gross salary: 0% deduction.
   - Next ₹10,000: 5% deduction.
   - Remaining amount above ₹20,000: 10% deduction.
7. Calculate net salary:
   
   Net Salary = Gross Salary − Total Deductions
8. Display the employee's formatted salary statement.
9. Stop the program.
#Flow chart
               ┌───────────────┐
             │     START     │
             └───────┬───────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │ Input employee name,      │
       │ basic salary, allowances, │
       │ overtime and incentives   │
       └─────────────┬─────────────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │ Calculate overtime pay    │
       │ = Hours × Rate            │
       └─────────────┬─────────────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │ Calculate gross salary    │
       │ = Basic + Allowances +    │
       │ Overtime + Incentives     │
       └─────────────┬─────────────┘
                     │
                     ▼
              ◇──────────────◇
             / Gross salary  \
            <   <= 10000?     >
             \              /
              ◇──────┬─────◇
                 Yes │ No
                     │
           ┌─────────┴──────────┐
           ▼                    ▼
   ┌──────────────┐    ◇────────────────◇
   │ Deduction = 0│   / Gross salary     \
   └──────┬───────┘  <   <= 20000?        >
          │            \                /
          │             ◇──────┬───────◇
          │                Yes │ No
          │                    │
          │          ┌─────────┴──────────┐
          │          ▼                    ▼
          │  ┌────────────────┐  ┌─────────────────┐
          │  │ Deduction = 5%  │  │ Deduction = 500 │
          │  │ of amount above│  │ + 10% of amount │
          │  │ Rs. 10000      │  │ above Rs. 20000 │
          │  └───────┬────────┘  └────────┬────────┘
          │          │                    │
          └──────────┴────────────────────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │ Net Salary = Gross Salary │
       │             - Deduction   │
       └─────────────┬─────────────┘
                     │
                     ▼
       ┌───────────────────────────┐
       │ Display formatted salary  │
       │ statement                 │
       └─────────────┬─────────────┘
                     │
                     ▼
             ┌───────────────┐
             │     STOP      │
             └───────────────┘
#Code
 # Employee Payroll and Deduction Analysis

name = input("Enter employee name: ")
basic = float(input("Enter basic salary: "))
allowances = float(input("Enter allowances: "))
overtime_hours = float(input("Enter overtime hours: "))
overtime_rate = float(input("Enter overtime rate per hour: "))
incentives = float(input("Enter incentives: "))

# Calculate overtime pay
overtime_pay = overtime_hours * overtime_rate

# Calculate gross salary
gross_salary = basic + allowances + overtime_pay + incentives

# Calculate progressive deductions
if gross_salary <= 10000:
    deduction = 0
elif gross_salary <= 20000:
    deduction = (gross_salary - 10000) * 0.05
else:
    deduction = (10000 * 0.05) + (
        (gross_salary - 20000) * 0.10
    )

# Calculate net salary
net_salary = gross_salary - deduction

# Display salary statement
print("\n========== SALARY STATEMENT ==========")
print("Employee Name       :", name)
print(f"Basic Salary        : Rs. {basic:.2f}")
print(f"Allowances          : Rs. {allowances:.2f}")
print(f"Overtime Pay        : Rs. {overtime_pay:.2f}")
print(f"Incentives          : Rs. {incentives:.2f}")
print("--------------------------------------")
print(f"Gross Salary        : Rs. {gross_salary:.2f}")
print(f"Total Deductions    : Rs. {deduction:.2f}")
print("--------------------------------------")
print(f"Net Salary          : Rs. {net_salary:.2f}")
print("======================================")

#Sample output
Enter employee name: Ravi
Enter basic salary: 18000
Enter allowances: 3000
Enter overtime hours: 5
Enter overtime rate per hour: 200
Enter incentives: 2000

========== SALARY STATEMENT ==========
Employee Name       : Ravi
Basic Salary        : Rs. 18000.00
Allowances          : Rs. 3000.00
Overtime Pay        : Rs. 1000.00
Incentives          : Rs. 2000.00
--------------------------------------
Gross Salary        : Rs. 24000.00
Total Deductions    : Rs. 900.00
--------------------------------------
Net Salary          : Rs. 23100.00
======================================
