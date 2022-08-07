from tkinter import *
from turtle import width

class Application:
    def __init__(self,master=None):
        #pass
        self.widget1 = master.title("Relógio")
        self.widget1 = Frame(master)
        self.widget1.pack()
        self.msg = Label(self.widget1, text="Primeiro widget")
        self.msg["font"] = ("Calibri", "10", "italic", "bold")
        self.msg.pack()
        self.sair = Button(self.widget1)
        self.sair["text"] = "Clique aqui"
        self.sair["font"] = ("Calibri", "10")
        self.sair["width"] = 10
        self.sair.bind("<Button-1>", self.mudarTexto)
        #self.sair["command"] = self.widget1.quit
        self.sair.pack()

    def mudarTexto(self, event):
        if self.msg["text"] == "Primeiro widget":
            self.msg["text"] = "O botão recebeu um clique"
        else:
            self.msg["text"] = "Primeiro widget"




root = Tk()
Application(root)
root.mainloop()

