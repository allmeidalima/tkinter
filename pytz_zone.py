import pytz
from datetime import datetime

pais = input("Pais: ")
d_e_h_n = datetime.now()
f = pytz.country_timezones(pais)
#print(f)
for p in f: 
  f_h = pytz.timezone(p)
  fuso = d_e_h_n.astimezone(f_h)
  print(f"Local  {p}   hora {fuso}")