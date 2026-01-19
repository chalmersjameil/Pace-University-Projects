def main():
    employees = {
        'Alice': {'salary': 100000, 'years_of_service': 12, 'department': 'Sales'},
        'Bob': {'salary': 45000, 'years_of_service': 2, 'department': 'Sales'},
        'Carol': {'salary': 50000, 'years_of_service': 5, 'department': 'Marketing'},
        'Bryan': {'salary': 85000, 'years_of_service': 8, 'department': 'Marketing'},
        'Dan': {'salary': 70000, 'years_of_service': 8, 'department': 'IT'},
        'Erin': {'salary': 65000, 'years_of_service': 8, 'department': 'Engineering'},
        'Frank': {'salary': 99000, 'years_of_service': 10, 'department': 'Product Development'},
        'Grace': {'salary': 550000, 'years_of_service': 3, 'department': 'Executive Office'},
    }

    # Find top earners
    top_earners = sorted(employees, key=lambda x: employees[x]['salary'], reverse=True)[:3]
    print("Top 3 earners:", top_earners)

    # Find longest serving employees
    longest_serving = sorted(employees, key=lambda x: employees[x]['years_of_service'], reverse=True)[:3]
    print("Top 3 longest-serving employees:", longest_serving)

    # Departmental analysis
    departments = {}
    for name, info in employees.items():
        dept = info['department']
        if dept not in departments:
            departments[dept] = {'total_salary': 0, 'total_years': 0, 'num_employees': 0}
        departments[dept]['total_salary'] += info['salary']
        departments[dept]['total_years'] += info['years_of_service']
        departments[dept]['num_employees'] += 1

    # Print each department's analysis
    for dept, data in departments.items():
        avg_salary = data['total_salary'] / data['num_employees']
        avg_years = data['total_years'] / data['num_employees']
        print(f"{dept}: Employees={data['num_employees']}, Avg Salary={avg_salary}, Avg Years={avg_years}")

    # Largest departments by number of employees
    largest_departments = sorted(departments, key=lambda x: departments[x]['num_employees'], reverse=True)[:3]
    print("3 largest departments:", largest_departments)

    # Costliest departments by salary expenditure
    costliest_departments = sorted(departments, key=lambda x: departments[x]['total_salary'], reverse=True)[:3]
    print("3 costliest departments:", costliest_departments)

if __name__ == '__main__':
    main()
