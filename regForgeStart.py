import os
import sys
sType = 'forge'
invoke = 'python3'

def declare_forge_variables():
    # Declares all variables as global
    global world
    global sFiles
    global dirs
    global typeOfServer
    global version
    global down

    # var.py is the file which includes all variables
    import var

    world = var.world

    # Server Files
    sFiles = var.sFiles

    # Forge server
    dirs = var.dirsFORGE
    typeOfServer = var.tFORGE
    version = var.FV
    down = var.downN

declare_forge_variables()

if os.name == 'nt':
    invoke = "py -3"
elif os.name == 'posix':
    invoke = "python3"

os.system(invoke + ' fStart.py ' + sType + sFiles + version)
