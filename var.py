import os
import sys
sFilesRAW = "servers/minecraft/filesPy/"
svFilesRAW = sFilesRAW + "versions/"
dirVRaw = "servers/minecraft/minecraftServers/"
dirFRaw = "servers/minecraft/forgeServers/"
dirBRaw = "servers/minecraft/bukkitServers/"
win32Origin = "E:\\"
cygwinOrigin = "/cygdrive/e/"
linuxOrigin = "/media/max/UNTITLED/"
finFiles = ""
finVFiles = ""
finDirV = ""
finDirF = ""
finDirB = ""

javaLaunch = "E:\\\\\\\\servers\\\\\\\\minecraft\\\\\\\\filesPy\\\\\\\\versions"

if sys.platform == 'win32':
    finFiles = os.path.normcase(os.path.join(win32Origin, sFilesRAW))
    finVFiles = os.path.normcase(os.path.join(win32Origin, svFilesRAW))
    finDirV = os.path.normcase(os.path.join(win32Origin, dirVRaw))
    finDirF = os.path.normcase(os.path.join(win32Origin, dirFRaw))
    finDirB = os.path.normcase(os.path.join(win32Origin, dirBRaw))
elif sys.platform == 'cygwin':
    finFiles = os.path.normcase(os.path.join(cygwinOrigin, sFilesRAW))
    finVFiles = os.path.normcase(os.path.join(cygwinOrigin, svFilesRAW))
    finDirV = os.path.normcase(os.path.join(cygwinOrigin, dirVRaw))
    finDirF = os.path.normcase(os.path.join(cygwinOrigin, dirFRaw))
    finDirB = os.path.normcase(os.path.join(cygwinOrigin, dirBRaw))
elif sys.platform == 'linux':
    finFiles = os.path.normcase(os.path.join(linuxOrigin, sFilesRAW))
    finVFiles = os.path.normcase(os.path.join(linuxOrigin, svFilesRAW))
    finDirV = os.path.normcase(os.path.join(linuxOrigin, dirVRaw))
    finDirF = os.path.normcase(os.path.join(linuxOrigin, dirFRaw))
    finDirB = os.path.normcase(os.path.join(linuxOrigin, dirBRaw))

sFiles = finFiles
svFiles = finVFiles
world = ""
dirsVANILLA = finDirV
dirsFORGE = finDirF
dirsBUKKIT = finDirB
tREG = "reg"
tSNAP = "snap"
tFORGE = "forge"
tBUKKIT = "bukkit"
downN = "no"
downY = "yes"

# Version of each server type
VV = '1.13'
# Vanilla Version

SV = '1.13'
# Snapshot Version

BV = 'dev.1.7.10'
# Bukkit Version

FV = '1.7.10-10.13.3.1358-1.7.10'
# Forge Version

MFV = '1.7.10'
# Minecraft Forge Version
