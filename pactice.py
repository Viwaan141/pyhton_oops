class Employee: #class define
    name = "Prakash"
    designation = "Manager"
    salesMadeThisWeek = 6
    def hasAchievedtarget(self): #attribute called inside class using self keyword
        if self.salesMadeThisWeek >= 5:
            print("target has been achieved")
        else:
            print("Target has not been achieved")

employeeOne = Employee() #object instance
print(employeeOne.name) #invoked(called) class attribute
employeeOne.hasAchievedtarget()
