def decorfun(fun):

    def wrapper():
        print("start wrapper 2")
        fun()
        print("end wrapper 2")

    return wrapper


def decorrun(fun):


    def wrapper():
        print("start wrapper 1")
        fun()
        print("end Wrapper 1")

    return wrapper

#@decorfun
#@decorrun
def normalfun():

    print("in normal function")


normalfun=decorfun(decorrun(normalfun))
normalfun()
