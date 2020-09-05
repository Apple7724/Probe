import tkinter as tk
 
# Создает объект окна. 
window = tk.Tk()

i= 0
 
# Создает обработчик событий.
def mouse_motion(event):
    
    button["text"] = "Good bye"

def mouse_leave(event):
    
    button["text"] = "Кликни"
# функция счетчика
def button_count(event):
    global i
    i = i+1
    counter.config(text="{}".format(i))
    print(i)

   
# Начальное изображение кнопки     
button = tk.Button(text="Кликни!")

# Начальное изображение счетчика
counter = tk.Label(bg='yellow', width=20, height=4, text='i')
counter.config(text="{}".format(i))
counter.pack(expand=1)


# Варианты действий 
button.bind("<Enter>", mouse_motion)
button.bind("<Leave>", mouse_leave)
button.bind("<Button-1>", button_count)

button.pack()

# Запускает обработчик событий.
window.mainloop()
