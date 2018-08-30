from datetime import datetime
date = datetime.now()
changes = input("Would you like to make settings changes? Y/[N]: ")
s2 = "1"
op_perm_lvl = "1"
s10 = "DEFAULT"
lvl_type = "DEFAULT"
s11 = ""
seed = ""
s12 = "false"
force_gm = "false"
s16 = "true"
npc_spawns = "true"
s17 = "true"
white_list = "true"
s18 = "true"
animal_spawns = "true"
s19 = "false"
hardcore = "false"
s24 = "1"
difficulty = "1"
s26 = "0"
gamemode = "0"
s27 = "5"
idle_timeout = "5"
s28 = "15"
max_players = "15"
s30 = "true"
monster_spawns = "true"
s31 = "true"
struct_gen = "true"
s33 = "0"
spawn_protect = "0"
def op_perm():
    global s2
    global op_perm_lvl
    print(' op_perm_lvl=\"1\"')
    print('     Operator Permission Level')
    print('     Value can be 1-4')
    print('         1 - Ops can bypass spawn protection')
    print('         2 - Ops can use /clear, /difficulty, /effect, /gamemode,\
    /gamerule, /give, /tp, and can edit command blocks')
    print('         3 - Ops can use /kick, /ban, /pardon, /op, and /deop')
    print('         4 - Ops can use /stop')
    s2 = input('op_perm_lvl=')
    if s2 == "":
        s2 = 1
    op_perm_lvl = s2
def level_type():
    global s10
    global lvl_type
    print(' lvl_type=\"DEFAULT\"')
    print('     The type of level that is generated')
    print('     Value can be:')
    print('         DEFAULT - Standard world with hills, valleys, water, etc.')
    print('         FLAT - (Or superflat) A flat world with no features meant for \
          building, villages, strongholds, and nether fortresses still generate')
    print('         LARGEBIOMES - Same as default, all biomes are larger')
    print('         AMPLIFIED - Same as default but world-generation height limit is increased')
    s10 = input('lvl_type=')
    if s10 != "":
        s10 = s10[0].upper()
        if s10 == "D":
            s10 = "DEFAULT"
        elif s10 == "F":
            s10 = "FLAT"
        elif s10 == "L":
            s10 = "LARGEBIOMES"
        elif s10 == "A":
            s10 = "AMPLIFIED"
        else:
            s10 = "DEFAULT"
        lvl_type = s10
def world_seed():
    global s11
    global seed
    print(' seed=\"\"')
    print('     The seed for the world')
    print('     Value can be anything')
    s11 = input('seed=')
    seed = s11
def f_gm():
    global s12
    global force_gm
    print(' force_gm="false"')
    print('     Force gamemode when user logs in')
    print('     Value can be true/false')
    s12 = input('force_gm=')
    if s12 != "":
        s12 = s12[0].upper()
        if s12 == "T":
            s12 = "true"
        elif s12 == "F":
            s12 = "false"
        force_gm = s12
def npc_spawn():
    global s16
    global npc_spawns
    print(' npc_spawns=\"true\"')
    print('     NPC spawning')
    print('     Value can be true/false')
    s16 = input('npc_spawns=')
    if s16 != "":
        s16 = s16[0].upper()
        if s16 == "T":
            s16 = "true"
        elif s16 == "F":
            s16 = "false"
        npc_spawns = s16
def wl():
    global s17
    global white_list
    print(' white_list=\"true\"')
    print('     White listing')
    print('     Value can be true/false')
    s17 = input('white_list=')
    if s17 != "":
        s17 = s17[0].upper()
        if s17 == "T":
            s17 = "true"
        elif s17 == "F":
            s17 = "false"
        white_list = s17
def animal_spawn():
    global s18
    global animal_spawns
    print(' animal_spawns=\"true\"')
    print('     Animal spawning')
    print('     Value can be true/false')
    s18 = input('animal_spawns=')
    if s18 != "":
        s18 = s18[0].upper()
        if s18 == "T":
            s18 = "true"
        elif s18 == "F":
            s18 = "false"
        animal_spawns = s18
def hard_core():
    global s19
    global hardcore
    print(' hardcore=\"false\"')
    print('     Hardcore mode')
    print('     Value can be true/false')
    s19 = input('hardcore=')
    if s19 != "":
        s19 = s19[0].upper()
        if s19 == "T":
            s19 = "true"
        elif s19 == "F":
            s19 = "false"
        hardcore = s19
