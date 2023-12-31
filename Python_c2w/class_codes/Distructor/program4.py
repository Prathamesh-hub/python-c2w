class Demo:

    print("start ")
    def __init__(self):
        print("in constructor")

    def __del__(self):
        print("in destructor")

    print("end")


def fun():
    print("in fun")
    obj=Demo()
    print("end fun")
    return obj        
    
retobj=fun()
print("end code")
