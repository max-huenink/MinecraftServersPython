import os
import sys
sType = 'reg'
invoke = 'python3'

def declare_reg_variables():
    # Declares all variables as global
    global world
    global sFiles
    global svFiles
    global dirs
    global typeOfServer
    global version
    global down
    global javaP

    # var.py is the file which includes all variables
    import var

    world = var.world

    # Server Files, minecraft versions folder
    sFiles = var.sFiles

    # Regular server
    dirs = var.dirsVANILLA
    typeOfServer = var.tREG
    version = var.VV
    down = var.downN
    javaP = var.javaLaunch

declare_reg_variables()

if os.name == 'nt':
    invoke = "py -3"
elif os.name == 'posix':
    invoke = "python3"
os.system(invoke + ' ' + os.path.join(sFiles, 'fStart.py') + ' ' + sType + ' ' + javaP + ' ' + "1.8.9")

