from tkinter import *

expression = ""
def press(num):
    global expression
    if num != "()":
        if num=="%":
            expression = expression + "/100"
        else:
            expression = expression + str(num)
    else:
        if expression == "":
            expression = expression + '('
        else:
            c_open = c_close = 0
            for i in expression:
                if i == '(':
                    c_open = c_open + 1
                elif i == ')':
                    c_close = c_close + 1
            if c_open > c_close:
                # Adds close bracket if there is already an unpaired open bracket in the expression
                expression = expression + ')'
            else:
                expression = expression + '('

    equation.set(expression)

def equalpress():
    try:

        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""

    except:

        equation.set(" Error ")
        expression = ""

def clear():
    global expression
    expression = ""
    equation.set("")

def backspace():
    global expression
    expression = expression[:-1]
    equation.set(expression)


gui = Tk()
gui.configure(background="dark blue")

gui.title("Simple Calculator")

equation = StringVar()

expression_field = Entry(gui, textvariable=equation, font="arial 16 bold")
expression_field.pack(side="top", ipadx=20, pady=10, fill="both", expand=True)

# First Row
R1=Frame(gui)
R1.pack(fill="both", side="top", expand=True)

clear = Button(R1, text='AC', fg='black', bg='light green',
                   command=clear, height=1, width=7)
clear.pack(fill="both", side="left", expand=True)

pop_expr = Button(R1, text="DEL", fg="black", bg="light green",
                      command=backspace, height=1, width=7)
pop_expr.pack(fill="both", side="left",expand=True)

brackets_button= Button(R1, text=" ( ) ", fg="black", bg="light blue",
                       command= lambda: press("()"), height=1, width=7)
brackets_button.pack(fill="both", side="left", expand=True)

divide = Button(R1, text=' / ', fg='black', bg='light blue',
                    command=lambda: press("/"), height=1, width=7)
divide.pack(fill="both", side="left", expand=True)

# Second Row
R2=Frame(gui)
R2.pack(fill="both", side="top", expand=True)

button7 = Button(R2, text=' 7 ', fg='black', bg='light blue',
                     command=lambda: press(7), height=1, width=7)
button7.pack(fill="both", side="left", expand=True)

button8 = Button(R2, text=' 8 ', fg='black', bg='light blue',
                     command=lambda: press(8), height=1, width=7)
button8.pack(fill="both", side="left", expand=True)

button9 = Button(R2, text=' 9 ', fg='black', bg='light blue',
                 command=lambda: press(9), height=1, width=7)
button9.pack(fill="both", side="left", expand=True)

multiply = Button(R2, text=' * ', fg='black', bg='light blue',
                      command=lambda: press("*"), height=1, width=7)
multiply.pack(fill="both", side="left", expand=True)

# Third Row
R3 = Frame(gui)
R3.pack(fill="both", side="top", expand=True)

button4 = Button(R3, text=' 4 ', fg='black', bg='light blue',
                     command=lambda: press(4), height=1, width=7)
button4.pack(fill="both", side="left", expand=True)

button5 = Button(R3, text=' 5 ', fg='black', bg='light blue',
                     command=lambda: press(5), height=1, width=7)
button5.pack(fill="both", side="left", expand=True)

button6 = Button(R3, text=' 6 ', fg='black', bg='light blue',
                     command=lambda: press(6), height=1, width=7)
button6.pack(fill="both", side="left", expand=True)

minus = Button(R3, text=' - ', fg='black', bg='light blue',
                   command=lambda: press("-"), height=1, width=7)
minus.pack(fill="both", side="left", expand=True)

# Fourth Row
R4 = Frame(gui)
R4.pack(fill="both", side="top", expand=True)

button1 = Button(R4, text=' 1 ', fg='black', bg='light blue',
                     command= lambda: press(1), height=1, width=7)
button1.pack(fill="both", side="left", expand=True)

button2 = Button(R4, text=' 2 ', fg='black', bg='light blue',
                     command=lambda: press(2), height=1, width=7)
button2.pack(fill="both", side="left", expand=True)

button3 = Button(R4, text=' 3 ', fg='black', bg='light blue',
                     command=lambda: press(3), height=1, width=7)
button3.pack(fill="both", side="left", expand=True)

plus = Button(R4, text='+', fg='black', bg='light blue',
              command=lambda: press("+"), height=1, width=7)
plus.pack(fill="both", side="left", expand=True)

# Fifth Row
R5 = Frame(gui)
R5.pack(fill="both", side="top", expand=True)

Decimal = Button(R5, text=' . ', fg='black', bg='light blue',
                     command=lambda: press('.'), height=1, width=7)
Decimal.pack(fill="both", side="left", expand=True)

button0 = Button(R5, text=' 0 ', fg='black', bg='light blue',
                 command=lambda: press(0), height=1, width=7)
button0.pack(fill="both", side="left", expand=True)

equal = Button(R5, text=" = ", fg='black', bg='light blue',
                     command=equalpress, height=1, width=7)
equal.pack(fill="both", side="left", expand=True)

percent_button = Button(R5, text=' % ', fg='black', bg='light blue',
                   command=lambda: press('%'), height=1, width=7)
percent_button.pack(fill="both", side="left", expand=True)


gui.mainloop()
