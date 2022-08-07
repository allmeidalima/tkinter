from tkinter import *
from tkinter import ttk
import datetime
import pytz

class Clock:
    def __init__(self,master=None):
        self.widget = master.title("Clock")
        self.widget = Frame(master)
        self.hour = ttk.Label(
            self.widget,
            font=('Comicsans, 30')

        )
        self.hour.pack()
        self.time_country()
        self.hour.grid(row=0, column=1, sticky=W, pady=2)
        self.hour.pack()
        
        self.phrase = ttk.Label(
            text="Sigla do Pais"
        )
        self.phrase.pack(side=LEFT)
        #self.options = StringVar()
        #self.combo = ttk.Combobox(self.widget, textvariable=self.options)
        #self.combo['values'] = [co for co in pytz.country_timezones]
        #self.combo['state'] = 'readonly'
        #self.combo['width'] = 5
        #self.combo.pack(side=LEFT, padx=10, pady=20)

    def time_country(self):
        country_huor = datetime.datetime.now()
        self.hour['text'] = country_huor.strftime('%H:%M:%S')
        self.widget.after(1000, self.time_country)
        







root = Tk()
Clock(root)
root.mainloop()