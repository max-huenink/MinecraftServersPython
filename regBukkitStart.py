import os
import sys
sType = 'bukkit'
invoke = 'python3'

def declare_bukkit_variables():
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

    # Bukkit server
    dirs = var.dirsBUKKIT
    typeOfServer = var.tBUKKIT
    version = var.BV
    down = var.downN

declare_bukkit_variables()

if os.name == 'nt':
    invoke = "py -3"
elif os.name == 'posix':
    invoke = "python3"

os.system(invoke + ' fStart.py ' + sType + sFiles + version)