def diff():
    global s24
    global difficulty
    print(' difficulty=\"1\"')
    print('     Game difficulty')
    print('     Value can be:')
    print('         0 = Peaceful')
    print('         1 = Easy')
    print('         2 = Normal')
    print('         3 = Hard')
    s24 = input('difficulty=')
    if s24 == "":
        s24 = 1
    difficulty = s24
def gm():
    global s26
    global gamemode
    print(' gamemode=\"0\"')
    print('     Gamemode')
    print('     Value can be:')
    print('         0 = Survival')
    print('         1 = Creative')
    print('         2 = Adventure')
    print('         3 = Spectator')
    s26 = input('gamemode=')
    if s26 == "":
        s26 = 0
    gamemode = s26
def timeout():
    global s27
    global idle_timeout
    print(' idle_timeout=\"5\"')
    print('     How long a player can be idle before being disconnected (in minutes)')
    print('     Value can be \"n\" (in minutes)')
    s27 = input('idle_timeout=')
    if s27 == "":
        s27 = 0
    idle_timeout = s27
def players():
    global s28
    global max_players
    print(' max_players=\"15\"')
    print('     Maximum players allowed on the server')
    print('     Value can be \"n\"')
    s28 = input('max_players=')
    if s28 == "":
        s28 = 15
    max_players = s28
def monster_spawn():
    global s30
    global monster_spawns
    print(' monster_spawns=\"true\"')
    print('     Monster spawning')
    print('     Value can be true/false')
    s30 = input('monster_spawns=')
    if s30 != "":
        s30 = s30[0].upper()
        if s30 == "T":
            s30 = "true"
        elif s30 == "F":
            s30 = "false"
        monster_spawns = s30
def structure_gen():
    global s31
    global struct_gen
    print(' struct_gen=\"true\"')
    print('     Structure generation')
    print('     Value can be true/false')
    s31 = input('struct_gen=')
    if s31 != "":
        s31 = s31[0].upper()
        if s31 == "T":
            s31 = "true"
        elif s31 == "F":
            s31 = "false"
        struct_gen = s31
def spawn_protection():
    global s33
    global spawn_protect
    print(' spawn_protect=\"0\"')
    print('     Spawn protection')
    print('     Value can be \"n\"')
    s33 = input('spawn_protect=')
    if s33 == "":
        s33 = 0
    spawn_protect = s33
if changes == '':
    changes = 'n'
changes = changes.upper()[0]
if changes == "Y":
    op_perm()
    level_type()
    world_seed()
    f_gm()
    npc_spawn()
    wl()
    animal_spawn()
    hard_core()
    diff()
    gm()
    timeout()
#    players()
    monster_spawn()
    structure_gen()
#    spawn_protection()
f = open('server.properties', 'a')
f.write('#Minecraft server properties\n')
f.write('#%s\n' % date)
f.write('generator-settings=\n')
f.write('op-permission-level=%s\n' % op_perm_lvl)
f.write('allow-nether=true\n')
f.write('level-name=world\n')
f.write('enable-query=true\n')
f.write('allow-flight=false\n')
f.write('announce-player-achievements=true\n')
f.write('server-port=25565\n')
f.write('max-world-size=29999984\n')
f.write('level-type=%s\n' % lvl_type)
f.write('enable-rcon=false\n')
f.write('level-seed=%s\n' % seed)
f.write('force-gamemode=%s\n' % force_gm)
f.write('server-ip=\n')
f.write('network-compression-threshold=256\n')
f.write('max-build-height=256\n')
f.write('spawn-npcs=%s\n' % npc_spawns)
f.write('white-list=%s\n' % white_list)
f.write('spawn-animals=%s\n' % animal_spawns)
f.write('hardcore=%s\n' % hardcore)
f.write('snooper-enabled=true\n')
f.write('resource-pack-sha1=\n')
f.write('online-mode=true\n')
f.write('resource-pack=\n')
f.write('pvp=true\n')
f.write('difficulty=%s\n' % difficulty)
f.write('enable-command-block=true\n')
f.write('gamemode=%s\n' % gamemode)
f.write('player-idle-timeout=%s\n' % idle_timeout)
f.write('max-players=%s\n' % max_players)
f.write('max-tick-time=60000\n')
f.write('spawn-monsters=%s\n' % monster_spawns)
f.write('generate-structures=%s\n' % struct_gen)
f.write('view-distance=10\n')
f.write('spawn-protection=%s\n' % spawn_protect)
f.write('motd=A Minecraft Server\n')
f.close()
