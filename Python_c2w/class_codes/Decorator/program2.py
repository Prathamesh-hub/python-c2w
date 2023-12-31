def outerfunction():
    print("In outer function")

    def Inner1():
        print("In inner function 1")

    def Inner2():
        print("In inner dunction 2")

    return Inner1,Inner2 

ret=outerfunction()
ret[0]()
ret[1]()
