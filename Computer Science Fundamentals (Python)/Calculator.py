from tkinter import *


r = Tk()
r.geometry("250x300")
r.resizable(0,0)
r.grid()
r.title("Calculator")
r.columnconfigure(0, weight=1)


display = Frame(r)
display.grid(row=0, column=0, columnspan=4, sticky='e')


optext = StringVar()
shwn_optext = StringVar()
op = Label(display, anchor=NE, font=("Cascadia Mono ExtraLight",35), justify="right", textvariable=shwn_optext)
op.pack(anchor=NE, fill='x')


def op_change(*args):
    shwn_optext.set(optext.get())


def shwnopchange(*args):
    if optext.get() != "":
        if len(str(optext.get())) > 8:
            shwn_optext.set(f'{float(optext.get()):.2e}')


optext.trace("w", op_change)
shwn_optext.trace("w", shwnopchange)


buttons = [["%", "CE", "C", "⌫"],
           ["√", "x²", "1/x",["÷","/"]],
           ["7", "8" , "9",["x","*"]],
           ["4", "5" , "6",["-","-"]],
           ["1", "2" , "3",["+","+"],],
           ["±", "0" , ".", "=" ],]


def negate(*args):
    if optext.get() != "":
        if "-" == optext.get()[0]:
            optext.set(optext.get()[1:])
        else:
            optext.set("-"+optext.get())


def op(text):
    global prev_num, operation
    if shwn_optext.get() != "":
        prev_num = optext.get()
        operation = text
        optext.set("")


def equal(*args):
    try:
        global operation
        if operation != "":
            result = str(eval(f"{prev_num} {operation} {optext.get()}"))  
            optext.set(result)
            operation = ""
    except:
        pass


def clear(*args):
    optext.set("")
    shwn_optext.set("")


def clear_entry(*args):
    optext.set("")


def square(*args):
    if optext.get() != "":
        result = str(float(optext.get()) ** 2)
        optext.set(result)


def inverse(*args):
    if optext.get() != "":
        result = str(1 / float(optext.get()))
        optext.set(result)


def percentage(*args):
    if optext.get() != "":
        result = str(float(optext.get()) / 100)
        optext.set(result)


def square_root(*args):
    if optext.get() != "":
        result = str(float(optext.get()) ** 0.5)
        optext.set(result)


for row in range(len(buttons)):
    for column in range(len(buttons[row])):
        r.rowconfigure(row+1, weight=1)
        r.columnconfigure(column, weight=1)
        if row == 0 and buttons[row][column] == "CE":
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column],command=clear_entry).grid(row=row+1, column=column, sticky=W)
        elif row == 0 and buttons[row][column] == "C":
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column],command=clear).grid(row=row+1, column=column, sticky=W)
        elif row == 0 and buttons[row][column] == "⌫":
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column],command=lambda: optext.set(optext.get()[:-1])).grid(row=row+1, column=column, sticky=W)
        elif buttons[row][column] == "=":
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column],command=equal).grid(row=row+1, column=column, rowspan=2, sticky=N+S+E+W)
        elif buttons[row][column] in [["-","-"],["+","+"],["x","*"],["÷","/"]]:
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column][0],command=lambda text=buttons[row][column][1]: op(text)).grid(row=row+1, column=column, sticky=N+S+E+W)
        elif buttons[row][column] == "±":
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column],command=negate).grid(row=row+1, column=column, sticky=N+S+E+W)
        elif buttons[row][column] == "x²":
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column],command=square).grid(row=row+1, column=column, sticky=N+S+E+W)
        elif buttons[row][column] == "1/x":
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column],command=inverse).grid(row=row+1, column=column, sticky=N+S+E+W)
        elif buttons[row][column] == "√":
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column],command=square_root).grid(row=row+1, column=column, sticky=N+S+E+W)
        elif buttons[row][column] == "%":
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column],command=percentage).grid(row=row+1, column=column, sticky=N+S+E+W)
        else:
            Button(r, width=10,font=("Cascadia Mono ExtraLight",23),height=10,text=buttons[row][column],command=lambda text=buttons[row][column]: optext.set(optext.get()+text)).grid(row=row+1, column=column, sticky=N+S+E+W)


r.mainloop()

