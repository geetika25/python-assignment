#ASSIGNMENT-17(GUI)


#Q1. Write a python program using tkinter interface to write Hello World and a exit button that closes the interface.

import tkinter
import tkinter
from tkinter import*

window=Tk()
window.title("welcome screen")
label=Label(window,text='Hello world!!\nWelcome to welcome screen !! this is a GUI graphical user interface\nsuch a better way to interact with users\nGUI Python offers multiple options for developing GUI (Graphical User Interface). \nOut of all the GUI methods, tkinter is most commonly used method. \nIt is a standard Python interface to the Tk GUI toolkit shipped with Python. \nPython with tkinter outputs the fastest and easiest way to create the GUI applications. \nCreating a GUI using tkinter is an easy task.',bg='pink',fg='black')
label.pack(fill=X)
button=Button(window,text='Exit',bg='pink',fg='black',command=exit,)
button.pack(fill=X,side=BOTTOM)
window.mainloop()

#Q2. Write a python program to in the same interface as above and create a action when the button is click it will display some text.



#import everything from tkinter
from tkinter import*

display=Tk()
def show():
    print(" She is a preety girl !! student of computer science department GNI(2nd year)")
display.title("lets perform a action")
button_1=Button(display,text='Geetika',bg='pink',fg='black',command=show)
button_1.pack(fill=X)

def show():
    print(" cool boy !! student of computer science department GNI(2nd year)")
display.title("lets perform a action")
button_2=Button(display,text='Bhuvnesh',bg='powder blue',fg='black',command=show)
button_2.pack(fill=X)
display.mainloop()


#Q3. Create a frame using tkinter with any label text and two buttons.One to exit and other to change the label to some other text.

from tkinter import *

def display():
       label.config(text="it will change")

prinnt=Tk()
label=Label(prinnt,text='start')
label.grid(row=0)
button_1=Button(prinnt,text='exit',command=quit).grid(row=1)
button_2=Button(prinnt,text='change',command=display).grid(row=2)
prinnt.mainloop()

#Q4. Write a python program using tkinter interface to take an input in the GUI program and print it.
from tkinter import *

def display():
    print(enter_1.get())
    print(enter_2.get())
    label3.config(text=enter_2.get())
prinnt=Tk()
label_1=Label(prinnt,text='name',bg='white',fg='black').grid(row=0)
label_2=Label(prinnt,text='Age',bg='white',fg='black').grid(row=1)
enter_1=Entry(prinnt)
enter_2=Entry(prinnt)
enter_1.grid(row=0,column=1)
enter_2.grid(row=1,column=1)
button_1=Button(prinnt,text='exit',command=quit).grid()
button_2=Button(prinnt,text='save',command=display).grid()
label3 = Label(prinnt, text='text will appear here')
label3.grid(row=2, column=1)
prinnt.mainloop()