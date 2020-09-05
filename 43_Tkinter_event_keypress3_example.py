import tkinter as tk
  
  
def func():
    try:
        x = float(entry_1.get())
        y = float(entry_2.get())
        label.config(text="Сумма числе будет равна {}".format(x + y))
    except ValueError:
        label.config(text="Ошибка введите цифры")
  
  
root = tk.Tk()
entry_1 = tk.Entry(root)
entry_2 = tk.Entry(root)
entry_1.pack()
entry_2.pack()
label = tk.Label(root, text="Сумма числе будет равна")
label.pack()
button = tk.Button(root, text='сложить числа', command=func)
button.pack()
root.mainloop()
