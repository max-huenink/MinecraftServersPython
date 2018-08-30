__author__ = 'Administrator'
from time import sleep
import sys
import os
import shutil
import urllib.request
import zipfile
import tarfile
# import fileZip

def dot():
    dots = [".", ".", "."]
    for i in dots:
        print("."),
        sleep(0.1)

def declare_variables():
    # Declares all variables as global
    global world
    global sFiles
    global dirs
    global typeOfServer
    global version
    global down
    # var.py is the file which includes all variables
    import var
    # Declares if world is pre-named
    if 1 < len(sys.argv):
        world = sys.argv[1]
    else:
        world = var.world
    # Server Files
    sFiles = var.sFiles
    # Directory, Version, and Downloaded
    if 2 < len(sys.argv):
        typ = sys.argv[2]
    else:
        print('What is the type of server to be created?')
        print('Types: reg, snap, forge, bukkit\n       downReg, downSnap, downForge, downBukkit')
        typ = input('Type: ').lower()
    # typ is the type of server that is being created
    if typ == "reg":
        # Regular server
        dirs = var.dirsVANILLA
        typeOfServer = var.tREG
        version = var.VV
        down = var.downN
    elif typ == "downReg".lower():
        # Downloaded regular server
        dirs = var.dirsVANILLA
        typeOfServer = var.tREG
        version = var.VV
        down = var.downY
    elif typ == "snap":
        # Snapshot server
        dirs = var.dirsVANILLA
        typeOfServer = var.tSNAP
        version = var.SV
        down = var.downN
    elif typ == "downSnap".lower():
        # Downloaded snapshot server
        dirs = var.dirsVANILLA
        typeOfServer = var.tSNAP
        version = var.SV
        down = var.downY
    elif typ == "forge":
        # Forge server
        dirs = var.dirsFORGE
        typeOfServer = var.tFORGE
        version = var.FV
        down = var.downN
    elif typ == "downForge".lower():
        # Downloaded forge server
        dirs = var.dirsFORGE
        typeOfServer = var.tFORGE
        version = var.FV
        down = var.downY
    elif typ == "bukkit":
        # Bukkit server
        dirs = var.dirsBUKKIT
        typeOfServer = var.tBUKKIT
        version = var.BV
        down = var.downN
    elif typ == "downBukkit".lower():
        # Downloaded bukkit server
        dirs = var.dirsBUKKIT
        typeOfServer = var.tBUKKIT
        version = var.BV
        down = var.downY
print(sys.argv)
declare_variables()
myUID = "1b7ffd7a-6c9a-463e-8910-60c7a531b2a4"
myName = "maxh76"

if world == "":
    print('What is the name of the new server?')
    world = input('World: ')

os.mkdir(os.path.join(dirs, world))
print("Creating server directory: ", os.path.join(dirs, world)),
dot()

os.chdir(os.path.join(dirs, world))
print("Changing directory to: ", os.path.join(dirs, world)),
dot()

# Creation/Copying of all necessary files
# server-icon.png
shutil.copyfile(os.path.join(sFiles, 'server-icon.png'), os.path.join(dirs, world, 'server-icon.png'))
print("Copying server-icon.png"),
dot()

# Json files
# ops.json
op = open('ops.json', 'a')
op.write('[{\"uuid\":\"%s\",\"name\":\"%s\",level:4,bypassesplayerlimit:true}]' % (myUID, myName))
op.close()
# whitelist.json
wl = open('whitelist.json', 'a')
wl.write('[{\"uuid\":\"%s\",\"name\":\"%s\"}]' % (myUID, myName))
wl.close()
# banned-ips.json
bi = open('banned-ips.json', 'a')
bi.write('[]')
bi.close()
# banned-players.json
bp = open('banned-players.json', 'a')
bp.write('[]')
bp.close()
# usercache.json
uc = open('usercache.json', 'a')
uc.write('[]')
uc.close()

# Server Properties
import sPropsCreate

# Changing level name
lvlName = open("server.properties.tmp", "a")
for line in open("server.properties"):
    line = line.replace("level-name=world", "level-name=" + world)
    lvlName.write(line)
lvlName.close()
shutil.move('server.properties.tmp', 'server.properties')

# Getting and setting motd
print('Motd?')
print('\\u00A7')
print('Black: 0 | Dark Blue: 1 | Dark Green: 2 | Dark Aqua: 3 | Dark Red: 4\n'
      'Dark Purple: 5 | Gold: 6 | Gray: 7 | Dark Gray: 8 | Blue: 9 | Green: a\n'
      'Aqua: b | Red: c | Light Purple: d | Yellow: e | White: f\n'
      'Obfuscated: k | Bold: l | Strikethrough: s | Underline: n | Italic: o | Reset: r')
motdI = input('motd=')
if motdI == "":
    motdI = "\u00A7dMax\'s Minecraft Server"

# TODO find out why his is broken
# I think I fixed it and it is no longer broken

