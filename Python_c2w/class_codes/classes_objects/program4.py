class employee(object):

    def __init__(self):
        print("in constructor")
        self.x=10
        self.y=20

    def disp(self):
        print(self.x)
        print(self.y)


obj=employee()
obj.disp()


