echo off
set GTKDIR=F:\GTK
set PYDIR=F:\Python25
cd ..
rmdir /S /Q build
rmdir /S /Q dist
mkdir dist\etc
mkdir dist\lib
mkdir dist\share
%PYDIR%\python.exe setup.py py2exe
pause
xcopy %GTKDIR%\bin\*.dll dist /E /Y
xcopy %GTKDIR%\etc dist\etc /E
xcopy %GTKDIR%\lib dist\lib /E
xcopy %GTKDIR%\share dist\share /E
xcopy %PYDIR%\Lib\site-packages\enchant\lib dist\lib /E
xcopy %PYDIR%\Lib\site-packages\enchant\share dist\share /E
rmdir /S /Q dist\share\applications
rmdir /S /Q dist\share\gtk-2.0
rmdir /S /Q dist\share\gtkthemeselector
rmdir /S /Q dist\share\man
rem Remove unused translation files included in iso-codes.
for /R dist\share\locale %%f in (iso_3166_2.mo*) do del /Q %%f
for /R dist\share\locale %%f in (iso_4217.mo*) do del /Q %%f
for /R dist\share\locale %%f in (iso_639_3.mo*) do del /Q %%f
pause