motdF = open('server.properties.tmp', 'a')
for line in open('server.properties'):
    line = line.replace('motd=A Minecraft Server', 'motd=' + motdI)
    motdF.write(line)
motdF.close()
shutil.move('server.properties.tmp', 'server.properties')

# Setting up start files
if down == 'yes':
    # Downloading file
    URL = input('Download url: ')
    shutil.copyfileobj(urllib.request.urlopen(URL), open('file.zip', 'wb'))

    # Unzipping file
    zfile = zipfile.ZipFile('file.zip')
    zfile.extractall('.')
    print(zfile.printdir())
    print('What is the path for the world?')
    print('i.e. world')
    zfile.close()
    zfileName = input('Path=')
    shutil.move(zfileName, world)
    os.remove('file.zip')
    # fileZip.zip_folder(world, world + '.tar')
    cleanFile = tarfile.open(world + '.tar')
    cleanFile.add(world)
    cleanFile.close()

# This function should get called
# in the if statements
def fileCopy(startVersion, typeOfServer, sFiles):
    # startVersion should be regStart or snapStart

    startFile = startVersion + '.py'

    shutil.copy(os.path.join(sFiles, startFile), startFile)
    shutil.copy(os.path.join(sFiles, 'backupStart.py'), 'backupStart.py')
    if down == 'yes':
      shutil.copy(os.path.join(sFiles, 'cleanStart.py'), 'cleanStart.py')

    regF = open('sType', 'a')
    regF.write(typeOfServer)
    regF.close()

    eula = open('eula.txt', 'a')

    eula.write('eula=true')
    eula.close()

    if startVersion == 'regStart':
        import regStart
    elif startVersion == 'snapStart':
        import snapStart
# I don't even need the if statements
# at this point since startVersion
# and typeOfServer both end in
# Start
# just invoke def fileCopy(typeOfServer, sFiles)
# then we can set startVersion = typeOfServer + 'Start'
# and seet startFile = startVersion + '.py'
# 
# But keep sFiles for modularization

## Leaving if statements for now
## Since forge and bukkit would
## Require a tad bit more work
## to switch over

# I can probably rework all of this
# into a function..
# At least the stuff for regular and
# snapshot servers, since they are
# practically identical.
if typeOfServer == 'reg':

    sVersion = 'regStart'
    fileCopy(sVersion, typeOfServer, sFiles)

# DEPRECATED
#
#    sType = 'regStart.py'
#
#    shutil.copy(os.path.join(sFiles, sType), sType)
#    shutil.copy(os.path.join(sFiles, 'backupStart.py'), 'backupStart.py')
#    if down == 'yes':
#        shutil.copy(os.path.join(sFiles, 'cleanStart.py'), 'cleanStart.py')
#    regF = open('sType', 'a')
#    regF.write(typeOfServer)
#    regF.close()
#
#    eula = open('eula.txt', 'a')
#    eula.write('eula=true')
#    eula.close()
#
#    import regStart

elif typeOfServer == 'snap':

    sVersion = 'snapStart'

    fileCopy(sVersion, typeOfServer, sFiles)

# DEPRECATED
#    sType = 'snapshotStart.py'
#
#    shutil.copy(os.path.join(sFiles, sType), sType)
#    shutil.copy(os.path.join(sFiles, 'backupStart.py'), 'backupStart.py')
#    if down == 'yes':
#        shutil.copy(os.path.join(sFiles, 'cleanStart.py'), 'cleanStart.py')
#    regF = open('sType', 'a')
#    regF.write(typeOfServer)
#    regF.close()
#
#    eula = open('eula.txt', 'a')
#    eula.write('eula=true')
#    eula.close()
#
#    import snapshotStart

elif typeOfServer == 'forge':
    shutil.copytree(os.path.join(sFiles, 'forgeLibraries'), 'libraries')
    os.mkdir('mods')
    shutil.copy(os.path.join(sFiles, 'regForgeStart.py'), 'regForgeStart.py')
    shutil.copy(os.path.join(sFiles, 'backupForgeStart.py'), 'backupForgeStart.py')
    if down == 'yes':
        shutil.copy(os.path.join(sFiles, 'cleanForgeStart.py'), 'cleanForgeStart.py')

    eula = open('eula.txt', 'a')
    eula.write('eula=true')
    eula.close()

    import regForgeStart

elif typeOfServer == 'bukkit':
    shutil.copy(os.path.join(sFiles, 'regBukkitStart.py'), 'regBukkitStart.py')
    shutil.copy(os.path.join(sFiles, 'backupBukkitStart.py'), 'backupBukkitStart.py')
    if down == 'yes':
        shutil.copy(os.path.join(sFiles, 'cleanBukkitStart.py'), 'cleanBukkitStart.py')

    eula = open('eula.txt', 'a')
    eula.write('eula=true')
    eula.close()

    import regBukkitStart
# EOF
