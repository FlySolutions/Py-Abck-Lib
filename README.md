# Py-Abck-Lib
Python Abck Lib inspired by https://github.com/zedd3v/abck \
Example of all uses in main.py
```python
from abck import Abck
from time import time

abck = Abck()

# Your starting timestamp
start_ts = int(time()*1000)

# Gd function
gd = abck.gd(
   1366, 768, 1366, 768, 1366, 350, 1382, # Screen sizes
   "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0", # User-Agent
   start_ts # Your starting timestamp
)
print(gd)
# Output => Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:76.0) Gecko/20100101 Firefox/76.0,uaend,11123,20100101,en-US,Gecko,0,0,0,0,391955,8236186,1366,768,1366,768,1366,350,1382,,cpen:0,i1:0,dm:0,cwen:0,non:1,opc:0,fc:1,sc:0,wrc:1,isc:74,vib:1,bat:0,x11:0,x12:1,5561,0.309670225845,796504118093,loc:

# Ab function
ab = abck.ab("Hello")
print(ab)
# Output => 500

# Sed function
sed = abck.sed()
print(sed)
# Output => 0,0,0,0,1,0,0

# Fas function
fas = abck.fas()
print(fas)
# Output => 26067385

# Np function
np = abck.np()
print(np)
# Output => 11133333331333333333

# o9
o9 = abck.calc_o9()
print(o9)
# Output (Is diff each time genned) => 75155232

#d3
d3 = abck.calc_d3()
print(d3)
# Output (Is diff each time genned) => 8350580
```
