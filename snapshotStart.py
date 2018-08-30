import os
import sys
sType = 'snap'
invoke = 'python3'

def declare_snapshot_variables():
    # Declares all variables as global
    global world
    global sFiles
    global dirs
    global typeOfServer
    global version
    global down
    global javaP

    # var.py is the file which includes all variables
    import var

    world = var.world

    # Server Files
    sFiles = var.sFiles

    # Snapshot server
    dirs = var.dirsVANILLA
    typeOfServer = var.tSNAP
    version = var.SV
    down = var.downN
    javaP = var.javaLaunch

declare_snapshot_variables()

if os.name == 'nt':
    invoke = "py -3"
elif os.name == 'posix':
    invoke = "python3"
os.system(invoke + ' ' + os.path.join(sFiles, 'fStart.py') + ' ' + sType + ' ' + javaP + ' ' + version)
