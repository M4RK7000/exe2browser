import argparse
import random
import os
import sys
import glob

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
             "VBucksGenerator"]  # Random name list for EXE/dir

namesLen = len(fakeNames) - 1  # To make a few expressions more pretty :>

class Executable:  # Classes are better
    def __init__(self, name, urls, icon, upx_args):
        """Initialize the executable object."""
        self.name = name
        self.urls = urls
        self.icon = icon
        self.script = "import os\n"
        self.upxArgs = upx_args
        try:
            self.settings = open("e2b.ini").readline()
        except: # settings might not exist ..
            self.settings = "none"
        for o_url in self.urls:
            self.script += f"os.system(\"start {o_url}\")\n"

    def freeze(self):
        """Freeze (and compress if provided by user) the executable."""

        # generate script
        f = open(self.name + ".py", "x")
        f.write(self.script)
        f.close()

        # start up pyinstaller:

        commands = os.system(f"pyinstaller --upx-dir / --onefile --icon \"{self.icon}\" {self.name}.py")

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

        if self.settings == "none" and self.upxArgs != "NONE": # compression
            print(f"{sys.argv[0]}: warning: .ini file not found. searching for UPX instead..")
            if glob.glob("upx.exe") == []:
                print(f"{sys.argv[0]}: strict warning: UPX not found, keeping current uncompressed .exe.")
                exit()
            else:
                self.settings = "upx.exe"
                os.system("echo upx.exe > e2b.ini")
                os.system(f"{self.settings} {self.upxArgs} {self.name}.exe")
        elif self.settings != "none" and self.upxArgs != "NONE":
            print("")

exe = {"name": "", "urls": [], "icon": "", "upxArgs": ""}
urlScript = """import os
"""
upx = {"mod":"-5","high":"-9 --brute","max":"-9 --ultra-brute","umax":"-b --ultra-brute --all-methods --all-filters"}
# Argparse code

parser = argparse.ArgumentParser(
    description="Disguise rickrolls, memes or other URLs to open in executable files. https://github.com/m42km/exe2browser")

parser.add_argument("url",
                    type=str,
                    help="URL(s) to open. (Please check documentation at the GitHub repo page !!)")

parser.add_argument("output",
                    type=str,
                    help="Output directory/executable file name.",
                    default="RANDOM")  # why do i format it like this LOL

parser.add_argument("--icon", "-i",
                    type=str,
                    help="Icon for the .exe file (.ico or executables with proper icons are acceptable)",
                    default="NONE")

parser.add_argument("--upx", "-u",
                    type=str,
                    help="UPX arguments to use. Use \"max\" for maximum compression, use \"min\" for minimum compression arguments.",
                    default="NONE")
args = parser.parse_args()

# Just some nice arg checking here..

if args.outname == "RANDOM":  # first, let's check out that output name.
    exe["name"] = fakeNames[random.randint(0, namesLen)]
else:
    if args.outname.endswith(".exe"):
        exe["name"] = args.outname.split(".")[0]  # remove .exe extension
    for iChar in [">", "<", "|", "\b", " "]:
        exe["name"] = args.outname.replace(iChar, "_")  # hey, none of those shenanigans please!!

for url in args.url.split():
    if url.startswith("http://") or url.startswith("https://"):  # then we have URL validation..
        exe["urls"].append(args.url)
        pass
    else:
        print(f"{sys.argv[0]}: error: one of your URLs is invalid (make sure it starts with http:// or https:// !)")
        exit()

if args.icon == "NONE":  # After that we make sure the icon is valid
    pass
else:
    if os.path.isfile(args.icon):
        if args.icon.lower().endswith(".ico") or args.icon.lower().endswith(".exe"):
            pass
        else:
            print(f"{sys.argv[0]}: error: icon file is in an invalid format")
            exit()
    else:
        print(f"{sys.argv[0]}: error: icon file does not exist")
        exit()

if args.upxargs == "NONE":  # Finally we check UPX arguments, and that's it!
    pass
else:
    try:
        exe["upxArgs"] = upx[args.upxargs.lower()]
    except:
        if not args.upxargs.contains("-"):
            print(f"{sys.argv[0]}: strict warning: invalid UPX arguments preset. Keeping current uncompressed file.")
        else:
            exe["upxArgs"] = args.upxargs.lower()

finalExe = Executable(exe["name"], exe["urls"], exe["icon"], exe["upxArgs"])
try:
    finalExe.freeze()
except Exception as e:
    print(f"{sys.argv[0]}: error: Python error - {e}")
    exit()