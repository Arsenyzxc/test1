@echo off
setlocal
set "ROOT=%~dp0.."
python "%ROOT%\main.py" --vfs-path "C:\Temp\myvfs" --script "%ROOT%\demo.script"
pause
