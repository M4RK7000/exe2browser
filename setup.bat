@echo off

echo          Setup for exe2browser
echo ==============================================
echo Please make sure you've installed python
echo before continuing! This will setup
echo pyinstaller and a setup file that exe2browser
echo uses.
pause
cls

echo Installing pyinstaller ..
pip install pyinstaller > nul
py -m pip install pyinstaller > nul
echo Creating option file..
echo upx.exe> e2b.ini
echo A file named e2b.ini has been placed in exe2browser's directory.
echo If you are using UPX for exe2browser, please open it and
pause