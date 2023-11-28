import discord
import asyncio
from mctools import RCONClient
from private import Private

private = Private()
#마인크래프트 rcon 객체 생성
rcon_client = RCONClient("localhost", 25575)
rcon_client.login("1234")

#디스코드 봇 객체 생성
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

#마인크래프트 command 실행
def execute_minecraft_command(command):
    try:
        response = rcon_client.command(command)
        return response
    except Exception as e:
        return False

#디스코드 봇 실행시 실행
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

#디스코드 봇이 메세지를 감지했을때 실행
@client.event
async def on_message(message):
    #파이썬 터미널에서 테스트
    #print(f'{message.author}로부터 메시지: {message.content}')
    if message.author == client.user:
        return
    
    print(message.content)
    if message.content[0] == "!" :
        minecraft_command = message.content[1:]
    else :
        minecraft_command = f'tellraw @a "{message.author.display_name} {message.content}"'
    response = execute_minecraft_command(minecraft_command)
    print(response)
    if response == False :
        await message.channel.send("error discord to minecraft")

#마인크래프트 서버 로그 읽고 디스코드에 출력하는 함수
async def follow_minecraft_chat():
    try:
        with open("C:/Users/wgdcw/Desktop/pyminebot/logs/latest.log", "r", encoding="utf-8") as file:
            # 파일의 끝으로 이동
            file.seek(0, 2)

            while True:
                line = file.readline()
                if not line:
                    # 파일이 갱신되지 않았으면 잠시 대기
                    await asyncio.sleep(1)
                    continue
                
                #파이썬 터미널에서 테스트
                #print(line, end='')
                channel = client.get_channel(1178436506130595850)
                await channel.send(line)
    except Exception as e:
        print("error minecraft to discord")

# Discord 봇 실행과 minecraft 서버 로그 읽기를 병렬로 실행
async def main():
    await asyncio.gather(
        client.start(private.bot_token),
        follow_minecraft_chat()
    )

# 이벤트 루프 시작
asyncio.run(main())