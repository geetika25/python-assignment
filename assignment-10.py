#ASSIGNMENT-11



#Question.1- Create a class Animal as a base class and define method animal_attribute.
#Create another class Tiger which is inheriting Animal and access the base class method

#create class Animal as a base class
class Animal:
 def __init__(self,characteristics):
  self.characteristics=characteristics
 def attribute (self):
  print("characteristics of tiger",self.characteristics)
  #second class Tiger and inherit it with class Animal
class Tiger(Animal):
 def attribute2(self):
  print("tiger is the symbol of anger")
n=input("enter the characteristics of tiger")
t=Tiger(n)  
t.attribute()
t.attribute2()


 #Question.2- What will be the output of following code.
#class A:
    #def f(self):
       # return self.g()

    #def g(self):
       # return 'A'

#class B(A):
    #def g(self):
        #return 'B'

#a = A()
#b = B()
#print a.f(), b.f()
#print a.g(), b.g()

#solution.2- 
#output: A B
#        A B
#code after update
#class A:
    #def f(self):
       # return self.g()

    #def g(self):
       # return 'A'

#class B(A):
    #def g(self):
        #return 'B'

#a = A()
#b = B()
#in the previous program the required brackets missing.
#print (a.f(), b.f())
#print (a.g(), b.g())


#Q.3- Create a class Cop. Initialize its name, age , work experience and designation.
#Define methods to add, display and update the following details.
#Create another class Mission which extends the class Cop. Define method add_mission _details. 
#Select an object of Cop and access methods of base class to get information for a particular cop and make it available for mission.


class Cop:
 def __init__ (self,name,age,work_experience,designation):
  self.name=name
  self.age=age
  self.work_experience=work_experience
  self.designation=designation
 def display(self):
  print("name : ",self.name)
  print("age : ",self.age)
  print("work_experience : ",self.work_experience)
  print("designation : ",self.designation)
 def update(self,name,age,work_experience,designation):
  self.name=name
  self.age=age
  self.work_experience=work_experience
  self.designation=designation
class Mission(Cop):
 g="the mission of the Los Angeles Police Department to safeguard the lives and property of the people "
 b="to caught a rappiest of a girl"
 def add_mission(self):
  print("mission_imformation : ",self.g,self.b)
n=input("enter your  good  name : ")
a=int(input("enter your age : "))
w=input("enter your work_experience")
d=input("enter your designation")
c=Mission(n,a,w,d)
c.display()
c.add_mission()
c.update(input("enter your  good  name : "),int(input("enter your age : ")),input("enter your work_experience"),input("enter your designation"))
c.display()
c.add_mission()
  
 
#Q.4- Create a class Shape.Initialize it with length and breadth Create the method Area.
#Create class rectangle and square which inherits shape and access the method Area.

class Shape:
 def __init__(self,length,breadth):
  self.length=length
  self.breadth=breadth
 def area(self):
    print("area=",self.length*self.breadth)
class Rectangle(Shape):
  def area(self):
    print("Area of rectangle=",self.length*self.breadth)
class Square(Shape):	
  def area(self):
    print("Area of square=",self.length*self.breadth)
l=int(input("Enter length:-"))
b=int(input("Enter Breadth:-"))
if l!=b:
  r=Rectangle(l,b)
  r.area()
else:
  s=Square(l,b)
  s.area()  