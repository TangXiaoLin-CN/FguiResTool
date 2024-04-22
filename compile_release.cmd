@echo off
set CUR=%~dp0
pyinstaller -D -w -i icon.ico --clean --win-private-assemblies -F FguiResTool.py 
pause