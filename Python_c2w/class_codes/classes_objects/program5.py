class employee:

    def __init__(self,empId,empName):
        print("in constructor")
        self.empId=empId
        self.empName=empName

    def empInfo(self):
        print(self.empId)
        print(self.empName)


emp1=employee(12,"prathamesh")
emp2=employee(15,"yash")

emp1.empInfo()
emp2.empInfo()
