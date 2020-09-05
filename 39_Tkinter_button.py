import tkinter as tk

button = tk.Button(
    text="Push me!",   # текст
    foreground="red", # цвет текста
    background="yellow", # цвет фона
    width=50, # ширина
    height=20 # высота
)
button.pack()

button.mainloop()
