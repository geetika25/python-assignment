#ASSIGNMENT-13
#EXCEPTION HANDLING

#ASSIGNMENT-13

# EXCEPTION HANDLING
# Let’s handle some exceptions. 
# Q.1- Name and handle the exception occured in the following program: 
# a=3
# if a < 4 :
 # a=a/(a-3)
 # print(a)

#solution 1. ZeroDivisionError: division by zero.
#how to handle  the exception occured in this program.
a=3
if a<4:
 try:
  a=a/(a-3)
  print(a)
 except Exception:
  print("here an error occured") 
  
# Q.2- Name and handle the exception occurred in the following program: 
# l=[1,2,3]
# print(l[3])
#solution 2. IndexError: list index out of range.
#how to handle index out of range error.
l=[1,2,3]
try:
 l1[3]
except Exception:
 print("here an error occured*") 

# Q.3- What will be the output of the following code:

#Program to depict Raising Exception
 
# try:
    # raise NameError("Hi there")  # Raise Error
# except NameError:
    # print ("An exception")
    # raise  # To determine whether the exception was raised or not
	
#solution 3.An exception
# Traceback (most recent call last):
  # File "assignment-13.py", line 40, in <module>
    # raise NameError("Hi there")  # Raise Error
# NameError: Hi there	
	
	
	

# Q.4- What will be the output of the following code:

#Function which returns a/b
def AbyB(a , b):
	try:
		c = ((a+b) / (a-b))
	except ZeroDivisionError:
		print("a/b result in 0")
	else:
		print(c)	
#Driver program to test above function
AbyB(2.0, 3.0)
AbyB(3.0, 3.0)


#solution 4.  -5.0
#              a/b result in 0	


# Q.5- Write a program to show and handle following exceptions: 
# 1. Import Error
# 2. Value Error
# 3. Index Error

#solution 5. (i) program to illustrate ImportError
try: 
 import geet
 print("geetika")
except Exception:
 print("here ImportError occured") 
#			(ii) program to illustrate ValueError
try:
 name=int(input("Enter your age or to see the ValueError enter your name : "))
 print(name)
except Exception : 
 print("here a ValueError is occured")
#			(iii) program to illustrate IndexError
# how to handle index out of range error.
l=[1,2,3]
try:
 l1[3]
except Exception:
 print("here an Index error occured*")


#Q.6- Create a user-defined exception AgeTooSmallError() that warns the user when they have entered age less than 18.
#The code must keep taking input till the user enters the appropriate age number(less than 18). 

#solution 6.
class Age(Exception):
 pass 
 
 
while True:
 try:
  age=int(input("enter your age : "))
  if age>18:
   raise Age
  break  
 except Age:
     print("your age is larger than 18")
     print('')   
print("exact age")
