@echo off

:mainMenu
cls
echo 1. ��������
echo 2. ��������
echo 3. ����
echo 4. ����
set /p choice=���ϴ� ��ȣ�� �Է��ϼ���: 
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
    echo �߸��� �Է��Դϴ�. �ٽ� �Է��ϼ���.
    timeout /nobreak /t 1 >nul
    goto mainMenu
)

goto mainMenu

:runServer
echo ������ �����մϴ�.
cd craftcord
python starting_server.py
set python_exit_code=%errorlevel%
cd ..
if %python_exit_code% equ 0 (
    call start.bat
    cls
    echo ������ ����Ǿ����ϴ�.
    pause
) else (
    call start.bat
    cls
    echo eula.txt���� eula=false�� eula=true�� �ٲ��ּ���.
    pause
)
goto mainMenu

:serverSettings
echo ���� ������ �մϴ�.
cd craftcord
python setting_server.py
pause
cd ..
goto mainMenu

:showHelp
echo ������ ǥ���մϴ�.
rem ���� ǥ�ÿ� �ʿ��� �ڵ� �߰�
pause
goto mainMenu