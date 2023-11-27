@echo off

:mainMenu
cls
echo ! 서버실행을 한번도 한 적이 없으면 서버설정을 먼저 해주세요
echo 1. 서버실행
echo 2. 서버설정
echo 3. 도움말
echo 4. 종료
set /p choice=원하는 번호를 입력하시오: 

if "%choice%"=="1" (
    call :runServer
) else if "%choice%"=="2" (
    call :serverSettingsMenu
) else if "%choice%"=="3" (
    echo 여기는 3입니다.
    pause
    goto mainMenu
) else if "%choice%"=="4" (
    exit /b
) else (
    echo 잘못된 입력입니다. 다시 입력하세요.
    timeout /nobreak /t 2 >nul
    goto mainMenu
)

:runServer
echo #여긴 1번을 선택했을때 실행되는 코드입니다.
pause
goto mainMenu

:serverSettingsMenu
cls
echo 1. 서버자동설정
echo 2. 서버수동설정
echo 3. 서버설정확인
echo 4. 서버설정가이드
echo 5. 돌아가기
set /p choice=원하는 번호를 입력하시오: 

if "%choice%"=="1" (
    rem 서버 자동설정 코드
) else if "%choice%"=="2" (
    call :manualSettingsMenu
) else if "%choice%"=="3" (
    echo #2-3입니다
    pause
    goto serverSettingsMenu
) else if "%choice%"=="4" (
    echo #여기는 2-4입니다
    pause
    goto serverSettingsMenu
) else if "%choice%"=="5" (
    goto mainMenu
) else (
    echo 잘못된 입력입니다. 다시 입력하세요.
    timeout /nobreak /t 2 >nul
    goto serverSettingsMenu
)

:manualSettingsMenu
cls
echo 1. 디스코드 봇 토큰값 수정
echo 2. 디스코드 채널 아이디값 수정
echo 3. 서버주소 값 수정
echo 4. 서버포트 값 수정
echo 5. rcon포트 값 수정
echo 6. rcon비밀번호 값 수정
echo 7. 돌아가기
set /p choice=원하는 번호를 입력하시오: 

if "%choice%"=="1" (
    rem 디스코드 봇 토큰 수정 코드
) else if "%choice%"=="2" (
    rem 디스코드 채널 아이디값 수정 코드
) else if "%choice%"=="3" (
    rem 서버주소 값 수정 코드
) else if "%choice%"=="4" (
    rem 서버포트 값 수정 코드
) else if "%choice%"=="5" (
    rem rcon포트 값 수정 코드
) else if "%choice%"=="6" (
    rem rcon비밀번호 값 수정 코드
) else if "%choice%"=="7" (
    goto serverSettingsMenu
) else (
    echo 잘못된 입력입니다. 다시 입력하세요.
    timeout /nobreak /t 2 >nul
    goto manualSettingsMenu
)

goto mainMenu