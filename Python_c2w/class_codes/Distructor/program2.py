class Parent:

    def __init__(self):
        print("in Parent Constructor")
        self.x=10
        self.y=20

    def dispparent(self):

        print(self.x)
        print(self.y)

class child(Parent):

    def __init__(self):

        print("in child constructor")
        print(super().__init__)
        print(Parent.__init__)
        self.x=30
        self.y=40

        


obj1=child()
obj1.dispparent()
