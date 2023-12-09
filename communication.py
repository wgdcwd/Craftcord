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
        time.sleep(1)
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
    #지정한 채널이 아니면 응답하지 않음
    if message.channel.id != int(private.vars["channel_id"]) :
        return
    
    #디스코드 채널에서 명령어를 사용했을 경우
    if message.content[0] == "!" : 
         minecraft_command = message.content[1:]
    #디스코드 채널에서 일반채팅을 사용했을 경우
    else : 
         minecraft_command = f'tellraw @a "<{message.author.display_name}> {message.content}"'

    response = execute_minecraft_command(minecraft_command)[0:-4].strip() #명령어를 실행 후 그에대한 응답을 받아옴. 그 후 공백, ANSI Escape Code 제거

    if response == False : # 오류가 난 경우
        await message.channel.send("error discord to minecraft")
    elif response == "" : # 응답이 없는 명령어의 경우
        pass
    elif response == "No player was found" : # 마인크래프트에 접속중인 플레이어가 없어서 디스코드 채널의 메세지가 마인크래프트에 출력되지 않는 경우
        pass
    else :
        await message.channel.send(response) # 명령어를 사용했을시 일반적인 경우

#마인크래프트 서버 로그 읽고 디스코드에 출력하는 함수
async def read_minecraft_chat():

    with open("..\\logs\\latest.log", "r", encoding="cp949") as file: # UTF-8로 읽을시에 한글을 사용하면 오류가남.
        # 파일의 끝으로 이동
        file.seek(0, 2)

        # 디스코드와 마인크래프트가 연결되기전에 client.get_channel을 하면 오류발생. 그래서 오류가안날때까지(연결될때까지) 재접속.
        while True : 
            channel = client.get_channel(int(private.vars["channel_id"]))
            await asyncio.sleep(1)
            if channel == None :
                continue
            else :
                print("discord channel is connected!")
                break

        # 마인크래프트의 로그를 읽어옴.
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