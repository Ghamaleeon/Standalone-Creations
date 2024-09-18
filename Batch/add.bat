@echo off

if not [%1] == [] cd %1
if not exist ".git" goto nofolder

git status
set choice=-A
echo Insert a flag or some files: (Default: %choice%)

set /p choice=
git add %choice%
git status
goto end

:nofolder
echo No .git folder was found in the dragged folder.

:end

pause