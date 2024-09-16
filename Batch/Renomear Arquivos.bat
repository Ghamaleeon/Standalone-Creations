@echo off

echo Insira o novo nome dos arquivos inseridos:
set /p name=
set count=0
for %%x in (%*) do Set /a count+=1
setlocal enabledelayedexpansion

for %%a in (%*) do (
	ren %%a %name%!count!%%~xa
	set /a count = !count! - 1
)