class Employee:
    def employeeDetails(self): #instance method 
        self.name = "Prakash"
     
    @staticmethod  #decorator
    def welcomeMessage(): #static method without -> when self is not used
        print("welcome to our organisation")
        
        
employee = Employee()
employee.employeeDetails()
print(employee.name)
employee.welcomeMessage()