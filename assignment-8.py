#ASSIGNMENT-8


#Let’s lookout some interesting methods and properties of the commonly used packages. 



#QUESTION: 1  


#What is Time Tuple


import time 
print(time.gmtime(60))


#QUESTION: 2  


#WAP To Get Formatted Time


import time
print(time.ctime())


#QUESTION: 3  


#Extract Month from the Time.


l=[]
import time
l=list(time.localtime())
print( "month = ",l[1])


#QUESTION: 4  


#Extract Day from the Time.

l=[]
import time
l=list(time.localtime())
print( "day = ",l[2])


#QUESTION: 5 

 
#Extract date (ex : 11 in 11/01/2021) from the time.

l=[]
import time
l=list(time.localtime())
print(l[2],"/",l[1],"/",l[0])

#QUESTION: 6  


#WAP Time Using Local Time


import time 
print(time.localtime())


#QUESTION: 7  



#Find the Factorial of a Number

n=int(input("enter any no. to calculate factorial : "))
import math
print(math.factorial(n))

#QUESTION: 8  


#Find the GCD of a Number


import math
print(math.gcd(15,21))


#Question: 9


#Use OS package and do the following tasks:
 

#1. Get current working directory


import os
print(os.getcwd())


#2. Get the user environment.

print(os.environ)