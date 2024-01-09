from tkinter import *

expression = ""

def press(num):
    global expression
    expression += str(num)
    equation.set(expression)

def clear():
    global expression
    expression = ""
    equation.set("")

def delete():
    global expression
    expression = expression[:-1]
    equation.set(expression)

def equal():
    try:
        global expression
        total = str(eval(expression))
        equation.set(total)
        expression = ""
    except Exception as e:
        equation.set("ERROR")
        expression = ""

if __name__ == "__main__":
    root = Tk()
    root.geometry("340x300")
    root.title("My first calculator")
    equation = StringVar()
    entry = Entry(root, textvariable=equation, bg="black", fg="white",font="Arial 20 bold")
    entry.grid(columnspan=4, ipadx=10, ipady=10, row=0, column=0, pady=10)
    root.configure(background="black")

    button_width = 8
    button_height = 2  
    padx_value = 5  
    pady_value = 5

    buttons = [
        '7', '8', '9', '+',
        '4', '5', '6', '-',
        '1', '2', '3', '*',
        '0', 'DEL', '=', '/',
    ]

    for i in range(4):
        for j in range(4):
            text = buttons[i * 4 + j]
            if text == '=':
                Button(root, text=text, command=lambda: equal(), bg="yellow", fg="black", height=button_height, width=button_width).grid(row=i + 1, column=j, padx=padx_value, pady=pady_value)
            elif text == 'DEL':
                Button(root, text=text, command=lambda: delete(), bg="black", fg="white", height=button_height, width=button_width).grid(row=i + 1, column=j, padx=padx_value, pady=pady_value)
            else:
                Button(root, text=text, command=lambda t=text: press(t), bg="black", fg="white", height=button_height, width=button_width).grid(row=i + 1, column=j, padx=padx_value, pady=pady_value)

    root.mainloop()
