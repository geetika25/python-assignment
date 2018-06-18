#decision control statement.



#Q1.take a input from user and check wheather it is leap year or not.
year = int(input("Enter a year: "))
if (year % 4) == 0:
   if (year % 100) == 0:
       if (year % 400) == 0:
           print("leap year")
       else:
           print(" not a leap year")
   else:
       print("not a leap year")
else:
   print(" not a leap year")
   


   #Q2.check the dimensions of square and rectangle.
a=int (input("enter the lenght of shape"))
b=int (input("enter the lenght of shape"))
c=int (input("enter the width of shape"))
d=int (input("enter the width of shape"))
if a==b==c==d:
 print("square")
elif a==b and c==d:
 print("rectangle")
else :
 print("not square & not rectangle") 
 
 
#Q3.determine the oldest and the youngest people.
a=int(input("enter your Age"))
if a<50:
 print("young")
if a>50:
 print("older")
 
 
 
 #Q4.write an if statement to lets competitor know which of these prices they won.
s=int(input("enter your score"))
if s<100:
 print("congratulation!!you won the price j6 infinity samsung set")
elif s==100:
 print("congratulation!!!you won the price of python programming books ")
else: 
 print("congratulations !!!! you won the trip of USA") 
 

#Q5.print the total cost after getting discount.
price=int(input("enter you prise :  "))
print("price=  ",price)
dis=int(input("enter the discount"))
print("discount:  ",dis)
discount=price * dis//100
total=price-discount
print("total amount after discount :  ",total)

 