@echo off
setlocal
set "ROOT=%~dp0.."
python "%ROOT%\main.py" --script "%ROOT%\demo.script"
pause
