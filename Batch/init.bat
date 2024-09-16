@echo off

if not [%1] == [] cd %1
if exist ".git" goto hasfolder

git init
git status

goto end

:hasfolder
echo A .git folder already exists.

:end

pause