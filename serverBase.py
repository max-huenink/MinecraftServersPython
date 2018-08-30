import sys
import os
import glob

def declare_server_variables():
    global sFiles
    global dirs
    global serverType
    global server
    global start

    if 1 < len(sys.argv):
        serverType = sys.argv[1].upper()[0]
    else:
        print('Server Types include: Reg, Snap, Forge, Bukkit')
        serverType = input('Server Type: ').upper()[0]
        if serverType == '':
            serverType = 'R'

    import var
    sFiles = var.sFiles
    if serverType == 'R' or serverType == 'S':
        dirs = var.dirsVANILLA
    elif serverType == 'B':
        dirs = var.dirsBUKKIT
    elif serverType == 'F':
        dirs = var.dirsFORGE

declare_server_variables()

if 2 < len(sys.argv):
    server = sys.argv[2]
else:
    # print(os.listdir(dirs))
    for folder in os.listdir(dirs):
        print(folder),
    print('Which server would you like to start?')
    server = input('Server: ')

if 3 < len(sys.argv):
    start = sys.argv[3].lower()[0]
else:
    start = ''

def server_create(sName, sType):
    invoke = 'python3'
    if os.name == 'nt':
        invoke = "py -3"
    elif os.name == 'posix':
        invoke = "python3"
    os.system(invoke + ' ' + sFiles + 'base.py ' + sName + ' ' + sType)

os.chdir(dirs)

if os.path.isdir(os.path.join(dirs, server)):
    os.chdir(os.path.join(dirs, server))
    if start == '':
        for x in glob.glob('*.sh'):
            print(x)
        for y in glob.glob('*.py'):
            print(y)
        print("Which (type)Start file would you like to use?")
        start = input('Type: ').lower()[0]
    if serverType == "R":
        if start == "r":
            import regStart
        elif start == "l":
            import legacyStart
        elif start == "s":
            import snapshotStart
        elif start == "c":
            import cleanStart
        elif start == "b":
            import backupStart
    elif serverType == "F":
        if start == "r":
            import regForgeStart
        elif start == "c":
            import cleanForgeStart
        elif start == "b":
            import backupForgeStart
    elif serverType == "B":
        if start == "r":
            import regBukkitStart
        elif start == "c":
            import cleanBukkitStart
        elif start == "b":
            import backupBukkitStart
elif server == "new":
    print("Making a new regular server")
    serverType = 'reg'
    server_create('', serverType)
elif server == "newS":
    print("Making a new snapshot server")
    serverType = 'snap'
    server_create('', serverType)
elif server == "newD":
    print("Making a new downloaded server")
    serverType = 'downReg'
    server_create('', serverType)
elif server == "newDS":
    print("Making a new downloaded snapshot server")
    serverType = 'downSnap'
    server_create('', serverType)
elif server == "newF":
    print("Making a new forge server")
    serverType = 'forge'
    server_create('', serverType)
elif server == "newDF":
    print("Making a new downloaded forge server")
    serverType = 'downForge'
    server_create('', serverType)
elif server == "newB":
    print("Making a new bukkit server")
    serverType = 'bukkit'
    server_create('', serverType)
elif server == "newDB":
    print("Making a new downloaded bukkit server")
    serverType = 'downBukkit'
    server_create('', serverType)
else:
    print("Server %s does not exist, would you like to create it?" % server)
    create = input("Create? (Y/[N]): ")
    if create == '':
        create = 'N'
    create = create.upper()[0]
    if create == 'Y':
        print("What type of server?")
        print("Regular, Snapshot, Forge, Bukkit")
        styp = input('Type: ').lower()[0]
        down = input('Downloaded (y/[n]): ')
        if down == '':
            down = 'n'
        down = down.lower()[0]

        if styp == 'r':
            serverType = 'reg'
        elif styp == 's':
            serverType = 'snap'
        elif styp == 'f':
            serverType = 'forge'
        elif styp == 'b':
            serverType = 'bukkit'
        elif styp == 'r' and down == 'y':
            serverType = 'downReg'
        elif styp == 's' and down == 'y':
            serverType = 'downSnap'
        elif styp == 'f' and down == 'y':
            serverType = 'downForge'
        elif styp == 'b' and down == 'y':
            serverType = 'downBukkit'
        server_create(server, serverType)
