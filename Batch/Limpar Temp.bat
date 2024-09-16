@echo off
pushd "C:\Windows\Temp" && (rd /s /q "C:\Windows\Temp" 2>nul & popd)
echo Limpando C:\Users\%USERNAME%\AppData\Local\Temp...
pushd "C:\Users\%USERNAME%\AppData\Local\Temp" && (rd /s /q "C:\Users\%USERNAME%\AppData\Local\Temp" 2>nul & popd)
echo As pastas temporarias foram limpadas.
timeout /t 5
cls