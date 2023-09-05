class Employee:
    def __init__(self, emp_id, name, age, salary):
        self.emp_id = emp_id
        self.name = name
        self.age = age
        self.salary = salary

class EmployeeTable:
    def __init__(self):
        self.employees = []

    def add_employee(self, employee):
        self.employees.append(employee)

    def search_by_age(self, target_age):
        matching_employees = [emp for emp in self.employees if emp.age == target_age]
        return matching_employees

    def search_by_name(self, target_name):
        matching_employees = [emp for emp in self.employees if emp.name.lower() == target_name.lower()]
        return matching_employees

    def search_by_salary(self, operator, target_salary):
        if operator == '>':
            matching_employees = [emp for emp in self.employees if emp.salary > target_salary]
        elif operator == '<':
            matching_employees = [emp for emp in self.employees if emp.salary < target_salary]
        elif operator == '<=':
            matching_employees = [emp for emp in self.employees if emp.salary <= target_salary]
        elif operator == '>=':
            matching_employees = [emp for emp in self.employees if emp.salary >= target_salary]
        else:
            matching_employees = []
        return matching_employees

    def display_results(self, result_employees):
        if not result_employees:
            print("No matching records found.")
        else:
            print("Employee ID\tName\tAge\tSalary (PM)")
            for emp in result_employees:
                print(f"{emp.emp_id}\t{emp.name}\t{emp.age}\t{emp.salary}")

def main():
    emp_table = EmployeeTable()

    # Populate the employee table with sample data
    emp_table.add_employee(Employee("161E90", "Raman", 41, 56000))
    emp_table.add_employee(Employee("161F91", "Himadri", 38, 67500))
    emp_table.add_employee(Employee("161F99", "Jaya", 51, 82100))
    emp_table.add_employee(Employee("171E20", "Tejas", 30, 55000))
    emp_table.add_employee(Employee("171G30", "Ajay", 45, 44000))

    while True:
        print("\nSearch Options:")
        print("1. Age")
        print("2. Name")
        print("3. Salary")
        print("4. Quit")
        
        choice = input("Enter your choice (1/2/3/4): ")

        if choice == '1':
            target_age = int(input("Enter the age to search for: "))
            result_employees = emp_table.search_by_age(target_age)
            emp_table.display_results(result_employees)
        elif choice == '2':
            target_name = input("Enter the name to search for: ")
            result_employees = emp_table.search_by_name(target_name)
            emp_table.display_results(result_employees)
        elif choice == '3':
            operator = input("Enter the salary operator (<, >, <=, >=): ")
            target_salary = int(input("Enter the salary to search for: "))
            result_employees = emp_table.search_by_salary(operator, target_salary)
            emp_table.display_results(result_employees)
        elif choice == '4':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option (1/2/3/4).")

if __name__ == "__main__":
    main()
