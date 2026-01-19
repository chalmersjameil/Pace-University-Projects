class Employee:
    def __init__(self, name, salary, years_of_service):
        self.name = name
        self.salary = salary
        self.years_of_service = years_of_service
    
    def get_salary(self):
        return self.salary
    
    def get_years_of_service(self):
        return self.years_of_service
    
    def __str__(self):
        return f"Name: {self.name}, Salary: {self.salary}, Years of Service: {self.years_of_service}"

class Department:
    def __init__(self, name):
        self.name = name
        self.employees = []
    
    def get_employees(self):
        return self.employees
    
    def add_employee(self, employee):
        self.employees.append(employee)
    
    def department_size(self):
        return len(self.employees)
    
    def average_salary(self):
        total_salary = sum(employee.get_salary() for employee in self.employees)
        return total_salary / len(self.employees) if self.employees else 0
    
    def average_years_of_service(self):
        total_years = sum(employee.get_years_of_service() for employee in self.employees)
        return total_years / len(self.employees) if self.employees else 0
    
    def __str__(self):
        return f"Department: {self.name}, Employees: {self.department_size()}"

    def top_earners(self, top_n=3):
        sorted_employees = sorted(self.employees, key=lambda e: e.get_salary(), reverse=True)
        return sorted_employees[:top_n]

def main():
    # Create Employee instances
    alice = Employee("Alice", 100000, 12)
    bob = Employee("Bob", 45000, 2)
    carol = Employee("Carol", 50000, 5)
    bryan = Employee("Bryan", 85000, 8)
    dan = Employee("Dan", 70000, 8)
    erin = Employee("Erin", 65000, 8)
    frank = Employee("Frank", 99000, 10)
    grace = Employee("Grace", 550000, 3)

    # Create Department instances and add employees
    sales = Department("Sales")
    sales.add_employee(alice)
    sales.add_employee(bob)
    
    marketing = Department("Marketing")
    marketing.add_employee(carol)
    marketing.add_employee(bryan)
    
    it = Department("IT")
    it.add_employee(dan)
    
    engineering = Department("Engineering")
    engineering.add_employee(erin)
    
    product_development = Department("Product Development")
    product_development.add_employee(frank)
    
    executive_office = Department("Executive Office")
    executive_office.add_employee(grace)

    # List of departments
    departments = [sales, marketing, it, engineering, product_development, executive_office]
    employees = [alice, bob, carol, bryan, dan, erin, frank, grace]

    # Print the top 3 earners in each department
    for department in departments:
        print(f"\nTop 3 earners in {department.name} Department:")
        top_earners = department.top_earners()
        for i, employee in enumerate(top_earners, 1):
            print(f"{i}. {employee}")

    # Find the largest departments based on number of employees
    print("\nLargest departments:")
    largest_departments = sorted(departments, key=lambda d: d.department_size(), reverse=True)
    for i, department in enumerate(largest_departments, 1):
        print(f"{i}. {department.name} - {department.department_size()} employees")

if __name__ == "__main__":
    main()
