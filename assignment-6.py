#LOOPS


#QUESTION: 1  

#Take a Input From User and Print On Screen
n=str(input("Enter your Sweet Name : "))
c=int(input("Enter how many times you want to print your name : "))
for x in range (c):
 print(n)

 
#QUESTION: 2  

#Write an Infinite Loop.
#n=int(input("Enter any number"))
#i=1
#while i<=n:
# print(n)

 
#QUESTION: 3 
 
#Create a List of Integers And Make a New List Which Will Store The Square Of The Elements.
l=[4,12,5,100]
n=[]
i=0
for x in l:
 b=l[i] * l[i] 
 n.append(b)
 i=i+1
print(n) 

 
#QUESTION: 4  


#Form a list for Integer,Float and String
integer=[]
for x in range(3):
 x=int(input("enter integer"))
 integer.append(x)
print(integer) 
string=[]
for x in range(3):
 x=str(input("enter string"))
 string.append(x)
print(string) 
float=[]
for x in range(3):
 x=(input("enter float"))
 float.append(x)
print(float) 


#QUESTION: 5  


#Using range(1,101), make a list containing even and odd numbers.
o=[]
e=[]
for x in range(1,101):
 if x%2==0:
  e.append(x)
 else:
   o.append(x)
print("even_no",e)
print("odd_no.",o)   
  
 
 #QUESTION: 6  


#Print Patterns
for x in range(0,70):
 for y in range(0,x+1):
  print("*",end="")
 print() 
  
 

#QUESTION: 7  


#Create a User Defined Dictionary
d={}
for x in range(2):
 name=str(input("enter name of student : "))
 marks=int(input("enter marks of student : "))
 d[name]=marks
print(d) 


#QUESTION: 8  


#Perform Inputs And Search and deletion From User in a list.
list=[]
for x in range(5):
 x=int(input("enter a no."))
 list.append(x)
print("list",list) 
v=int(input("enter no. you want to search : "))
for y in list:
 if y==v:
  print("value found",y)
de=int(input("enter no. you want to remove : "))
for y in list:
 if y==de:
  print(list.remove(de))
  print(list)



