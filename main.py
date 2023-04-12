import tkinter
from PASS import Pass
from tkinter import *
import tkinter.messagebox

root = Tk()

root.title("First try")
root.config(bg="black")

number_required = 0
symbols_required = 0
caps_required = 0
lower_required = 0


def generate_N_P():
    pass_generator.delete(0, END)
    number_required = amount_numbers_entry.get()
    symbols_required = amount_symbols_entry.get()
    caps_required = caps_label_entry.get()
    lower_required = lower_entry.get()
    if not number_required.isdigit() or not symbols_required.isdigit() or not caps_required.isdigit() or not lower_required.isdigit():
        tkinter.messagebox.showerror("Error", "Type only number please")
    else:
        data = Pass(number_required, symbols_required, caps_required, lower_required)
        pass_generator.insert(0, str(data.generate_N()))


# INSIDE ROOT FIRST GRID
frame = Frame(root)
frame.config()
frame.grid(column=0, row=0)

tittle = Label(frame, text='PASSWORD GENERATOR', width=53)
tittle.pack()

# INSIDE ROOT SECOND GRID
frame2 = Frame(root)
frame2.config()
frame2.grid(column=0, row=1)

pass_name = Label(frame2, text='New Password')
pass_name.pack(side=LEFT)

pass_generator = Entry(frame2, width=40)
pass_generator.pack(side=RIGHT)

# INSIDE ROOT THIRD GRID
frame3 = Frame(root)
frame3.grid(column=0, row=2)

amount_numbers = Label(frame3, text='Numbers')
amount_numbers.pack(side=LEFT)
amount_numbers_entry = Entry(frame3, width=5)
amount_numbers_entry.pack(side=LEFT)

amount_symbols = Label(frame3, text='Symbols')
amount_symbols.pack(side=LEFT)
amount_symbols_entry = Entry(frame3, width=5)
amount_symbols_entry.pack(side=LEFT)

caps_label = Label(frame3, text='Caps')
caps_label.pack(side=LEFT)
caps_label_entry = Entry(frame3, width=5)
caps_label_entry.pack(side=LEFT)

lower_label = Label(frame3, text='Lower cases')
lower_label.pack(side=LEFT)
lower_entry = Entry(frame3, width=5)
lower_entry.pack(side=LEFT)

# INSIDE FOURTH GRID
frame4 = Frame(root)
frame4.grid(column=0, row=3)

generate_pass = Button(frame4, text='Generate', width=50, command=generate_N_P)
generate_pass.pack()

root.mainloop()
