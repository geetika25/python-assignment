# CLASS 4
# ASSIGNMENT - PANDAS


#Q.1 - Create a dataframe with your name , age , mail id and phone number and add your friends’s information to the same.
import pandas as pd
data={"Name":["Geetika"],
           "Age":["20"],
           "Mail id":["geetika2598@gmail.com"]}
df=pd.DataFrame(data)
print(df)
df2={"Name":"Bhuvnesh",
           "Age":"20",
           "Mail id":"Bhuvnesh2598@gmail.com"}
df=df.append(df2,ignore_index=True)
print("\n",df)

# Q.2 - Download the dataset from this link ,
# Click Here
# Import the data and print the following :
# a.) First 5 rows of Dataframe
# b.) First 10 rows of the Dataframe
# c.) find basic statistics on the particular dataset.
# d.) Find the last 5 rows of the dataframe
# e.) Extract the 2nd column and find basic statistics on it.

import pandas as pd
df=pd.read_csv("weather.csv")
print(df)

print("a.) First 5 rows of Dataframe : ",df.head(5))

print("b.) First 10 rows of the Dataframe",df[0:10])

print("c.) find basic statistics on the particular dataset.",df.describe())

print("d.) Find the last 5 rows of the dataframe",df.tail(5))
p=df["Location"]
print("e.) Extract the 2nd column and find basic statistics on it.",p.describe())
