# Task 2:-
# Simple Calculator With Basic AITHMETIC Operations(i.e +,-,*,/,%):-
# Program Implementation:-
from tkinter import Tk, Entry, Button, StringVar

class Calculator:
    def __init__(self, master):
        master.title("Simple Calculator")
        # Width: 356 & Height: 421
        master.geometry('356x421+0+0')  # Corrected geometry format (width x height)
        master.config(bg='black')
        master.resizable(True, True)

        self.equation = StringVar() # it's a Stringvariable
        self.entry_value = ''
        Entry(width=17, bg='#ccddff', font=('Arial Bold', 28), textvariable=self.equation).place(x=0, y=0)

        # Note:- At below ARITHMETIC Operations & Brackets(i.e ( & )) are in Lightpink colour:-
        # Remaining Number(i.e 0,1,2,3,4,5,6,7,8,9) Buttons & CLEAR(i.e C) Button are in White colour:-
        # while "EQUAl to"(i.e =) Button is in Lightblue colour:-

        Button(width=10,height=3,text='(',relief='flat',bg='lightpink',command=lambda:self.show('(')).place(x=0,y=50)
        Button(width=10,height=3,text=')',relief='flat',bg='lightpink',command=lambda:self.show(')')).place(x=90,y=50)
        Button(width=10,height=3,text='%',relief='flat',bg='lightpink',command=lambda:self.show('%')).place(x=180,y=50)
        Button(width=10,height=3,text='1',relief='flat',bg='white',command=lambda:self.show('1')).place(x=0,y=125)
        Button(width=10,height=3,text='2',relief='flat',bg='white',command=lambda:self.show('2')).place(x=90,y=125)
        Button(width=10,height=3,text='3',relief='flat',bg='white',command=lambda:self.show('3')).place(x=180,y=125)
        Button(width=10,height=3,text='4',relief='flat',bg='white',command=lambda:self.show('4')).place(x=0,y=200)
        Button(width=10,height=3,text='5',relief='flat',bg='white',command=lambda:self.show('5')).place(x=90,y=200)
        Button(width=10,height=3,text='6',relief='flat',bg='white',command=lambda:self.show('6')).place(x=180,y=200)
        Button(width=10,height=3,text='7',relief='flat',bg='white',command=lambda:self.show('7')).place(x=0,y=275)
        Button(width=10,height=3,text='8',relief='flat',bg='white',command=lambda:self.show('8')).place(x=180,y=275)
        Button(width=10,height=3,text='9',relief='flat',bg='white',command=lambda:self.show('9')).place(x=90,y=275)
        Button(width=10,height=3,text='0',relief='flat',bg='white',command=lambda:self.show('0')).place(x=90,y=350)
        Button(width=10,height=3,text='.',relief='flat',bg='white',command=lambda:self.show('.')).place(x=180,y=350)
        Button(width=10,height=3,text='+',relief='flat',bg='lightpink',command=lambda:self.show('+')).place(x=270,y=275)
        Button(width=10,height=3,text='-',relief='flat',bg='lightpink',command=lambda:self.show('-')).place(x=270,y=200)
        Button(width=10,height=3,text='/',relief='flat',bg='lightpink',command=lambda:self.show('/')).place(x=270,y=50)
        Button(width=10,height=3,text='*',relief='flat',bg='lightpink',command=lambda:self.show('*')).place(x=270,y=125)
        Button(width=10,height=3,text='=',relief='flat',bg='lightblue',command=self.solve).place(x=270,y=350)
        Button(width=10,height=3,text='C',relief='flat',command=self.clear).place(x=0, y=350)

    def show(self, value):
        self.entry_value += str(value)
        self.equation.set(self.entry_value)

    def clear(self):
        self.entry_value = ''
        self.equation.set(self.entry_value)

    def solve(self):
        try:
            result = eval(self.entry_value)
            self.equation.set(result)
        except Exception as e:
            self.equation.set("Error")

root = Tk()
calculator = Calculator(root)
root.mainloop()
