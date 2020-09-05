import tkinter as tk

label = tk.Label(
    text="Hello!",   # текст
    foreground="orange", # цвет текста
    background="green", # цвет фона
    width=50, # ширина
    height=20 # высота
)
label.pack()

label.mainloop()
