![](github-assets/exe2browser.png)

# exe2browser
**exe2browser** is a beta, Windows-only Python tool to disguise browser tabs/URLs in executable files.

### Checklist for v0.5

- [x] Add icon support
- [x] Add support for UPX
- [x] Add options file
- [x] Add support for multiple URLs to open
- [ ] Update documentation

## Documentation

### Setup

Run the `setup.bat` file, or just install `pyinstaller` using `pip` if that causes trouble.

Then, `cd` your way to the repo directory and you'll be set!

### Usage
```
positional arguments:
  url                   URL(s) to open, please seperate each URL by a space.
  output                Output directory/executable file name.

optional arguments:
  -h, --help            show this help message and exit
  --icon ICON, -i ICON  Icon for the .exe file (.ico or executables with proper icons are acceptable)
  --upx UPX, -u UPX     UPX arguments/compression preset to use. (e.g. -u max, -u "-8 --brute". 
                        check presets below!)

UPX presets:
    umax = "-b --ultra-brute --all-methods --all-filters"
    max = "-9 --ultra-brute"
    high = "-9 --brute"
    mod = "-5"
```
## Disclaimer

I) I do **not own** PyInstaller or any other projects used to make this program.

II) I am **not responsible** for any damage caused by this program.