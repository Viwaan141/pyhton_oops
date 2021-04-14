class Employee:
    numberOfWorkinghours = 40

employeeOne = Employee() #created emplyee object
employeeTwo = Employee() #created employee object
print(employeeOne.numberOfWorkinghours)
print(employeeTwo.numberOfWorkinghours)
Employee.numberOfWorkinghours = 45 #changed attribute value of class
print(employeeOne.numberOfWorkinghours)
print(employeeTwo.numberOfWorkinghours)
employeeOne.numberOfWorkinghours = 35 #changed attribute value of one of the objects
print(employeeOne.numberOfWorkinghours)
print(employeeTwo.numberOfWorkinghours)

employeeOne.name = "Prakash" #created new attribute in class
print(employeeOne.name)
employeeTwo.name = "Viwaan"
print(employeeTwo.name)

