x=int(input("enter the value x"))
y=int(input("enter the value of y"))
for i in range(x,y+1):
    if(i%2==0):
        print(i,"is even")
    else:
        print(i,"is odd")
