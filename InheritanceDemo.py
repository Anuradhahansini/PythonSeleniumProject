# creating the parent class
class Employee:
    def __init__(self, empname, emproll):
        self.empname = empname
        self.emproll = emproll

    # This method should be part of the Employee class, not inside __init__
    def getdetails(self): # Corrected indentation here
        print(f"Employee Name: {self.empname}")
        print(f"Employee Roll: {self.emproll}")

# creating the child1 class
class QA(Employee):

    def __init__(self, dept, empname, emproll):
       self.dept = dept
       # Calling the parent class (Employee) constructor correctly
       # super().__init__(empname, emproll) # Alternative and often preferred way
       Employee.__init__(self, empname, emproll)

    # This method should be part of the QA class, not inside __init__
    def getdept(self): # Corrected indentation here
        print(f"Department: {self.dept}")


# Creating the Child2 class
class DEV(Employee):
    def __init__(self, dept, empname, emproll):
        self.dept = dept
        # Calling the parent class (Employee) constructor correctly
        # super().__init__(empname, emproll) # Alternative and often preferred way
        Employee.__init__(self, empname, emproll)

    def getdept(self):
        print(f"Department: {self.dept}")

# Creating the object for child class

print("--- QA Object Details ---")
obj1 = QA("Automation", "ram", 1)
# Now getdetails() is available because QA inherits from Employee
obj1.getdetails()
obj1.getdept()


print("\n--- DEV Object Details ---")
obj2 = DEV("Developer", "Kumar", 2)
# Now getdetails() is available because DEV inherits from Employee
obj2.getdetails()
obj2.getdept()