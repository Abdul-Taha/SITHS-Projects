from tkinter import ttk
from tkinter import *


root = Tk()
root.title("Conversion App")
root.geometry('325x100')
root.resizable(0,0)


metric_prefixes = {
    'Yotta': 1e24,
    'Zetta': 1e21,
    'Exa': 1e18,
    'Peta': 1e15,
    'Tera': 1e12,
    'Tiga': 1e9,
    'Mega': 1e6,
    'Kilo': 1e3,
    'Hecto': 1e2,
    'Deca': 1e1,
    '':1,
    'Deci': 1e-1,
    'Centi': 1e-2,
    'Milli': 1e-3,
    'Micro': 1e-6,
    'Nano': 1e-9,
    'Pico': 1e-12,
    'Femto': 1e-15,
    'Atto': 1e-18,
    'Zepto': 1e-21,
    'Yocto': 1e-24,
}


units = ['Meter', 'Gram', 'Second', 'Ampere', 'Kelvin', 'Mole', 'Candela']


input_frame = Frame(root)
input_frame.pack(side='left')


result_frame = Frame(root)
result_frame.pack(side='right')


def convert(*args):
    try:
        result.set('{:.2e}'.format((float(amount_var.get())*metric_prefixes[selected_prefix.get()])/metric_prefixes[selected_result_prefix.get()]))
    except:
        result.set("Input Not Number")


selected_prefix = StringVar()
selected_prefix.set(list(metric_prefixes.keys())[10])
prefix_menu = OptionMenu(input_frame,selected_prefix,*list(metric_prefixes.keys()))
prefix_menu.grid(row=1,column=0)
selected_prefix.trace('w',convert)


selected_unit = StringVar()
selected_unit.set(units[0])  
unit_menu = OptionMenu(input_frame,selected_unit,*units)
unit_menu.grid(row=1,column=1,sticky='w')


selected_result_prefix = StringVar()
selected_result_prefix.set(list(metric_prefixes.keys())[10])
result_prefix_menu = OptionMenu(result_frame,selected_result_prefix,*list(metric_prefixes.keys()))
result_prefix_menu.grid(row=1,column=0,sticky='e')
selected_result_prefix.trace('w',convert)


result_unit = Label(result_frame,text=selected_unit.get())
result_unit.grid(row=1,column=1,sticky='e')


filler = Label(result_frame,text='')
filler.grid(row=0,column=1,sticky='e')


result = StringVar()
result.set("Input Not Number")


result_Label = Label(text=f"Result: {result.get()}")
result_Label.place(relx=1.0, rely=0.5,y=-15, anchor='e')
result.trace('w',lambda *args:result_Label.config(text=f"Result: {result.get()}"))


selected_unit.trace('w',lambda *args:result_unit.config(text=selected_unit.get()))




amount_var = StringVar()
amount = Entry(input_frame,textvariable=amount_var)
amount.grid(row=0,column=0,columnspan=2,sticky='w')
amount_var.trace('w',convert)
               
root.mainloop()
