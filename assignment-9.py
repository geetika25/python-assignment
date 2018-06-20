											#Common Modules in Python

#Question.1- Create a circle class and initialize it with radius. Make two methods getArea and getCircumference inside this class.



#program to print radius , area and circumtance of a circle.
#first create class circle
class Circle:
#class  definations as init method.
 def __init__(self,radius):
  self.radius=radius
 def show1(self):
 #function to print radius
  print("Radius = ",self.radius)
 #function to print area 
 def area(self):
  print("Area of a circle = ",self.radius**2*3.14)
 #function to print circumtance
 def circum(self):
  print("Circumtance of a circle = ",self.radius*3.14*2)
#creating object of class circle
c=Circle(2)
#function calling
c.show1()
c.area()
c.circum()
   


#Question.2- Create a Student class and initialize it with name and roll number. Make methods to :
#1. Display - It should display all informations of the student.



#program to store all the imformation of the student.
class Student:
 #class definations as init method.
 def __init__(self,name,roll_no):
  self.name=name
  self.roll_no=roll_no
 #functions to print imformation to the console
 def display(self):
  print("\nhello your name is",self.name,"and your roll number is",
  self.roll_no)
n=str(input("Enter your Good name :- ")) 
r=int(input("Enter your roll_no :- ")) 
 #function calling
s=Student(n,r)
s.display()




#Q.3- Create a Temprature class. Make two methods :
#1. convertFahrenheit - It will take celsius and will print it into Fahrenheit.
#2. convertCelsius - It will take Fahrenheit and will convert it into Celsius.


#initialize class Temprature
class Temprature:
 def __init__(self,celcius,fr):
  self.celcius=celcius
  self.fr=fr
 def cel(self):
  print("convertFahrenheit : ",(self.celcius*1.8)+32)
 def fer(self):
  print(" convertCelsius : ",(self.fr-32)*(5/9)) 
#input function to take input from user 
c=int(input("Enter temprature in celsius : "))
f=int(input("Enter temprature in Fahrenheit : ")) 
b=Temprature(c,f)
b.cel()
b.fer()


#Q.4- Create a class MovieDetails and initialize it with Movie name, artistname,Year of release and ratings .
#Make methods to 
#1. Display-Display the details.
#2. Update- Update the movie details.


#create class 
class MovieDetail:
 def __init__(self,name,artist,year,rating):
  self.name=name
  self.artist=artist
  self.year=year
  self.rating=rating
  #function to print imformation
 def display(self):
  print("Great !! your favorite movie is ",self.name) 
  print("The artist name of this movie is ",self.artist)
  print("This movie is release on ",self.year)
  print("Rating status : ",self.rating)
  #input function to take input from user
  #to update the imformation ,create a function update
 def update(self,name,artist,year,rating):
  self.name=name
  self.artist=artist
  self.year=year
  self.rating=rating
n=str(input("Enter your favorite movie name : "))
a=str(input("enter artist name : "))
y=int(input("enter year of release : "))
r=int(input("enter rating : "))  
s=MovieDetail(n,a,y,r)
s.display()
s.update(str(input("Enter your favorite movie name : ")),str(input("enter artist name : ")),int(input("enter year of release : ")),int(input("enter rating : ")))
s.display()


#Q.5- Create a class Expenditure and initialize it with expenditure,savings.Make the following methods. 
#1. Display expenditure and savings 
#2. Calculate total salary
#3. Display salary

#create class Ependiture
class Ependiture:
 def __init__(self,exp,sav):
  self.exp=exp
  self.sav=sav
  #function to display the imformation
 def display(self):
  print("expenditure is : ",self.exp)
  print("saving is : ",self.sav)  
  #function to add expenditure and saving
 def add(self):
  print("total salary : ",self.exp+self.sav) 
e=int(input("enter expenditure : "))
s=int(input("enter saving : "))
 
b=Ependiture(e,s)
b.display()
b.add()