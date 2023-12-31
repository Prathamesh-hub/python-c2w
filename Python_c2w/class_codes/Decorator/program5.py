def decorfun(fun):

    def wrapper():
        print("start Wrapper")
        fun()
        print("end wrapper")

    return wrapper
    
####@decorfun
def normalfun():
    print("hello in normal function")

####normalfun=decorfun(normalfun)
normalfun()

