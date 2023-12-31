def outerfunction():
    print("In outer function")

    def Innerfunction1():
        print("In inner function 1")

    def Innerfunction2():
        print("In inner dunction 2")

    Innerfunction1()
    Innerfunction2()

outerfunction()

