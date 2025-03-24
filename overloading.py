class SumClass:
 def sum(self,a=None,b=None,c=None):
    if a!=None and b!=None:
        print("Function with two arguments")
        print("Sum=",a+b)
    elif a!=None and b!=None and c!=None:
        print("Function with three arguments")
        print("Sum=", a+b+c)
    else:
        print("Provide more numbers")
obj = SumClass()
obj.sum(19, 8, 77)
obj.sum(18, 20)
