#Q1.create a list with user defined inputs.
# program for user defined inputs.
print(" write famous profiles in field of cs.")
l=[]
a= (input("enter first name of our list"))
b= (input("enter second name of our list"))
c= (input("enter third name of our list"))
l.append(a)
l.append(b)
l.append(c)
print(l)
#program for defined input.
pl=["java","python","c","c++","javascript"]
print(pl)
fees= [5000,6000,3000,2000,4000]
print(fees)

#Q2.addd the following list to above created list:['google",apple","facebook","microsoft","tesla"]
c=["google","apple","facebook","microsoft","tesla"]
print(pl.extend(c))
print(pl)

#Q3.count the number of time an objec coccurs in a list.
list=["g","e","e","t","i","k","a"]
print(list.count("e"))

#Q4.create a list with numbers and sort it in ascending order.
list=[10,2,4,5,12,7,3,1,6,]
print(list.sort())
print(list)

#Q5.given are two one dimentional array A and B which are sorted in ascending order.write a program to merge them into a single sorted array C that contain every item from arrays A and B,in ascending order list. 
Array_A=[10,8,6,4,2]
Array_B=[9,7,5,3,1]
print(Array_A.sort())
print(Array_A)
print(Array_B.sort())
print(Array_B)
c=[]
c.extend(Array_A)
c.extend(Array_B)
print(c)
c.sort()
print(c)

#Q6.implement a stack and queue using lists.
#impliment stack using list.program to print list of stack to console.
stack=[]
stack.append("acad")
stack.append("view")
stack.append("python")
stack.append("fundamentals")
print("insertion in list") 
print(stack)
stack.pop()
print("after poping")
print(stack)

#impliementation queue using list.program to print list of queue to console.
queue=[]
queue.append("sunday")
queue.append("monday")
queue.append("tuesday")
queue.append("wednesday")
print("insertion from one end")
print(queue)
del queue[0]
print("poping from another end")
print(queue)

#Q7count even and odd numbers in that list.
list=[1,2,3,4,5,6,7,8,9,10]
even_no=0
odd_no=0
for x in list:
 if x%2==0:
  even_no=even_no + 1
 else:
  odd_no=odd_no + 1
print("even no in list: ",even_no)
print("odd no in list: ",odd_no)  
 
