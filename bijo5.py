class book:
    price=100
    @classmethod
    def display(cls):
        print(cls.price)
    def show(self,x):
 ##         self.price=x
         print(self.price)
b=book()
b.display()
b.show(200)

class student:
    @staticmethod
    def deportments(dept):
        available_dept=["mech","civil"]
        if dept in available_dept:
            return 'true'
        return 'false'
str=student()
print(str.deportments('civil'))

class product:
    count =0
    def __init__(self,name):
        self.name=name
        product.count+=1
    @staticmethod
    def productstaticcount():
        return product.count
    @classmethod
    def productclasscount(cls):
        print("class info:",cls)
        print("class count:",cls.count)
p1=product("camera")
print(p1.productstaticcount())
print(p1.productclasscount())

class rect:
    def __init__(self,x,y):
        self.l=x
        self.b=y
    def rectarea(self):
        return self.l*self.b
r=rect(5,8)
s=r
print("rectangle is",r.rectarea())
print("rectangle is",s.rectarea())

class rect:
    n=0
    def __init__(self,x,y):
        rect.n+=1
        self.l=x
        self.b=y
    def __del__(self):
        rect.n-=1
        class_name =self.__class__.__name__
        print(class_name,"destroyed")
    def rectarea(self):
        print("rectangle is",self.l*self.b)
    def noofobject(self):
        print("objects are",rect.n)
r=rect(3,5)
r.rectarea()
r.noofobjects()

class rect:
    def __init__(self,x,y):
        self.__l=x
        self.__b=y
    def rectarea(self):
        return self.__l*self.__b
r=rect(5,8)
print("rectangle is",r.rectarea())

class rect:
    def __init__(self,x,y):
        self.l=x
        self.b=y
    def area(self):
        return self.l*self.b
class triancle(rect):
    def __init__(self):
        rect__init__(self)
        self.x=17
        self.y=18
    def area(self):
        return 1/2*self.x*self.y
r=rect()
print("rect is",r.area())
        
        


        






    
