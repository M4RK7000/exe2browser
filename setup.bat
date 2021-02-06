@echo off

echo          Setup for exe2browser
echo ===========================================
echo If you've installed everything needed for
echo exe2browser, please close this window :)
echo If you only installed python, continue.
echo If you didn't install python, exit, install
echo Python and execute this file again.
pause
cls

echo Installing pyinstaller ..
echo ----------------------------------------------------
pip install pyinstaller > nul
py -m pip install pyinstaller > nul
echo Installation should be good, please continue.