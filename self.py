class Employee:
    def employeeDetails(self):
        self.name = "Prakash" # with "self" this attribute is available for lifespan of class
        print("Name = ",self.name)
        age = 30 # without "self" this is only valid for that method only
        print("Age = ",age)

    def method2(self):
        print("printing in another method")
        print("Name:",self.name)
        print("Age:",age)

employee = Employee()
employee.employeeDetails() # same Employee.employeeDetails(employee)
employee.method2()