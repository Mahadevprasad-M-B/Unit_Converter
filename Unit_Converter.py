# -*- coding: utf-8 -*-
"""
Created on Wed Feb 21 10:13:53 2024

@author: Lenovo
"""
import tkinter as tk
from tkinter import ttk

# conversion method

def unit_conversion():
    value = float(value_entry.get())
    sel_Type = unit_entry.get()

    # Conversion from Centimeter to Feet
    if sel_Type == "Centimeter to Feet":
        result = (value/30.48)
        result_label1["text"] = f"{round(value, 2)} cm is equal to {round(result,2)} Feet"

    # Conversion from Feet to Inches
    elif sel_Type == "Feet to Inches":
        result = (value*12)
        result_label1["text"] = f"{round(value, 2)} Feet is equal to {round(result,2)} inches"

    # Conversion from Sqft to Sqmtr
    elif sel_Type == "Sqft to Sqmtr":
        result = (value * 0.0929)
        result_label1["text"] = f"{round(value, 2)} Sqft is equal to {round(result,2)} Sqmtr"
    
    # Conversion from Sqft to Hectre 
    elif sel_Type == "Sqft to Hectare":
        result = (value/107639.104)
        result_label1["text"] = f"{round(value, 2)} Sqft is equal to {round(result,2)} Hectare"

    # Conversion from Sqft to Acre
    elif sel_Type == "Sqft to Acre":
        result = (value / 43560)
        result_label1["text"] = f"{round(value, 2)} Sqft is equal to {round(result,2)} Acre"

    else:
        result_label1["text"] = f"--Invalid Conversion Type--"


#GUI Setup

window = tk.Tk()
window.title('Unit Converter')
window.configure(background='#020a25')

# Setting the title of the window
title_label = ttk.Label(window,text="Unit Converter")
title_label.grid(row=0,column=0,padx=10,pady=10)

#Setting the the label 
unit_label = ttk.Label(window,text='Type of conversion:',width=20)
unit_label.grid(row=1,column=0,padx=10,pady=10)

# List of ootions displayed in the combo box
unit_options = ["Centimeter to Feet","Feet to Inches","Sqft to Sqmtr","Sqft to Hectare","Sqft to Acre"]

# To select the type f conversion from the list
unit_entry = ttk.Combobox(window,values=unit_options,width=20)
unit_entry.grid(row=1,column=1,padx=10,pady=10)

# To emter the value
value_label = ttk.Label(window,text='Enter the Value',width=20)
value_label.grid(row=2,column=0,padx=10,pady=10)
value_entry = ttk.Entry(window,width=20)
value_entry.grid(row=2,column=1,padx=10,pady=10)

# button to convert units 
convert_btn = ttk.Button(window,text='Convert',command=unit_conversion)
convert_btn.grid(row=3,column=1,padx=10,pady=10)

# Label to display the result
result_label = ttk.Label(window,text='Result:',width=20)
result_label.grid(row=4,column=0,padx=10,pady=10)

result_label1 = ttk.Label(window,text='----',width=30)
result_label1.grid(row=4,column=1,padx=10,pady=10)

window.mainloop()