
# ASSIGNMENT-16

# DATABASES IN PYTHON



# Q.1- Create a database. Create the following tables:
# 1. Book
# 2. Titles
# 3. Publishers
# 4. Zipcodes
# 5. AuthorsTitles
# 6. Authors


import pymysql as py

# db=py.connect("localhost","root","root","library")
# cursor=db.cursor()
# qr="create table book(name char(20))"
# cursor.execute(qr)
# db.close()
#
# db=py.connect("localhost","root","root","library")
# cursor=db.cursor()
# qr="create table titles(name char(20))"
# cursor.execute(qr)
# db.close()
#
# db=py.connect("localhost","root","root","library")
# cursor=db.cursor()
# qr="create table publishers(name char(20))"
# cursor.execute(qr)
# db.close()
#
# db=py.connect("localhost","root","root","library")
# cursor=db.cursor()
# qr="create table zipcode (name char(20))"
# cursor.execute(qr)
# db.close()
#
# db=py.connect("localhost","root","root","library")
# cursor=db.cursor()
# qr="create table Authortitle(name char(20))"
# cursor.execute(qr)
# db.close()
#
# db=py.connect("localhost","root","root","library")
# cursor=db.cursor()
# qr="create table Authors(name char(20))"
# cursor.execute(qr)
# db.close()

#output question.1 :
# +-------------------+
# | Tables_in_library |
# +-------------------+
# | book              |
# +-------------------+
# 1 row in set (0.00 sec)
#
# mysql> show tables;
# +-------------------+
# | Tables_in_library |
# +-------------------+
# | authors           |
# | authortitle       |
# | book              |
# | publishers        |
# | titles            |
# | zipcode           |
# +-------------------+






# Q.2- Insert values in the tables.

db=py.connect("localhost",'root','root','Library')
point=db.cursor()
for i in range(0,6):
 try:
   cmd=input("enter SQL Querry to insert values in created table:-")
   point.execute(cmd)
   db.commit()
 except:
    db.rollback()
db.close()

#output:-

# mysql> select * from book;
# +------+
# | name |
# +------+
# | java |
# | C++  |
# +------+
# 2 rows in set (0.00 sec)
#
# mysql> select * from titles;
# +--------------+
# | names        |
# +--------------+
# | play java    |
# | play classes |
# +--------------+
# 2 rows in set (0.00 sec)
#
# mysql> select * from publishers;
# +------------------+
# | name             |
# +------------------+
# | jai ma pulishers |
# | bharat publish   |
# +------------------+
# 2 rows in set (0.00 sec)
#
# mysql> select * from zipcodes;
# +----------+
# | name     |
# +----------+
# | abdtjg   |
# | bhdrysoo |
# +----------+
# 2 rows in set (0.00 sec)
#
# mysql> select * from authorstitles;
# +-----------+
# | name      |
# +-----------+
# | play java |
# | play oops |
# +-----------+
# 2 rows in set (0.00 sec)
#
# mysql> select * from authors;
# +--------------+
# | name         |
# +--------------+
# | hary         |
# | bala goswami |
# +--------------+
# 2 rows in set (0.00 sec)



# Q.3- Update any values in any of the tables. Print the original and updated values.

db=py.connect("localhost",'root','root','Library')
point=db.cursor()
for i in range(0,6):
 try:
   cmd=input("enter SQL Querry to update values in created table:-")
   point.execute(cmd)
   db.commit()
 except:
    db.rollback()
db.close()

#output:-
# mysql> select * from book;
# +------+
# | name |
# +------+
# | java |
# | C++  |
# +------+
# 2 rows in set (0.00 sec)

#  updated:-
# mysql> select * from book;
# +----------+
# | name     |
# +----------+
# | database |
# | C++      |
# +----------+
# 2 rows in set (0.00 sec)