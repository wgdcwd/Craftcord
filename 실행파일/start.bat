@echo off

:mainMenu
cls
echo ! ���������� �ѹ��� �� ���� ������ ���������� ���� ���ּ���
echo 1. ��������
echo 2. ��������
echo 3. ����
echo 4. ����
set /p choice=���ϴ� ��ȣ�� �Է��Ͻÿ�: 

if "%choice%"=="1" (
    call :runServer
) else if "%choice%"=="2" (
    call :serverSettingsMenu
) else if "%choice%"=="3" (
    echo ����� 3�Դϴ�.
    pause
    goto mainMenu
) else if "%choice%"=="4" (
    exit /b
) else (
    echo �߸��� �Է��Դϴ�. �ٽ� �Է��ϼ���.
    timeout /nobreak /t 2 >nul
    goto mainMenu
)

:runServer
echo #���� 1���� ���������� ����Ǵ� �ڵ��Դϴ�.
pause
goto mainMenu

:serverSettingsMenu
cls
echo 1. �����ڵ�����
echo 2. ������������
echo 3. ��������Ȯ��
echo 4. �����������̵�
echo 5. ���ư���
set /p choice=���ϴ� ��ȣ�� �Է��Ͻÿ�: 

if "%choice%"=="1" (
    rem ���� �ڵ����� �ڵ�
) else if "%choice%"=="2" (
    call :manualSettingsMenu
) else if "%choice%"=="3" (
    echo #2-3�Դϴ�
    pause
    goto serverSettingsMenu
) else if "%choice%"=="4" (
    echo #����� 2-4�Դϴ�
    pause
    goto serverSettingsMenu
) else if "%choice%"=="5" (
    goto mainMenu
) else (
    echo �߸��� �Է��Դϴ�. �ٽ� �Է��ϼ���.
    timeout /nobreak /t 2 >nul
    goto serverSettingsMenu
)

:manualSettingsMenu
cls
echo 1. ���ڵ� �� ��ū�� ����
echo 2. ���ڵ� ä�� ���̵� ����
echo 3. �����ּ� �� ����
echo 4. ������Ʈ �� ����
echo 5. rcon��Ʈ �� ����
echo 6. rcon��й�ȣ �� ����
echo 7. ���ư���
set /p choice=���ϴ� ��ȣ�� �Է��Ͻÿ�: 

if "%choice%"=="1" (
    rem ���ڵ� �� ��ū ���� �ڵ�
) else if "%choice%"=="2" (
    rem ���ڵ� ä�� ���̵� ���� �ڵ�
) else if "%choice%"=="3" (
    rem �����ּ� �� ���� �ڵ�
) else if "%choice%"=="4" (
    rem ������Ʈ �� ���� �ڵ�
) else if "%choice%"=="5" (
    rem rcon��Ʈ �� ���� �ڵ�
) else if "%choice%"=="6" (
    rem rcon��й�ȣ �� ���� �ڵ�
) else if "%choice%"=="7" (
    goto serverSettingsMenu
) else (
    echo �߸��� �Է��Դϴ�. �ٽ� �Է��ϼ���.
    timeout /nobreak /t 2 >nul
    goto manualSettingsMenu
)

goto mainMenu