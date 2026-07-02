@echo off
REM
REM svg2ico Inkscape Extension Installer
REM Automatic installation script for Windows
REM

setlocal enabledelayedexpansion

echo.
echo svg2ico Inkscape Extension Installer
echo ======================================
echo.

REM Try to find Inkscape installation directory
set "INKSCAPE_DIR="
set "INKSCAPE_EXT_DIR="

REM Check Program Files (default installation)
if exist "C:\Program Files\Inkscape" (
    set "INKSCAPE_DIR=C:\Program Files\Inkscape"
) else if exist "C:\Program Files (x86)\Inkscape" (
    set "INKSCAPE_DIR=C:\Program Files (x86)\Inkscape"
) else (
    echo Error: Inkscape installation not found
    echo Please install Inkscape first, or specify the extensions folder manually
    echo.
    pause
    exit /b 1
)

set "INKSCAPE_EXT_DIR=!INKSCAPE_DIR!\share\extensions"

echo Inkscape directory found: !INKSCAPE_DIR!
echo Extensions directory: !INKSCAPE_EXT_DIR!
echo.

REM Check if extensions directory exists
if not exist "!INKSCAPE_EXT_DIR!" (
    echo Creating extensions directory...
    mkdir "!INKSCAPE_EXT_DIR!"
    if errorlevel 1 (
        echo Error: Could not create extensions directory
        pause
        exit /b 1
    )
)

REM Get the directory where the script is located
set "SCRIPT_DIR=%~dp0"

REM Copy extension files
echo Installing svg2ico extension files...
echo.

if not exist "!SCRIPT_DIR!svg2ico.py" (
    echo Error: svg2ico.py not found
    pause
    exit /b 1
)

if not exist "!SCRIPT_DIR!svg2ico.inx" (
    echo Error: svg2ico.inx not found
    pause
    exit /b 1
)

REM Copy files
copy "!SCRIPT_DIR!svg2ico.py" "!INKSCAPE_EXT_DIR!\svg2ico.py" >nul
if errorlevel 1 (
    echo Error: Could not copy svg2ico.py
    pause
    exit /b 1
)

copy "!SCRIPT_DIR!svg2ico.inx" "!INKSCAPE_EXT_DIR!\svg2ico.inx" >nul
if errorlevel 1 (
    echo Error: Could not copy svg2ico.inx
    pause
    exit /b 1
)

echo [OK] Extension files installed successfully
echo.

REM Check for Python 3
where python3 >nul 2>&1
if errorlevel 1 (
    echo Warning: Python 3 is not installed or not in PATH
    echo           The extension requires Python 3.6 or later
    echo.
) else (
    echo [OK] Python 3 found in PATH
    echo.
)

REM Check for Pillow
python3 -c "from PIL import Image" >nul 2>&1
if errorlevel 1 (
    echo Warning: Pillow (PIL) is not installed
    echo           Installing Pillow is required for the extension to work
    echo.
    echo Install it using:
    echo   pip install Pillow
    echo.
) else (
    echo [OK] Pillow is installed
    echo.
)

echo.
echo Installation complete!
echo Please restart Inkscape for the extension to appear in the menu.
echo.
echo To use svg2ico:
echo   1. Open or create an SVG file in Inkscape
echo   2. Go to Extensions ^> Export ^> SVG to ICO
echo   3. Select the desired size and output filename
echo   4. Click Apply
echo.
pause
