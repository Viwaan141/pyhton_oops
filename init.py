class Employee:
    def __init__(self,passedName): #this method is called when classs or object is called
        self.name = passedName

    def dispalyEmployeeDetails(self):
        print(self.name)

employee =  Employee("Prakash")
employeeTwo = Employee("Viwaan")
employee.dispalyEmployeeDetails()
employeeTwo.dispalyEmployeeDetails()
