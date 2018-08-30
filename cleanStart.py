import os
import tarfile
import re
s = open("server.properties", "r")
lines = s.readlines()
W = ''
for i in lines:
    search = re.search('level-name=', i)
    if search:
        W = re.sub(r'\n', '', i)[11:]
s.close()

os.remove(W)

tar = tarfile.open(W + '.tar')
tar.extractall()
tar.close()

# zfile = zipfile.ZipFile(W + '.zip')
# zfile.extractall('.')

Fsty = open('sType', 'r')
sty = Fsty.readline(1)
# print(sty)
Fsty.close()

if sty == 'r':
    import regStart
elif sty == 's':
    import snapshotStart
elif sty == 'l':
    import legacyStart