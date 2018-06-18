#ASSIGNMENT-7

#FUNCTIONS

#Let’s create methods for Python. 


#QUESTION: 1  


#Create a Function To Calculate Area of a circle by taking radius from user.



radius=float(input("enter any no (radius)to calculate area of a circle: "))
def area():
 PI=3.14
 area=PI*radius*radius
 print("the area of a circle is : ",area)
area()




#QUESTION: 2  

#  Write a function “perfect()” that determines if parameter number is a perfect number.
#  Use this function in a program that determines and prints all the perfect numbers between 1 and 1000. 
#  [An integer number is said to be “perfect number” if its factors, including 1(but not the number itself), sum to the number. E.g., 6 is a perfect number because 6=1+2+3].

def perfect(n):
  sum=0
  for i in range(1,n):
   if n%i==0:
    sum=sum + i
  if sum==n:
   return True
  else:
   return False
for i in range (1,1001):
 if perfect(i):
   print(i) 
   
 
#QUESTION: 3  



#Print multiplication table of 12 using recursion.


def table(n,i):
 print(n ,"x" ,i, "=", n*i)
 i=i+1
 if i<=10:
  table(n,i)
table(12,1)
 

#QUESTION: 4  


#Write a function to calculate power of a number raised to other ( a^b ) using recursion.



n1=int(input("enter any number : "))
n2=int(input("power of number : "))
def power(a,b):
 if b==1:
  return a
 else:
  pow=a*power(a,b-1)
  return pow
p=power(n1,n2)
print("power : ",p)



#QUESTION: 5  


#Write a function to find factorial of a number but also store the factorials calculated in a dictionary.



n=int(input("enter any number : "))
def rec(x):
 if (x==1 or x==0):
  return 1
 else:
   f=x * rec(x-1)
   return f
fact=rec(n)   
print(fact)
dic={}
dic[n]=fact
print(dic)


