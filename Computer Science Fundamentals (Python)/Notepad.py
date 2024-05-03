from tkinter import *
from tkinter import font, filedialog
import os
from random import randint

#This is a Joke Program

root = Tk()
root.geometry("300x300")
root.title("Bad Notepad")
root.grid

def open_file(*args):
    filepath = filedialog.askopenfile(initialdir=os.getcwd(), title="Open", filetypes=(("Text Document","*.txt"), ("All Files","*.*")))
    if filepath is not None:
        with open(filepath.name, 'r') as f:
            text.delete('1.0', END)
            text.insert(END, f.read())




def save_file(*args):
    filepath = filedialog.asksaveasfile(initialdir=os.getcwd(), title="Save As", defaultextension=".txt", filetypes=(("Text Document","*.txt"), ("All Files","*.*")))
    if filepath is not None:
        with open(filepath.name, 'w') as f:
            f.write(text.get('1.0', END))


text=Text(root, wrap="none")
text.pack(expand = True, fill = "both")


menubar = Menu(root)
file_menu = Menu(menubar,tearoff=0)
font_menu = Menu(menubar,tearoff=0)
f=StringVar()
f.set("Arial")
size=IntVar()
size.set(8)
size.trace("w",lambda *args: text.config(font=(f.get(),size.get())))
f.trace("w",lambda *args: text.config(font=(f.get(),size.get())))
size_menu = Menu(menubar,tearoff=0)


menubar.add_cascade(label="File",menu=file_menu)
menubar.add_cascade(label="Font",menu=font_menu)
menubar.add_cascade(label="Size",menu=size_menu)




file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save",command=save_file)



#Randomizes Location of Dropdown Menu
for i in font.families():
    font_menu.add_command(label=i,command=lambda font=i: [f.set(font),font_menu.post(randint(0, root.winfo_screenwidth()),randint(0, root.winfo_screenheight()))])

for i in range(1,201):
    size_menu.add_command(label=str(i),command=lambda s=i: [size.set(s),size_menu.post(randint(0, root.winfo_screenwidth()),randint(0, root.winfo_screenheight()))])




root.config(menu=menubar)
root.mainloop()

