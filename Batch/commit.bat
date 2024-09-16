@echo off

if not [%1] == [] cd %1
if not exist ".git" goto nofolder

git status
set choice=-m "Update"
echo Insert a flag: (Default: %choice%)

set /p choice=
git commit %choice%
goto end

:nofolder
echo No .git folder was found in the dragged folder.

:end

pause