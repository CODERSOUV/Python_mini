from tkinter import *

expression = ""

def press(num):
    global expression
    if num == '%':
        try:
            expression = str(eval(expression) / 100)
        except Exception as e:
            expression = "ERROR"
    if expression == "0":
        expression = str(num)
    else:
        expression += str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("0")

def equal():
    try:
        global expression
        if expression.strip():
            total = str(eval(expression))
            equation.set(total)
            expression = ""
        else:
            equation.set("ERROR")
            expression = ""
    except Exception as e:
        equation.set("ERROR")
        expression = ""

def delete():
    global expression
    expression = expression[:-1]
    if not expression:
        equation.set("0")
    else:
        equation.set(expression)

def square_root():
    global expression
    try:
        expression = str(eval(expression) ** 0.5)
        equation.set(expression)
    except Exception as e:
        equation.set("ERROR")
        expression = "0"

if __name__ == "__main__":
    root = Tk()
    root.geometry("262x260")
    root.title("My first calculator")
    equation = StringVar()
    entry = Entry(root, textvariable=equation, bg="lightgreen", fg="black", font="Arial 15 bold")
    equation.set('0')
    entry.grid(columnspan=6, ipadx=15, ipady=10, row=0, column=0, pady=5)
    root.configure(background="black")

    Button(root, text="AC", command=clear, bg="lightgreen", fg="black", height=2, width=8).grid(row=1, column=0, padx=0, pady=0)
    Button(root, text="%", command=lambda: press('%'), bg="lightblue", fg="black", height=2, width=8).grid(row=1, column=1, padx=0, pady=0)
    Button(root, text="√", command=square_root, bg="lightblue", fg="black", height=2, width=8).grid(row=1, column=2, padx=0, pady=0)
    Button(root, text="/", command=lambda: press('/'), bg="lightblue", fg="black", height=2, width=8).grid(row=1, column=3, padx=0, pady=0)
    Button(root, text="7", command=lambda: press(7), bg="lightblue", fg="black", height=2, width=8).grid(row=2, column=0, padx=0, pady=0)
    Button(root, text="8", command=lambda: press(8), bg="lightblue", fg="black", height=2, width=8).grid(row=2, column=1, padx=0, pady=0)
    Button(root, text="9", command=lambda: press(9), bg="lightblue", fg="black", height=2, width=8).grid(row=2, column=2, padx=0, pady=0)
    Button(root, text="*", command=lambda: press('*'), bg="lightblue", fg="black", height=2, width=8).grid(row=2, column=3, padx=0, pady=0)
    Button(root, text="4", command=lambda: press(4), bg="lightblue", fg="black", height=2, width=8).grid(row=3, column=0, padx=0, pady=0)
    Button(root, text="5", command=lambda: press(5), bg="lightblue", fg="black", height=2, width=8).grid(row=3, column=1, padx=0, pady=0)
    Button(root, text="6", command=lambda: press(6), bg="lightblue", fg="black", height=2, width=8).grid(row=3, column=2, padx=0, pady=0)
    Button(root, text="-", command=lambda: press('-'), bg="lightblue", fg="black", height=2, width=8).grid(row=3, column=3, padx=0, pady=0)
    Button(root, text="1", command=lambda: press(1), bg="lightblue", fg="black", height=2, width=8).grid(row=4, column=0, padx=0, pady=0)
    Button(root, text="2", command=lambda: press(2), bg="lightblue", fg="black", height=2, width=8).grid(row=4, column=1, padx=0, pady=0)
    Button(root, text="3", command=lambda: press(3), bg="lightblue", fg="black", height=2, width=8).grid(row=4, column=2, padx=0, pady=0)
    Button(root, text="+", command=lambda: press('+'), bg="lightblue", fg="black", height=2, width=8).grid(row=4, column=3, padx=0, pady=0)
    Button(root, text="0", command=lambda: press(0), bg="lightblue", fg="black", height=2, width=8).grid(row=5, column=0, padx=0, pady=0)
    Button(root, text=".", command=lambda: press('.'), bg="lightblue", fg="black", height=2, width=8).grid(row=5, column=1, padx=0, pady=0)
    Button(root, text="DEL", command=lambda: delete(), bg="lightgreen", fg="black", height=2, width=8).grid(row=5, column=2, padx=0, pady=0)
    Button(root, text="=", command=lambda: equal(), bg="lightgreen", fg="black", height=2, width=8).grid(row=5, column=3, padx=0, pady=0)

    root.mainloop()
