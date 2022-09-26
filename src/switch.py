#!/usr/bin/env python3

import serial 
import sys 

try:
  dn = sys.argv[1]
except IndexError:
  print("Please provide the display number 1 -4")
  sys.exit(0)

try:
   dn = int(dn)
except Exception as err:
   print("display number must be integer")
   sys.exit(0)

if dn >=1 and dn <= 4:
  pass 
else:
   print("Display number should be 1 - 4")
   sys.exit(0)

if dn == 1:
   c = [0x47,0x30,0x31,0x67,0x41,0x00]
if dn == 2:
   c = [0x47,0x30,0x32,0x67,0x41,0x00]
if dn == 3:
   c = [0x47,0x30,0x33,0x67,0x41,0x00]
if dn == 4:
   c = [0x47,0x30,0x34,0x67,0x41,0x00]
try:
   s = serial.Serial('/dev/ttyUSB1', 9600)
   s.write(serial.to_bytes(c))
except Exception as err:
   print("Exception while sending command!")
   print(err)
finally:
   s.close()
