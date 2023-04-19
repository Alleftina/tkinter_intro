import tkinter as tk
# from tkinter import ttk
import ttkbootstrap as ttk


window = ttk.Window(themename='darkly')
window.title('Intro')
window.geometry('300x150')

km_in_miles = 1.60934

def convert():
    mile_input = entry_int.get()
    kilometres_out = round(km_in_miles*mile_input,3)
    output_string.set(str(kilometres_out))

title_label = ttk.Label(master=window,
                        text='Miles to kilometers',
                        font='Calibri 26 bold')

title_label.pack()
input_frame = ttk.Frame(master=window)
entry_int = tk.IntVar()
entry = ttk.Entry(master=input_frame, textvariable=entry_int)
button = ttk.Button(master=input_frame,
                    text='Convert',
                    command=convert)

entry.pack(side='left', padx=10)
button.pack(side='left')
input_frame.pack(pady=10)


output_string = tk.StringVar()

output_label = ttk.Label(master=window,
                         text='Output',
                         font='Calibri 26',
                         textvariable=output_string)

output_label.pack(pady=5)

window.mainloop()
