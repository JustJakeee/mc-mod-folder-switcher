import os, shutil, configparser

config = configparser.ConfigParser()
config.read_file(open(r"config.cfg"))
fc = os.listdir("Folders/")
ff = "Folders/"
mf = config.get("config", "mod_folder_path")
running = False
clearConsole = lambda: os.system('cls' if os.name in ('nt', 'dos') else 'clear')

def run():
    running = True
    for x in range(len(fc)):
        print(str(x) + ": " + fc[x])

    ipt = int(input("What folder would you like to switch to?\n"))

    try:
        shutil.rmtree(mf)
    except FileNotFoundError:
        print("Bruhhh- Make a mod folder first :facepalm:")

    shutil.copytree(ff + fc[ipt], mf)
    clearConsole()
    running = False

while not running:
    run()