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
    call start.bat
    cls
    echo 서버가 종료되었습니다.
    pause
) else (
    call start.bat
    cls
    echo eula.txt에서 eula=false를 eula=true로 바꿔주세요.
    pause
)
goto mainMenu

:serverSettings
echo 서버 설정을 합니다.
cd craftcord
python setting_server.py
pause
cd ..
goto mainMenu

:showHelp
echo 도움말을 표시합니다.
rem 도움말 표시에 필요한 코드 추가
pause
goto mainMenu