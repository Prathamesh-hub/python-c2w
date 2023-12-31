class Parent:
    def __init__(self):

        print("in parent constructor")

    def parentinfo(self):

        print("in parent info")


class child(Parent):


    def __init__(self):

        #super().__init__()

        Parent.__init__(self)

        print("in parent constructor 2")

    def childinfo(self):

        print("in child info")


obj1=child()

obj1.parentinfo()

obj1.childinfo()

