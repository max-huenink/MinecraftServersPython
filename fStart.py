import os
import sys

sType = sys.argv[1]
svFilesJ = sys.argv[2]
version = sys.argv[3]
ram = '-Xmx2G'

if sType == 'reg':
    os.system('java -jar ' + ram + ' ' + svFilesJ + '\\\\minecraft_server.' + version + '.jar nogui')
elif sType == 'snap':
    os.system('java -jar ' + ram + ' ' + svFilesJ + '\\\\minecraft_server.' + version + '.jar nogui')
elif sType == 'bukkit':
    os.system('java -jar ' + ram + ' ' + svFilesJ + '\\\\craftbukkit-dev' + version + '.jar nogui')
elif sType == 'forge':
    os.system('java -jar ' + ram + ' ' + svFilesJ + '\\\\forge-' + version + '-universal.jar nogui')
