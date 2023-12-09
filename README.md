# craftcord

craftcord는 마인크래프트 서버와 디스코드 간의 채팅 및 명령어 연동을 제공하는 프로젝트입니다.

## 기능

- 마인크래프트의 채팅을 디스코드에, 디스코드의 채팅을 마인크래프트 서버에 보내줍니다.
- 디스코드 채널에서 !를 사용해 마인크래프트 명령어를 사용할 수 있습니다. (ex. !op player, !tp palyer1 player2)
- 서버 프로그램 파일을 자동으로 인식합니다. jar파일의 이름이 server.jar이든 spigot1.20.3 이든 jar 파일이 하나만있으면 정상작동 됩니다.
- server.properties의 변수들을 디스코드 봇과 연결되게 자동으로 설정합니다. 사용자는 어떤 코드를 직접 수정하지 않아도 편하게 서버를 열 수 있습니다.

## 환경

- 해당 프로젝트는 windows10, Python 3.12.0에서 작성되었습니다.
- 프로젝트로 실행한 마인크래프트 버전은 1.20.2이며 서버프로그램으로 spigot이 사용되었습니다.
- 다른 환경이어도 구동이 될 수 있지만 windows10에 spigot 프로그램을 사용하는 것을 권장합니다.

## 설치

- pip install discord
- pip install mctools -참고: pip install discord 실행 시 추가 의존성이 자동으로 설치됩니다.
- 자세한 내용은 requirements.txt를 확인해주세요.

## 사용법

1. [디스코드 개발자 포탈](https://discord.com/developers/applications)에서 봇을 생성합니다. ![image1](/images/1.png)
2. SETTINGS에 Bot에서 Privileged Gateway Intents 에서 SERVER MEMBERS INTENT와 MESSAGE CONTENT INTENT를 활성화시켜줍니다.![image2](/images/2.png)
3. SETTINGS에 OAuth2에 URL Generator에서 SCOPES에 bot에 체크하고 밑에 뜨는 BOT PERMISSIONS에 Read Messages/View Channels, Send Messages에 체크하고 밑에 GENERATED URL로 이동해 디스코드 봇을 원하는 디스코드 서버에 초대합니다.![image3](/images/3.png)![image4](/images/4.png)
4. 마인크래프트 서버를 만들 폴더를 생성하고 그 안에 해당 프로젝트 파일과 마인크래프트 서버 프로그램(jar 파일. 예: spigot, craftbukkit) 을 넣습니다. 그리고 craftcord내에 실행파일 폴더에 있는 craftcord.bat을 jar 파일이 있는 곳으로 이동시킵니다. ![image5](/images/5.png)
5. [디스코드 개발자 포탈](https://discord.com/developers/applications)에 Bot에 Build-A-Bot 에서 Reset Token을 누르고 Token기억해둡니다.![image6](/images/6.png)
6. 봇을 초대한 디스코드 서버에 마인크래프트와 연동할 채널의 아이디를 기억해둡니다. ![image7](/images/7.png)
7. craftcord.bat을 실행시키고 서버설정에 들어갑니다. 그리고 서버자동설정으로 들어가 bot_token값과 channel_id값을 입력하고 나머지 값들을 알맞게 입력해줍니다.![image8](/images/8.png)
8. craftcord.bat의 처음으로 돌아와 서버실행을 하면 eula.txt를 수정하라는 안내가 나옵니다. 그러면 eula.txt를 열고 알맞게 수정한 후 다시 서버를 실행하면 연결이 완료됩니다. 그 후 별다른 변동사항이 없으면 서버실행 기능만 사용하면 됩니다.![image9](/images/9.png)

## 라이선스

[여기에 라이선스 정보를 입력하세요.]

## 문의

[여기에 문의할 수 있는 방법을 입력하세요.]
