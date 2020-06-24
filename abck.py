""" 
Python _abck lib 
Inspired by https://github.com/zedd3v/abck 
Xero/FlySolutions (C) 2020
"""

from time import time
import random
class Abck:
   def __init__(self):
      # Global vars, in order of use (kinda)
      self.xagg = "11123" # Xagg, related to Bmak.xagg
      self.product_sub = "20100101" # Psub, related to Bmak.psub which is related to native navigator.productSub
      self.language = "en-US" # Lang, related to Bmak.lang which is related to native navigator.Language
      self.engine = "Gecko" # Prod, related to Bmak.prod which is related to native navigator.product
      self.plugin_count = "0" # Plen, related to Bmak.plen which is amount of plugins
      self.headless = "0" # Pen, related to Bmak.pen which is if browser is headless (native window._phantom)
      self.window = "0" # Wen, related to Bmak.wen which is looking for a new window. (Detecting selenium)
      self.spam_bot = "0" # Den, related to Bmak.den which is looking if you are a spam bot (Detecting domAutomation)
      self.callPhantom = "0" # BD Function cpen
      self.is_ie = "0"       # . i1
      self.docMode = "0"     # . dm
      self.chromeWS = "0"    # . cwen
      self.onLine = "1"      # . non
      self.opera = "0"       # . opc
      self.firefox = "1"     # . fc
      self.safari = "0"      # . sc
      self.rtcSupport = "1"  # . wrc
      self.windowTop = "74"  # . isc
      self.vibration = "1"   # . vib
      self.battery = "0"     # . bat
      self.forEach = "0"     # . x11
      self.filereader = "1"   # . x12

   # Get_cf_date Function
   def get_cf_date(self):
      return int(time()*1000)

   # AB Function (Akamais 'hashing' method)
   def ab(self, t):
      if t == None:
         return -1
      a = 0
      for p in t:
         if ord(p) < 128:
            a += ord(p)
      return a

   # BD Function (Only to build as string)
   def bd(self):
      bd_string = ""
      bd_string += "cpen:" + self.callPhantom + ","
      bd_string += "i1:" + self.is_ie + ","
      bd_string += "dm:" + self.docMode + ","
      bd_string += "cwen:" + self.chromeWS + ","
      bd_string += "non:" + self.onLine + ","
      bd_string += "opc:" + self.opera + ","
      bd_string += "fc:" + self.firefox + ","
      bd_string += "sc:" + self.safari + ","
      bd_string += "wrc:" + self.rtcSupport + ","
      bd_string += "isc:" + self.windowTop + ","
      bd_string += "vib:" + self.vibration + ","
      bd_string += "bat:" + self.battery + ","
      bd_string += "x11:" + self.forEach + ","
      bd_string += "x12:" + self.filereader
      return bd_string
   
   def gd(self,
   availWidth,availHeight,width,height,clientWidth,clientHeight,outerWidth,
   user_agent,
   start_ts):
      # Vars
      self.z1 = int(start_ts / (2016 * 2016)) # z1
      self.d3 = self.get_cf_date() % 10000000 # d3, current timestamp divided by  1e7 (7 zeros)
      screen_string = str(availWidth) + "," + str(availHeight) + "," + str(width) + "," + str(height) + "," + str(clientWidth) + "," + str(clientHeight) + "," + str(outerWidth) # Screen sizes
      bd_string = self.bd()
      ua_hash = self.ab(user_agent)
      rnd_seed = str(random.random())[0:14]
      ts_2 = start_ts / 2
      ts_2 = int(ts_2)
      # Build string
      gd_string = ""
      gd_string += user_agent + ",uaend," # User-agent
      gd_string += self.xagg + "," # Xagg, related to Bmak.xagg
      gd_string += self.product_sub + "," # Psub, related to Bmak.psub
      gd_string += self.language + "," # Lang, related to Bmak.lang
      gd_string += self.engine + "," # Prod, related to Bmak.prod
      gd_string += self.plugin_count + "," # Plen, related to Bmak.plen
      gd_string += self.headless + "," # Pen, related to Bmak.pen
      gd_string += self.window + "," # Wen, related to Bmak.wen
      gd_string += self.spam_bot + "," # Den, related to Bmak.den
      gd_string += str(self.z1) + "," # z1, related to Bmak.z1
      gd_string += str(self.d3) + "," # d3, related to Bmak.d3
      gd_string += screen_string + "," # Screen info
      gd_string += "," + bd_string + "," # BD, various info about the browser
      gd_string += str(ua_hash) + "," # User-Agent Hash
      gd_string += str(rnd_seed) + "," # Random seed number
      gd_string += str(ts_2) # Start timestamp divided by 2
      gd_string += ",loc:" # Loc, related to bmak.loc which is empty

      return gd_string

   def sed(self):
      return "0,0,0,0,1,0,0"

   def fas(self):
      return "26067385"

   def np(self):
      return "11133333331333333333"

   def calc_o9(self):
      t = e = self.d3
      for c in range(0, 5):
         n = int(t / 10 ** c) % 10
         a = n + 1
         mn = n % 4
         if mn == 0:
            e = e * a
         elif mn == 1:
            e = e + a
         else:
            e = e - a
      return e

   def calc_d3(self):
      return self.d3
