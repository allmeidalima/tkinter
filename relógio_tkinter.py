"""
root = Tk()
root.title("Relógio Mundial")
ttk.Label(
    root,
    font=('Comicsans, 30')
        )
    hour.after(1000, time_country)
       
root.mainloop()

time_country()
#root.after(1000, time_country)



clock = Label()
clock.pack()
clock['font'] = 'Roboto 100 bold'
clock['text'] = strftime('%H:%M:%S')

def get_current_time():
    now = strftime('%H:%M:%S')
    if now != clock['text']:
        clock['text'] = now
    clock.after(100, get_current_time)

get_current_time()
clock.mainloop()
"""

from tkinter import *
from tkinter import ttk
import datetime
from ttkbootstrap import Style
from time import strftime
import pytz

style = Style()
root = style.master

root.title('Relógio Mundial')

frame_geral = ttk.Frame()

def time_country():
    country_huor = datetime.datetime.now()
    hour = country_huor.strftime('%H:%M:%S')
    print(hour)

values_countrys = [tz for tz in pytz.country_timezones]
#print(values)

#Sigla paises
frame_sigla_pais = ttk.Frame(frame_geral)

label_sigla_pais = ttk.Label(
    frame_sigla_pais,
    text='Pais',
    font=(None, 20)
)
combo_countrys = ttk.Combobox(
    frame_sigla_pais,
    values=values_countrys,
    font=(None, 20)
)
combo_countrys.set("BR")
resultado = combo_countrys.get()

label_sigla_pais.grid(row=0, column=0, padx=10, pady=10)
combo_countrys.grid(row=0, column=1, padx=10, pady=10)
frame_sigla_pais.pack()

values_estados = [es for es in pytz.country_timezones(resultado)]
print(values_estados)
#Estados
frame_estados = ttk.Frame(frame_geral)

label_estados = ttk.Label(
    frame_estados,
    text='Estado',
    font=(None, 20)
)
combo_estados = ttk.Combobox(
    frame_estados,
    values=values_estados,
    font=(None, 20)
)

label_estados.grid(row=0, column=0, padx=10, pady=10)
combo_estados.grid(row=0, column=1, padx=10, pady=10)
frame_estados.pack()

frame_geral.pack()
root.mainloop()