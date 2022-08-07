from tkinter import Tk, Label, Button

window = Tk() #criando uma janela 

#criando uma Label
text = Label(
    text='Hello Word',
    font=('serif', 50)
) 
text.pack() #Juntando todos o widgets 

window.mainloop() #Rodando em loop a janela 

