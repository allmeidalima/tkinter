from tkinter import Tk, ttk, Button

janela = Tk()
estilo = ttk.Style()
estilo.configure(
    'TButton',
    font=('Arial', 30),
)


b1 = Button(text='Live de Python')
b2 = ttk.Button(text='Live de Python')

b1.pack(pady=30)
b2.pack(
    padx=50, pady=50
)

# print(b1.winfo_class())
# print(b2.winfo_class())

janela.mainloop()