def decorfun(fun):

    print("indecor fun")

    def Wrapper(*args):
        print("start wrapper")
        val=fun(*args)
        print("end wrapper")
        return val

    return Wrapper

@decorfun
def normalfun(x,y):
    print("in normal function")
    return x+y

print(normalfun(10,20))
