import tkinter as tk
from tkinter import ttk
from tkinter.messagebox import showinfo
from calendar import month_name

root = tk.Tk()

# config the root window
root.geometry('600x400')
root.resizable(False, False)
root.title('Buget Laptop Calculator')

# purpose needed------------------------------------------------------------------------------------------

# label
label = ttk.Label(text="Please select the main reason or purpose of the laptop:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
purpose = tk.StringVar()
purpose_cb = ttk.Combobox(root, textvariable=purpose)

# get first 3 letters of every month name
purpose_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
purpose_cb['state'] = 'readonly'

# place the widget
purpose_cb.pack(fill=tk.X, padx=5, pady=5)


'''
# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(title='Result', message=f'You selected {selected_month.get()}!')


month_cb.bind('<<ComboboxSelected>>', month_changed)
'''

#operating system ---------------------------------------------

# label
label = ttk.Label(text="Please select a operating system that you would like for the laptop:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
operating_system = tk.StringVar()
operating_system_cb = ttk.Combobox(root, textvariable=operating_system)

# get first 3 letters of every month name
operating_system_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
operating_system_cb['state'] = 'readonly'

# place the widget
operating_system_cb.pack(fill=tk.X, padx=5, pady=5)


'''
# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(title='Result', message=f'You selected {selected_month.get()}!')


month_cb.bind('<<ComboboxSelected>>', month_changed)
'''

#brand--------------------------------------------------

# label
brand = ttk.Label(text="Please select a prefered brand for your laptop:")
brand.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_brand = tk.StringVar()
selcected_brand_cb = ttk.Combobox(root, textvariable=selected_brand)

# get first 3 letters of every month name
selcected_brand_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
selcected_brand_cb['state'] = 'readonly'

# place the widget
selcected_brand_cb.pack(fill=tk.X, padx=5, pady=5)

'''
# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(title='Result', message=f'You selected {selected_month.get()}!')


month_cb.bind('<<ComboboxSelected>>', month_changed)
'''
#ram--------------------------------------------------------------------

# label
label = ttk.Label(text="Please select the amount of ram you would like for your laptop:")
label.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_label = tk.StringVar()
label_cb = ttk.Combobox(root, textvariable=selected_label)

# get first 3 letters of every month name
label_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
label_cb['state'] = 'readonly'

# place the widget
label_cb.pack(fill=tk.X, padx=5, pady=5)

'''
# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(title='Result', message=f'You selected {selected_month.get()}!')


month_cb.bind('<<ComboboxSelected>>', month_changed)
'''
#storage-----------------------------------------------------------

# label
storage = ttk.Label(text="Please select the amount of storage you would like for your laptop:")
storage.pack(fill=tk.X, padx=5, pady=5)

# create a combobox
selected_storage = tk.StringVar()
selcected_brand_cb = ttk.Combobox(root, textvariable=selected_storage)

# get first 3 letters of every month name
selcected_brand_cb['values'] = [month_name[m][0:3] for m in range(1, 13)]

# prevent typing a value
selcected_brand_cb['state'] = 'readonly'

# place the widget
selcected_brand_cb.pack(fill=tk.X, padx=5, pady=5)

'''
# bind the selected value changes
def month_changed(event):
    """ handle the month changed event """
    showinfo(title='Result', message=f'You selected {selected_month.get()}!')


month_cb.bind('<<ComboboxSelected>>', month_changed)
'''



root.mainloop()
