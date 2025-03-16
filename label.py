from tkinter import *  # Import all classes, functions, and constants from the Tkinter module

window = Tk()  # Create a main window object


window.title('4-EVER')

logo = PhotoImage(file='image.png')  # Load an image file and create a PhotoImage object
window.iconphoto(True,logo)


label = Label(
             window,
             text="Hello, Tkinter!",
             foreground='blue',
             font=('arial',40,'italic'),
             bg='black',
             relief=RAISED,
             bd=10,
             padx=10,
             pady=10,
             image=logo,#adds image to label but removes text tocovercome this use compound
             compound='top',
             )                              # Create a label widget with text
label.pack()  # Add the label to the window
#label.place(x= 210,y=210) # Add the label to the window

window.mainloop()  # Start the Tkinter event loop to display the window and respond to user interactions