import tkinter as tk
 
# Создает объект окна. 
window = tk.Tk()
 
# Создает обработчик событий.
def handle_keypress(event):
    """Выводит символ, связанный с нажатой клавишей"""
    print(event.char)

window.bind("<Key>", handle_keypress)
# Запускает обработчик событий.
window.mainloop()
