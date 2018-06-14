#TUPLE



#Q1.write a program to create a tuple with different data type and do the following operations :1.find the lenght of tuple.
t=(2,2,'b','g')
print("lenght of tuple with different data type")
print(len(t))

#Q2.find largest and smallest element of tuple.
tuple=(10,100,1000,10000)
print("the largest element of tuple is : ")
print(max(tuple))
print("the smallest element of tuple is : ")
print(min(tuple))

#Q3.write a program to find the product of all elements of a tuple.
tuple=(2,3,2)
mul=1
for x in tuple:
 mul=mul*x
print(mul) 



#SET



#Q1.create two sets using user defined value:
b1=set([])
b=int (input("enter number"))
a=int (input("enter second number"))
c=int (input("enter third number"))
b1.add(a)
b1.add(b)
b1.add(c)
print(b1)

b2=set([])
b=int (input("enter number"))
a=int (input("enter second number"))
c=int (input("enter third number"))
b2.add(a)
b2.add(b)
b2.add(c)
print(b2)

#(a)calculate difference between two sets.
print("s1=" ,b1)
print("s2" ,b2)
print("s3=",b1-b2)
print("s4=" ,b2-b1)

#(b)print the result of intersection of two sets.
g1=set([2,4,6,8])
g2=set([3,4,5,8,9])
print(g1&g2)


#DICTIONARY


#Q1.create a dictionary to store name and marks to 10 student by user input.
d={}
name=str(input("enter name of student"))
marks=int(input("enter marks of student"))
d[name]=marks
name=str(input("enter name of student"))
marks=int(input("enter marks of student"))
d[name]=marks
name=str(input("enter name of student"))
marks=int(input("enter marks of student"))
d[name]=marks
name=str(input("enter name of student"))
marks=int(input("enter marks of student"))
d[name]=marks
name=str(input("enter name of student"))
marks=int(input("enter marks of student"))
d[name]=marks
name=str(input("enter name of student"))
marks=int(input("enter marks of student"))
d[name]=marks
name=str(input("enter name of student"))
marks=int(input("enter marks of student"))
d[name]=marks
name=str(input("enter name of student"))
marks=int(input("enter marks of student"))
d[name]=marks
name=str(input("enter name of student"))
marks=int(input("enter marks of student"))
d[name]=marks
name=str(input("enter name of student"))
marks=int(input("enter marks of student"))
d[name]=marks
print(d)

#Q2.sort the dictionary created in previous question according to marks.
print(d)
values=list(d.values())
print(values)
values.sort()
print(values)

#Q3.count the number of occurrence of each letter in word "MISSISSIPPI".store count of every letter with the letter  in a dictionary.
l=list("mississippi")
d={}
d['m']=l.count('m')
d['i']=l.count('i')
d['s']=l.count('s')
d['p']=l.count('p')
print(d)

