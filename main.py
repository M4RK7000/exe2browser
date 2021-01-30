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

"""Argparse code."""

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

"""Just some nice arg checking here."""

if args.outname == "RANDOM":
    exeName = fakeNames[random.randint(0, namesLen)]
else:
    exeName = args.outname


