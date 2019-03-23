# Timer Application using Time and Tkinter Module
# done by @Sri_Programmer
# pythonv3.7.2

__auhtor__ = 'Sri Manikanta Palakollu.'

import time
import tkinter as tk
from tkinter import *

# Function to generate the time
def tick(time1 =''):
    time2 = time.strftime('%I:%M:%S')
    if time2 != time1:
        time1 = time2
        clock_frame.config(text=time2)
    clock_frame.after(200, tick)

window = tk.Tk()    # Initializes the window
window.title("Timer Application")   # Title for the window
clock_frame = tk.Label(window, font=('Monaco 65 bold'),bg = '#2B2B52', fg='#D63031')    # Labelling the Entire window
clock_frame.pack(fill='both', expand=1) 
window.geometry('700x500')  # Size of the window
window.configure(background="lightgreen")   

tick()  # Function Call. 

# End of the Loop
window.mainloop()