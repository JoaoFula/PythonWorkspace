class Employee:
    # Common class base for all employees
    empCount = 0

    # __init__ function allows the creation of the class by calling Employee(name, salary)
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1

    def displayCount(self):
        print("Total number of employees %d" % Employee.empCount)

    def displayEmployee(self):
        print("Name: ", self.name, ", Salary: ", self.salary)

# This will create the first object of the Employee class 
emp1 = Employee ("Greg", 5000)
emp2 = Employee ("Chris", 3000)

emp1.displayEmployee()
emp2.displayEmployee()
print("Total Employee %d" % Employee.empCount)