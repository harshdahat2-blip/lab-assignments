# employee_salary.py

name = input("Enter Employee Name: ")
emp_id = input("Enter Employee ID: ")
dept = input("Enter Department: ")
basic = float(input("Enter Basic Salary: "))

da = 0.92 * basic
hra = 0.58 * basic
ta = 0.30 * basic
lic = 500

gross_salary = basic + da + hra + ta
net_salary = gross_salary - lic

print("\n--- Salary Details ---")
print("Name:", name)
print("Employee ID:", emp_id)
print("Department:", dept)
print("Basic Salary:", basic)
print("Gross Salary:", gross_salary)
print("Net Salary:", net_salary)