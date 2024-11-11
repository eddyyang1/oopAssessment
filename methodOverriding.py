class Employee:
    def calculate_salary(self):
        print("Calculating salary...")

class Manager(Employee):
    def calculate_salary(self):
        print("Manager salary is calculated based on additional benefits.")

# Demonstration
emp = Employee()
mgr = Manager()
emp.calculate_salary()
mgr.calculate_salary()
