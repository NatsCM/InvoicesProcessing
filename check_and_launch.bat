@echo off
setlocal

echo 🐍 Checking Python installation...

python --version >nul 2>&1
IF %ERRORLEVEL% NEQ 0 (
    echo ❌ Python is not installed.

    REM If you have local .exe installer:
    if exist python-installer.exe (
        echo ▶️ Opening Python local installer...
        start python-installer.exe
    ) else (
        echo 🌐 Opening official Python download site...
        start https://www.python.org/downloads/windows/
    )

    pause
    exit /b
) else (
    echo ✅ Python detected.
)

echo 🛠 Running installation and program...

REM Continue the normal process
call launch.bat

endlocal
pause