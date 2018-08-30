import sys
import os
import urllib.request
import shutil
import re

def declare_variables():
    global sFiles
    global svFiles
    global oldVV
    global FV
    global SV
    global BV

    import var

    sFiles = var.sFiles
    svFiles = var.svFiles
    oldVV = var.VV
    FV = var.MFV
    SV = var.SV
    BV = var.BV

declare_variables()

if 1 < len(sys.argv):
    newVV = sys.argv[1]
else:
    print("What is the name of the new vanilla minecraft version? e.g. %s" % oldVV)
    newVV = input("New version: ")
# Checks for the new minecraft version

os.chdir(svFiles)
# Changes directory to sFiles

URL = 'https://s3.amazonaws.com/Minecraft.Download/versions/%s/minecraft_server.%s.jar' % (newVV, newVV)
exist = urllib.request.urlopen(URL).getcode()
if exist == 200:
    if oldVV != FV:
        if os.path.isfile('%s/minecraft_server.%s.jar' % (svFiles, oldVV)):
            os.remove('%s/minecraft_server.%s.jar' % (svFiles, oldVV))
    if os.path.isfile('%s/minecraft_server.%s.jar' % (svFiles, newVV)):
        os.remove('%s/minecraft_server.%s.jar' % (svFiles, newVV))
    shutil.copyfileobj(urllib.request.urlopen(URL), open('minecraft_server.%s.jar' % newVV, 'wb'))

    s = open(os.path.join(sFiles, 'var.py'), 'r')
    string = s.read()
    newString = re.sub("VV = '%s'" %oldVV, "VV = '%s'" %newVV, string)
    s.close()
    s = open(os.path.join(sFiles, 'var.py'), 'w')
    s.write(newString)
    s.close()

    print('Vanilla servers updated from %s to %s' % (oldVV, newVV))
else:
    print('Vanilla servers not updated as minecraft_server.%s.jar does not exist' % newVV)
