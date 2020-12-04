from datetime import date
from datetime import datetime
from datetime import timedelta


d1 = datetime.now()
d1s = d1.strftime("%d-%b-%Y")
request = d1.strftime("%d-%b-%Y (%H:%M:%S)")

d2 = d1 + timedelta(days=1)
d2s = d2.strftime("%d-%b-%Y")

d3 = d1 + timedelta(days=2)
d3s = d3.strftime("%d-%b-%Y")

d4 = d1 + timedelta(days=3)
d4s = d4.strftime("%d-%b-%Y")

d5 = d1 + timedelta(days=4) 
d5s = d5.strftime("%d-%b-%Y")