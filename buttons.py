from tkinter import *  # Import all classes, functions, and constants from the Tkinter module

window =Tk()
window.title(' BUTTONS !')

pic =PhotoImage(file='image.png')
window.iconphoto(True,pic)


#############    buttons     ############

button = Button(window,
                text='click me',
                relief=RAISED,
                fg='red',
                bd=10,
                bg='green',
                font=('sans-serif',20,'bold'),
                padx=10,
                pady=10,
                image=pic,
                compound='top',
                
               
                )
button.pack()

window.mainloop()