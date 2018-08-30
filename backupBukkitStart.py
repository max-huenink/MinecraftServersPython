import os
import tarfile
import datetime
import re
s = open("server.properties", "r")
lines = s.readlines()
W = ''
for i in lines:
    search = re.search('level-name=', i)
    if search:
        W = re.sub(r'\n', '', i)[11:]
s.close()

day = str(datetime.datetime.now().day)
month = str(datetime.datetime.now().month)
year = str(datetime.datetime.now().year)
hour = str(datetime.datetime.now().hour)
minute = str(datetime.datetime.now().minute)
second = str(datetime.datetime.now().second)
time = year + '-' + month + '-' + day + '-' + hour + '.' + minute + '.' + second

fName = W + '_' + time + '.tar'
print("Compressing " + W + "to " + fName)
file = tarfile.open(fName, 'w')
file.add(W)
file.close()
print("Done compressing")

# Fsty = open('sType', 'r')
# sty = Fsty.read
# Fsty.close()

import regBukkitStart