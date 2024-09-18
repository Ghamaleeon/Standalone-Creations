@echo off

if not [%1] == [] cd %1
if not exist ".git" goto nofolder

echo Insert a command: (Example: add [name] [online-repository])
git remote -v

set /p choice=
git remote %choice%
git remote -v
goto end

:nofolder
echo No .git folder was found in the dragged folder.

:end

pause