class Employee:
    empCount = 0

    # parameterized constructor
    def __init__(self, name=None, salary=None):
        self.name = name
        self.salary = salary
        Employee.empCount += 1


    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)


    def displayEmployee(self):
        print("Name : " , self.name, ",  Salary: " , self.salary)


emp1 = Employee()
emp1.displayCount()
emp1.displayEmployee()

emp2 = Employee('Ashutosh', 5000)
emp2.displayCount()
emp2.displayEmployee()
