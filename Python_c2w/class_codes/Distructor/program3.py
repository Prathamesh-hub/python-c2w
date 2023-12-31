class Demo:
    print("Start class")

    def __init__(self):
        print("in constructor")

    print("end class")

    def __del__(self):
        print("in destructor")


print("start")
obj1=Demo()
obj2=Demo()
obj3=obj1
del obj1
print("end")
