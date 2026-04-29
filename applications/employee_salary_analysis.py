# Step 1: Get number of employees
n = int(input("Enter number of employees: "))

emp_list = []

# Taking input for each employee
for i in range(n):
    print(f"\nEnter details of Employee {i+1}")
    emp_id = int(input("Enter ID: "))
    name = input("Enter Name: ")
    salary = int(input("Enter Salary: "))
    
    emp_list.append((emp_id, name, salary))

# Convert list to tuple
employees = tuple(emp_list)

# Step 2: Display all employee details
print("\n--- All Employee Details ---")
for emp in employees:
    print("ID:", emp[0], "| Name:", emp[1], "| Salary:", emp[2])

# Step 3: Search for an employee using Employee ID
search_id = int(input("\nEnter Employee ID to search: "))
found = False

for emp in employees:
    if emp[0] == search_id:
        print("Employee Found:", emp)
        found = True
        break

if not found:
    print("Employee not found")

# Step 4: Find employee with highest salary
max_emp = employees[0]

for emp in employees:
    if emp[2] > max_emp[2]:
        max_emp = emp

print("\nEmployee with Highest Salary:")
print("ID:", max_emp[0], "| Name:", max_emp[1], "| Salary:", max_emp[2])

# Step 5: Employees with salary > 50000
print("\nEmployees with Salary > 50000:")
for emp in employees:
    if emp[2] > 50000:
        print("ID:", emp[0], "| Name:", emp[1], "| Salary:", emp[2])
