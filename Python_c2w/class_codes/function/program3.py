def div(x):
    if(x%4==0 and x%5==0):
        print(x,"divisible by 4")
    else:
        print(x,"divisible by 5")

x=int(input("enter the value"))
div(x)
