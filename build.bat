@echo off

cd %~dp0

set /p PATH=path: 

echo.
echo Converting to exe...

".venv/Scripts/pyinstaller" --onefile --noconsole --specpath ".\spec" "%PATH%"

echo.
echo Done!

pause