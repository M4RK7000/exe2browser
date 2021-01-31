import argparse
import random
import os
import sys

###############################################################################
# If you're reading this, I need more .exe names for the fakeNames list!      #
# Check out the issues page and make a new issue with label "add random name" #
###############################################################################

fakeNames = ["MinecraftCrackInstall",
             "FreeVBucksGen",
             "NotARickroll",
             "VegasProCRACK",
             "VegasProCrack",
             "FreeServerBooter",
             "MinecraftServerBooter",
             "JoeMama",
             "output",
             "FortniteCrack",
             "FortniteVBucks",
             "VBucksGenerator"] # Random name list for EXE/dir

namesLen = len(fakeNames) - 1 # To make a few expressions more pretty :>

exeName = ""

urlScript = """import os
os.system('start %s')
"""

# Argparse code

parser = argparse.ArgumentParser(description="Disguise rickrolls, memes or other URLs to open in executable files. https://github.com/M4RK7000/exe2browser")

parser.add_argument("url",
                    type=str,
                    help="URL to open.")

parser.add_argument("outname",
                    type=str,
                    help="Output directory/executable file name, defaults to a random name.",
                    default="RANDOM") 
                    # why do i format it like this LOL

args = parser.parse_args()

# Just some nice arg checking here


if args.outname == "RANDOM": # first, let's check out that output name.
    exeName = fakeNames[random.randint(0, namesLen)]
else:
    if exeName.endswith(".exe"):
        exeName = args.outname.split(".")[0] # remove .exe extension
    else:
        for ichar in [">", "<", "|", "\b", " "]:
            exeName = args.outname.replace(ichar, "_") # hey, none of those shenanigans please!!

url = args.url
if url.startswith("http://") or url.startswith("https://"): # then we have URL validation, all there is to it :)
    pass
else:
    print("%s: error: is invalid (make sure it starts with http:// or https:// !)" % sys.argv[0])
    exit()

# This is the part where the real stuff begins ..
# file&dir preparation

os.mkdir(exeName + "_exe") # just to make sure a system-reserved name like "con" is corrected

f = open(exeName + ".py", "x")
f.write(urlScript % (args.url))
f.close() # aight file script written

os.mkdir("%s_exe" % exeName) #
os.chdir("%s_exe" % exeName)

commands = os.system("python -m pyinstaller --onefile %s.py" % (exeName))

if commands == 1:
    commands = os.system("py -m pyinstaller --onefile %s.py" % (exeName))
else:
    pass # Thanks PlayboiNazzy for testing my man

os.chdir("tst")
os.system("move %s.exe .." % (exeName))
os.chdir("..")

os.system("rmdir /S /Q build") # deletion
os.system("rmdir /S /Q dist")
os.system("rmdir /S /Q __pycache__")
os.system("del %s.spec" % (exeName))
os.system("del %s.py" % (exeName))

os.chdir("move %s.exe .." % (exeName))