class A:                       #syntax for classes
    def __init__(self):
        print('hello Raju')
a=A()

class B:
    def __init__(self):
        pass
    def sum(self,a,b):
        c=a+b
        return c
    def sumofmultiplevalues(self,a,b,c,d):
        e=self.sum(a,b)
        f=self.sum(c,d)
        return e*f
b=B()

b.sum(1,2)
b.sumofmultiplevalues(2,3,4,5)

