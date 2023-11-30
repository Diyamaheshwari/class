'''class employee():
    def _init_(self,name,age,Id):
        self.name=name
        self.age=age
        self.Id=Id
     
                     
    def display(self):
        print("Name is:",name)
        print("Age is:",age)
        print("Id is:",Id)

name=input("Enter your name: ")
age=int(input("Enter your age:"))
Id=int(input("Enter your Id:")) 
obj=employee()

obj.display()

class student:
    pass
stud_1=student()
stud_2=student()
stud_1.name='SriRam'
stud_1.age=25
stud_1.graduate="MBA"
stud_2.name='Lakshman'
stud_2.age=23
stud_2.graduate="Engineer"
print("stud_1.name:",stud_1.name)
print("stud_1.age:",stud_1.age)
print("stud_1.graduate:",stud_1.graduate)
print("stud_2.name:",stud_2.name)
print("stud_2.age:",stud_2.age)
print("stud_2.graduate:",stud_2.graduate)

1) class
2) Object
3) constructor
4)Method overloading
6) overriding
5)Inheritance
7)Data hiding
8) polymorphism'''

            #METHOD OVERLOADING

'''class Class_Name:
    def method1(self,name="a",wish="b",rollno=456):
        self.name=name
        self.wish=wish
        self.rollno=rollno
        print(self.name,self.wish,self.rollno)
object_1=Class_Name()
object_1.method1()
object_1.method1("Ram")
object_1.method1("Ram","Good Morning")'''

                #Inheritance

'''class car:
    def setenginemodel(self, engine):
        self.engine=engine
    def getenginemodel(self):
        print(self.engine)
class Honda(car):
    def setcarmodel(self,model):
        self.model=model
    def getcarmodel(self):
        print(self.model)
mycar=Honda()
mycar.setenginemodel('EK-1')
mycar.setcarmodel('v6')
print('Car Details')
mycar.getenginemodel()
mycar.getcarmodel()'''

            #multiple inheritance

'''class car:
    def setenginemodel(self, engine):
        self.engine=engine
    def getenginemodel(self):
        print(self.engine)
class tyre:
    def settyrenumber(self,num):
        self.num=num
    def gettyrenumber(self,num):
        print(self.num)
class Honda(car,tyre):
    def setcarmodel(self,model):
        self.model=model
    def getcarmodel(self):
        print(self.model)
accord=Honda()
accord.setenginemodel("EK-1")
accord.setcarmodel("V6")
accord.settyrenumber(236)
print("car details: ")
accord.getenginemodel()
accord.getcarmodel()
accord.gettyrenumber()
#multilevel'''

            #Hierarchical inheritance

"""class Parent:
    def func1(self):
        print("This function is in parent class")
class Child1(Parent):
    def func2(self):
        print("This function is in child1")
class Child2(Parent):
    def func3(self):
        print("This function is in child2")

object1=Child1()
object2=Child2()
object1.func1()
object1.func2()
object2.func1()
object2.func3()"""

            #overriding

'''class Parent:
    def func1(self):
        print("This function is in parent class")
class Child1(Parent):
    def func1(self):
        #Parent.func1(self)
        super().func1()
        print("This function is in child1")
class Child2(Parent):
    def func3(self):
        print("This function is in child2")

object1=Child1()
object2=Child2()
object1.func1()
object2.func3()'''

        #public and private data members

'''class ABC():
    def __init__(self,var1,var2):
        self.var1=var1
        self.__var2=var2
    def display(self):
        print("From class method, var1=",self.var1)
        print("From class method, var2=",self.__var2)
obj=ABC(10,20)
obj.display()
print("From main module,var1=",obj.var1)'''

            #private methods
class ABC():
    def __init__(self,var):
        self.var=var
    def __display(self):
        print("From class method,var=",self.var)
obj=ABC(10)
obj._ABC__display()

            
