class company:
    compName = "facebook"

    def __init__(self):
        print("in constructor")
        self.empId=12
        self.empName="kanha"

    def compInfo(self):
        print(self.empId)
        print(self.empName)
        print(self.compName)


emp1=company()
emp1.compInfo()
emp2=company()
emp2.compinfo( compName = "meta")
