import sys
import os
import urllib.request
import shutil
import re

def declare_variables():
    global sFiles
    global svFiles
    global oldSV
    global FV
    global VV
    global BV

    import var

    sFiles = var.sFiles
    svFiles = var.svFiles
    oldSV = var.SV
    FV = var.MFV
    VV = var.VV
    BV = var.BV

declare_variables()

if 1 < len(sys.argv):
    newSV = sys.argv[1]
else:
    print("What is the name of the new vanilla minecraft version? e.g. %s" % oldSV)
    newSV = input("New version: ")
# Checks for the new minecraft version

os.chdir(svFiles)
# Changes directory to sFiles

URL = 'https://s3.amazonaws.com/Minecraft.Download/versions/%s/minecraft_server.%s.jar' % (newSV, newSV)
exist = urllib.request.urlopen(URL).getcode()
if exist == 200:
    if oldSV != VV:
        if os.path.isfile('%s/minecraft_server.%s.jar' % (svFiles, oldSV)):
            os.remove('%s/minecraft_server.%s.jar' % (svFiles, oldSV))
    if os.path.isfile('%s/minecraft_server.%s.jar' % (svFiles, newSV)):
        os.remove('%s/minecraft_server.%s.jar' % (svFiles, newSV))
    shutil.copyfileobj(urllib.request.urlopen(URL), open('minecraft_server.%s.jar' % newSV, 'wb'))

    s = open(os.path.join(sFiles, 'var.py'), 'r')
    string = s.read()
    newString = re.sub("SV = '%s'" % oldSV, "SV = '%s'" % newSV, string)
    s.close()
    s = open(os.path.join(sFiles, 'var.py'), 'w')
    s.write(newString)
    s.close()

    print('Snapshot servers updated from %s to %s' % (oldSV, newSV))
else:
    print('Snapshot servers not updated as minecraft_server.%s.jar does not exist' % newSV)
