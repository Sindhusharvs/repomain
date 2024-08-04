'''
class Student:

    def __init__(self):
        self.name=''
        self.reg=''
    def display(self):
        print("Name:",self.name)
        print("Reg:",self.reg)

stu=Student()
stu1=Student()
stu.name='sindhu'
stu.reg='123'
stu1.name='preethi'
stu1.reg='345'

stu.display()
stu1.display()
'''
'''
class Fruit:
    def __init__(self,colour):
          self.colour=colour
          

apple =Fruit('red')
print(apple.colour)
'''
'''
class Teacher:
    def __init__(self,name,reg):
        self.name=name
        self.reg=reg
    def display(self):
        print(self.name)
        print(self.reg)
t1=Teacher('sindhu',123)
t2=Teacher('shalini',345)
t1.display()
t2.display()
'''
'''
class Calculator:
    def __init__(self,a,b):
        self.num1=a   Instance variables
        self.num2=b
        
    def add(self):
      print(self.num1+self.num2)
    def sub(self):
        print(self.num1-self.num2)
    def mul(self):
        print(self.num1*self.num2)
    def div(self):
        print(self.num1/self.num2)
    def mod(self):
        print(self.num1%self.num2)
        
a=int(input('Enter number:'))
b=int(input('Enter number:'))
cal=Calculator(a,b)
cal.add()
cal.sub()
cal.mul()
cal.div()
cal.mod()

'''
'''
class lap():
    charger='c-type' #class variable
    def __init__(self,name,price): #Constructors
        self.name=name
        self.price=price

    def display(self): #Instance Methods
        print('Name:',self.name)
        print('price:',self.price)
        print('charger:',self.charger)

        
obj=lap('Lenovo','10k')
obj.display()
'''
'''
class lap():
    charger='c-type' #class variable
    def __init__(self,name,price): #Constructors
        self.name=name #Instance variables
        self.price=price

    def display(self): #Instance Methods
        print('Name:',self.name)
        print('price:',self.price)
        print('charger:',self.charger)
    @classmethod
    def display_1(cls):  #class methods
        cls.charger='b-type'
        print(cls.charger)


obj=lap('Lenovo','10k')
obj.display()
lap.display_1()
'''
''' Multilevel Inheritance
class dad():
    def func(self):
        print('A')
        
class mom(dad):
    def fun(self):
        print('B')
        
class son(mom):
    def sun(self):
        print('c')
    

obj=son()
obj.func()
obj.fun()
obj.sun()
        
'''
'''
#super Keyword

class dad():
    def __init__(self):
        print('A')
    def display(self):
        print('dad')
class mom(dad):
    def __init__(self):
        super().__init__()
        print('B')
    def display(self):
        print('mom')
        
class son(mom,dad):
    def __init__(self):
        super().__init__()
        print('c')
    def display(self):
        print('son')

obj=son()
'''
'''
class person():
    def __init__(self,name,con,dob): 
        nam=self.name
        country=self.con
        DOB=self.dob

    def dateofbirth(self):
         return self.dob

Name=input('Enter your name:')
Country=input('Enter your country name:')
Dob=int(input('Enter  only your Year of ur Birth'))
obj=person(Name,Country,Dob)
print(obj.dateofbirth)            
'''
import datetime
class person():
   today=datetime.date.today()
   def __init__(self,name,con,dob): 
        self.name=name
        self.con=con
        self.dob=dob

   def dateofbirth(self):
        age=self.today-self.dob
        return age

Name=input('Enter your name:')
Country=input('Enter your country name:')
Dob=int(input('Enter  only your Year of ur Birth:'))
obj=person(Name,Country,Dob)
print(obj.dateofbirth())            


















    













































    



























