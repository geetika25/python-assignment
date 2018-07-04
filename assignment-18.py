#ASSIGNMENT-18(GUI 2)
#Q1. Create a dict with name and mobile number.Define a GUI interface using tkinter and pack the label and create a scrollbar to scroll the list of keys in the dictionary.
import tkinter
from tkinter import *
root=Tk()

root.title("dictionary")
def show():
    k=mylist.get(ACTIVE)
    v=dic[k]
    label.config(text=k)
    label_1.config(text=v)
top_frame=Frame(root)
top_frame.pack()
button=Button(top_frame,text='save',bg='powder blue',command=show)
button.pack()
label=Label(top_frame,text='Name of student',bg='pink')
label.pack()
label_1=Label(top_frame,text='Contact',bg='pink')
label_1.pack()
dic={'Geet':'9034621663','Bhuv':'895038221','Bhan':'903842922','Tann':'897688688','kirt':'736354627','ghee':'899899898','bhuf':'890-90909','gtee':'88989838383893','buhu':'38948348984398','heye':'83939393993','geee':'854954884','huds':'345678'}
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
root.geometry("500x500")
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for k in dic.keys():
            mylist.insert(END,k)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)

root.mainloop()
#Q2. In the same tkinter file as created above, create a function to insert items into the dictionary.

root=Tk()

root.title("dictionary")
def insert():
    k=e1.get()
    v=e2.get()
    dic[k]=v
    mylist.insert(END,k)
    print(dic)

top_frame=Frame(root)
top_frame.pack()
button=Button(top_frame,text='Enter',bg='powder blue',command=insert)
button.pack()
label=Label(top_frame,text='Name of student',bg='pink')

label.pack()
e1=Entry(top_frame)
e1.pack()
label_1=Label(top_frame,text='Contact',bg='pink')
label_1.pack()
e2=Entry(top_frame)
e2.pack()
dic={'Geet':'9034621663','Bhuv':'895038221','Bhan':'903842922','Tann':'897688688','kirt':'736354627','ghee':'899899898','bhuf':'890-90909','gtee':'88989838383893','buhu':'38948348984398','heye':'83939393993','geee':'854954884','huds':'345678'}
scrollbar=Scrollbar(root)
scrollbar.pack(side=RIGHT,fill=Y)
root.geometry("500x500")
mylist=Listbox(root,yscrollcommand=scrollbar.set)
for k in dic.keys():
            mylist.insert(END,k)
mylist.pack(side=LEFT,fill=BOTH)
scrollbar.config(command=mylist.yview)

root.mainloop()