@echo off

if not [%1] == [] cd %1
if not exist ".git" goto nofolder

git remote -v
git branch -a
set choice=origin main
echo Insert a remote and a branch: (Default: %choice%)

set /p choice=
git pull %choice%
goto end

:nofolder
echo No .git folder was found in the dragged folder.

:end

pause