@echo off
title recherche de BatEdit
echo @echo off>>fichier.bat
If not exist "main.py" echo "Main.py is not found. Extract the file"
If exist "main.py" Python main.py
title BatEdit s'est fermé
cls
echo Merci d'utiliser BatEdit
echo Si BatEdit s'est arrête brusquement, cela pourrait s'agir d'un problème inconnu
pause>nul