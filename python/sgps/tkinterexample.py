from tkinter import *
from tkinter import ttk

# Tk()  ->  Initializes Tk and creates the Tcl Interpreter, also 
#           creates the main window of the application

# ttk.Frame(parentContainer, attributes)
#
#   ^_______Creates a frame widget, basically an empty container
#           where we can fit other widgets, ttk allows the use 
#           of Tk themed widgets, difference with normal tk.widget
#           is that it adapts to the platform the program runs in,
#           it also offers a bunch of exclusive widgets               
#                                       

# widget(parentContainer, attributes).grid(column=, row=)   ->  Positions a widget inside the parent widget,
#                                                               in the given row and column

# Available widgets are:
# - Button
# - Checkbutton
# - Entry
# - Frame
# - Label
# - LabelFrame
# - Menubutton
# - PanedWindow
# - Radiobutton
# - Scale
# - Scrollbar
# - Spinbox
# ttk exclusive widgets:
# - Combobox
# - Notebook
# - Progressbar
# - Separator
# - Sizegrip
# - Treeview


## Root Definition and Settings
root = Tk()
root.title("Auto SGPS")
root.configure(
    # width=100,
    # height=100,
    # padx=100,
    # pady=100,
    bg="purple"
)
root.wm_minsize(800, 600)
root.columnconfigure(0,weight=1)
root.rowconfigure(0, weight=1)

# Main frame initialization and configuration
main_frame = ttk.Frame(root, padding=10) # positions the main frame with 10px padding inside our root/window
main_frame.grid()


label1 = ttk.Label(main_frame, text="Yo mama fat as hell").grid(column=2,row=1)
btn1 =ttk.Button(main_frame,text="Got It!", command=root.destroy).grid(column=2,row=2)

print("Root Keys ->", root.keys(), "\nFrame Keys -> ", main_frame.keys())
root.mainloop() # puts everything on the display, and responds to user input until the program terminates.



def nose():
    pass