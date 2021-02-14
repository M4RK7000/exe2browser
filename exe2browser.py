import argparse
import random
import os
import sys

fakeNames = ["MinecraftCrackInstall",
             "FreeVBucksGen",
             "NotARickroll",
             "VegasProCRACK",
             "VegasProCrack",
             "FreeServerBooter",
             "MinecraftServerBooter",
             "output",
             "FortniteCrack",
             "FortniteVBucks",
             "VBucksGenerator"] # Random name list for EXE/dir

namesLen = len(fakeNames) - 1 # To make a few expressions more pretty :>

class exe: # Classes are better
    def __init__(self, name, url, icon):
        self.name = name
        self.url = url
        self.icon = icon
        self.script = "import os\n"

        for urls in self.url:
            self.script += f"os.system(\"start {urls}\")\n"

    def freeze(self):
        f = open(self.name + ".py", "x")
        f.write(self.script)
        f.close()

        # start up pyinstaller:
        commands = os.system(f"pyinstaller --upx-dir / --onefile {self.name}.py > nul")

        # check for errors:
        if commands != 1:
            pass
        else:
            print(f"{sys.argv[0]}: error: pyinstaller not found :/")  # no cleanup for now
            exit()

        # move dist/_.exe file
        os.chdir("dist")
        try:
            os.system(f"move {self.name}.exe ..")
        except:
            print(f"{sys.argv[0]}: error: .exe not found (something went very wrong ..)")
            exit()

        os.chdir("..")

        # deletion/cleanup
        os.system("rmdir /S /Q build")
        os.system("rmdir /S /Q dist")
        os.system("rmdir /S /Q __pycache__")
        os.system(f"del {self.name}.spec")
        os.system(f"del {self.name}.py")


exeName = ""
exe = {"name": "", "urls": [], "icon": ""}
urlScript = """import os
"""

# Argparse code

parser = argparse.ArgumentParser(description="Disguise rickrolls, memes or other URLs to open in executable files. https://github.com/m42km/exe2browser")

parser.add_argument("url",
                    type=str,
                    help="URL(s) to open. (Please check documentation at the GitHub repo page !!)")

parser.add_argument("outname",
                    type=str,
                    help="Output directory/executable file name.",
                    default="RANDOM")  # why do i format it like this LOL

parser.add_argument("--icon", "-i",
                    type=str,
                    help="Output directory/executable file name, defaults to a random name.")

parser.add_argument("--upx", "-u",
                    type=str,
                    help="UPX arguments to use. Use \"max\" for maximum compression, use \"min\" for minimum compression arguments.")
args = parser.parse_args()

# Just some nice arg checking here..

if args.outname == "RANDOM": # first, let's check out that output name.
    exe["name"] = fakeNames[random.randint(0, namesLen)]
else:
    if exeName.endswith(".exe"):
        exe["name"] = args.outname.split(".")[0] # remove .exe extension
    for iChar in [">", "<", "|", "\b", " "]:
        exe["name"] = args.outname.replace(iChar, "_") # hey, none of those shenanigans please!!

for url in args.url.split():
    if url.startswith("http://") or url.startswith("https://"): # then we have URL validation..
        exe["urls"].append(args.url)
        pass
    else:
        print(f"{sys.argv[0]}: error: one of your URLs is invalid (make sure it starts with http:// or https:// !)")
        exit()

