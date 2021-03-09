class calculator:
    a =0
    b =0
    def __init(self,a,b):
        self.a=a
        self.b=b

    
    def add(self, a, b):
        return a+b
    def subtract(self, a, b):
        return a-b
    def multiply(self, a, b):
        return a*b
    def divide(self, a, b):
        return a/b
my_cl = calculator()
while True:
    print("1: Add")
    print("2: subtract")
    print("3: multiply")
    print("4: divide")
    print("5: Exit")
    ch = int(input ("select operation:"))

    if ch in (1, 2, 3, 5):
       if(ch == 5):
            break                     
    a = int(input("Enter the first number:"))
    b = int(input("Enter the second number:"))

    if(ch == 1):
       print(a, "+", b, "=", my_cl.add(a,b) )
    elif(ch == 2):
       print(a, "-", b, "=",my_cl.subtract(a,b) )
    elif(ch == 3):
       print(a, "*", b, "=",my_cl.multiply(a,b) )
    elif(ch == 4):
       print(a, "/", b, "=",my_cl.divide(a,b) )
else:
       print("Invalid Input")


