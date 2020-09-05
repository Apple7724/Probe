import tkinter as tk

window = tk.Tk()
label = tk.Label(text="Input name ",fg="red")
entry = tk.Entry(
    fg="yellow",
    bg="brown",
    width=50
)


label.pack()
entry.pack()




entry.mainloop()
