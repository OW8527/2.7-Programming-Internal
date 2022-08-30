

import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
import pandas 
df = pandas.read_csv('Cleaned_Laptop_data.csv')
print(df)

root = tk.Tk()

#Changing the background colour of the window - if want to use hex make sure # is at the frount and its in the ""
root.configure(bg="#F6F8FF")

# root window
root.geometry('400x320')
root.resizable(False, False)
root.title('Buget Laptop Calculator')


def show_selected_size():
    showinfo(
        title='Result',
        message=selected_size.get()
    )


selected_size = tk.StringVar()
sizes = (('Apple', 'For computer type you have selected Apple'),
         ('Hp', 'For computer type you have selected HP'),
         ('Acer', 'For computer type you have selected Acer'),
         ('Dell', 'For computer type you have selected Dell'),
         ('Lenovo', 'For computer type you have selected Lenvo'))
         

# label on top of section buttons
label = ttk.Label(text="What Computer type would you prefer?")
label.pack(fill='x', padx=5, pady=5)

# radio buttons
for size in sizes:
    r = ttk.Radiobutton(
        root,
        text=size[0],
        value=size[1],
        variable=selected_size
    )
    r.pack(fill='x', padx=5, pady=5)

# button
button = ttk.Button(
    root,
    text="Get Selected Size",
    command=show_selected_size)

button.pack(fill='x', padx=5, pady=5)


root.mainloop()


'''
import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name
from datetime import datetime

root = tk.Tk()

# config the root window
root.geometry('300x200')
root.resizable(False, False)
root.title('Combobox Widget')

# label
label = ttk.Label(text="Please select a month:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_month = tk.StringVar()
month_cb = ttk.Combobox(root, textvariable=selected_month)

# get first 3 letters of every month name
month_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
month_cb['state'] = 'readonly'

# place the widget
month_cb.pack(fill=tk.X, padx=5, pady=5)


# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(
        title='Result',
        message=f'You selected {selected_month.get()}!'
    )


month_cb.bind('<<ComboboxSelected>>', month_changed)

# set the current month
current_month = datetime.now().strftime('%b')
month_cb.set(current_month)

root.mainloop()
'''

''' First Attempt
from optparse import Option
from ssl import Options
from tkinter import *


top = Tk()
#Changing the background colour of the window - if want to use hex make sure # is at the frount and its in the ""
top.configure(bg="#F6F8FF")

#Changing the title of the window	
top.title("Budget")

#how you change the size of the window
top.geometry("450x600")


# the label for user_name
user_name = Label(top,
				text = "Enter Username").place(x = 60,
										y = 100)
	
# the label for user_password
user_password = Label(top,
					text = "Enter Password").place(x = 60,
											y = 140)
	
submit_button = Button(top,
					text = "Click here").place(x = 150,
											y = 270)
	
user_name_input_area = Entry(top,
							width = 30).place(x = 155,
											y = 100)
	
user_password_entry_area = Entry(top,
								width = 30).place(x = 155,
												y = 140)

# Change the label text
def show():
    label.config( text = clicked.get() )
  
# Dropdown menu options
options = [
    "Monday",
    "Tuesday",
    "Wednesday",
    "Thursday",
    "Friday",
    "Saturday",
    "Sunday"
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Monday" )
  
# Create Dropdown menu
drop = OptionMenu( top , clicked , *options )
drop.pack()
  
# Create button, it will change label text
button = Button( top , text = "click Me" , command = show ).pack()
  
# Create Label
label = Label( top , text = " " )
label.pack()





#Executes the tkinter
top.mainloop()
'''