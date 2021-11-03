# A number generator
import tkinter as tk

#configure the window
window = tk.Tk()
window.geometry("600x600")
window.title("Number Generator")
window.configure(background='yellow')

#The button :O
but = tk.Button(window, bg="green", text="Generate", command=lambda: print("hi"))
but.pack(side= 'bottom')
window.mainloop()

