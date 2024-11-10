class Employee:
    def __init__(self, name, employee_id, salary):
        self.name = name
        self.employee_id = employee_id
        self.salary = salary
    
    def display_details(self):
        print(f"Employee ID: {self.employee_id}, Name: {self.name}, Salary: ${self.salary:.2f}")
    
    def update_salary(self, new_salary):
        self.salary = new_salary
        print(f"Updated salary for {self.name} to ${self.salary:.2f}")

class Department:
    def __init__(self, department_name):
        self.department_name = department_name
        self.employees = []
    
    def add_employee(self, employee):
        self.employees.append(employee)
        print(f"Added employee '{employee.name}' to the department '{self.department_name}'")
    
    def calculate_total_salary_expenditure(self):
        total_salary = sum(employee.salary for employee in self.employees)
        print(f"Total salary expenditure for department '{self.department_name}': ${total_salary:.2f}")
    
    def display_all_employees(self):
        if self.employees:
            print(f"Employees in department '{self.department_name}':")
            for employee in self.employees:
                employee.display_details()
        else:
            print(f"No employees in department '{self.department_name}'.")

# Interactive code for adding employees and displaying total salary expenditure
def department_management():
    department = Department("Finance")
    
    while True:
        print("\nDepartment Management System:")
        print("1. Add Employee")
        print("2. Update Employee Salary")
        print("3. Display All Employees")
        print("4. Display Total Salary Expenditure")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ")
        
        if choice == "1":
            name = input("Enter employee's name: ")
            employee_id = input("Enter employee's ID: ")
            try:
                salary = float(input("Enter employee's salary: "))
                employee = Employee(name, employee_id, salary)
                department.add_employee(employee)
            except ValueError:
                print("Invalid input for salary. Please enter a numeric value.")
        
        elif choice == "2":
            employee_id = input("Enter employee's ID to update salary: ")
            try:
                new_salary = float(input("Enter new salary: "))
                employee = next((e for e in department.employees if e.employee_id == employee_id), None)
                if employee:
                    employee.update_salary(new_salary)
                else:
                    print(f"Employee with ID {employee_id} not found.")
            except ValueError:
                print("Invalid input for salary. Please enter a numeric value.")
        
        elif choice == "3":
            department.display_all_employees()
        
        elif choice == "4":
            department.calculate_total_salary_expenditure()
        
        elif choice == "5":
            print("Exiting the department management system.")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the department management system
department_management()
