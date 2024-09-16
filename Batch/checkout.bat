@echo off

if not [%1] == [] cd %1
if not exist ".git" goto nofolder

git log
echo Insert a git hash:

set /p choice=
git checkout %choice%
goto end

:nofolder
echo No .git folder was found in the dragged folder.

:end

pause