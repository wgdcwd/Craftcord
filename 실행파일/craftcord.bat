@echo off

:mainMenu
cls
echo 1. 서버실행
echo 2. 서버설정
echo 3. 도움말
echo 4. 종료
set /p choice=원하는 번호를 입력하세요: 
cls

if "%choice%"=="1" (
    call :runServer
) else if "%choice%"=="2" (
    call :serverSettings
) else if "%choice%"=="3" (
    call :showHelp
) else if "%choice%"=="4" (
    exit /b
) else (
    echo 잘못된 입력입니다. 다시 입력하세요.
    timeout /nobreak /t 1 >nul
    goto mainMenu
)

goto mainMenu

:runServer
echo 서버를 실행합니다.
cd craftcord
python starting_server.py
set python_exit_code=%errorlevel%
cd ..
if %python_exit_code% equ 0 (
    cd craftcord
    call start.bat
    cls
    echo 서버가 종료되었습니다.
    cd ..
    pause
) else (
    cd craftcord
    call start.bat
    cls
    echo eula.txt에서 eula=false를 eula=true로 바꿔주세요.
    cd ..
    pause
)
goto mainMenu

:serverSettings
cd craftcord
python setting_server.py
cd ..
goto mainMenu

:showHelp
echo README.md를 읽어주세요!
start "" "https://github.com/wgdcwd/craftcord"
pause
goto mainMenu