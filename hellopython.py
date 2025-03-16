from tkinter import *  # Import all classes, functions, and constants from the Tkinter module

window = Tk()  # Create a main window object
window.geometry("420x420")  # Set the dimensions of the window to 420x420 pixels

window.title("4-EVER")  # Set the title of the window to "4-EVER"
logo = PhotoImage(file='image.png')  # Load an image file and create a PhotoImage object
window.iconphoto(True, logo)  # Set the window icon to the loaded image
window.config(bg="purple")  # Set the background color of the window to purple

window.mainloop()  # Start the Tkinter event loop to display the window and respond to user interactions