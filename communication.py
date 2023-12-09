#마인크래프트와 디스코드를 연결시켜주는 코드
import discord
import asyncio
import time
from mctools import RCONClient
from private import Private
import msg_converter

private = Private()
#마인크래프트 rcon 객체 생성
while True :
    try :
        rcon_client = RCONClient(private.vars["server_address"], private.vars["rcon_port"])
        rcon_client.login(private.vars["rcon_password"])
        print("minecraft is connected!")
        break
    except :
        time.sleep(10)
        continue

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
    print(f'discord bot is connected! : {client.user}')

#디스코드 봇이 메세지를 감지했을때 실행
@client.event
async def on_message(message):
    #디스코드 봇이 자기자신의 메세지에는 응답하지 않음
    if message.author == client.user:
        return
    
    if message.channel.id != int(private.vars["channel_id"]) :
        return

    if message.content[0] == "!" :
         minecraft_command = message.content[1:]
    else :
         minecraft_command = f'tellraw @a "{message.author.display_name} {message.content}"'
    response = execute_minecraft_command(minecraft_command)[0:-4].strip() # 공백, ANSI Escape Code 제거
    if response == False :
        await message.channel.send("error discord to minecraft")
    elif response == "" :
        pass
    elif response == "No player was found" :
        pass
    else :
        await message.channel.send(response)

#마인크래프트 서버 로그 읽고 디스코드에 출력하는 함수
async def read_minecraft_chat():

    with open("..\\logs\\latest.log", "r", encoding="utf-8") as file:
        # 파일의 끝으로 이동
        file.seek(0, 2)
        while True :
            channel = client.get_channel(int(private.vars["channel_id"]))
            await asyncio.sleep(1)
            if channel == None :
                continue
            else :
                print("discord channel is connected!")
                break
        while True:
            line = file.readline()
            if not line:
                # 파일이 갱신되지 않았으면 잠시 대기
                await asyncio.sleep(1)
                continue
            #로그를 읽고 알맞게 변환해서 디스코드 채널에 출력
            msg = msg_converter.convert_minecraft_msg(line)
            if msg != None :
                await channel.send(msg)


# Discord 봇 실행과 minecraft 서버 로그 읽기를 병렬로 실행
async def main():
    await asyncio.gather(
        client.start(private.vars["bot_token"]),
        read_minecraft_chat()
    )



# 이벤트 루프 시작
asyncio.run(main())