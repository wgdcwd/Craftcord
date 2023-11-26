import discord
from mctools import RCONClient
from pritemp import Private

private = Private()
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

# Minecraft 서버 정보
server_address = private.server_address
rcon_port = 25575
rcon_password = "1234"

# Discord 봇 정보
bot_token = private.bot_token
channel_id = 1174781890067181652  # 채널 ID로 변경해야 합니다.

def execute_minecraft_command(command):
    try:
        # RCON 연결
        with RCONClient(server_address, rcon_port) as rcon_client:
            if rcon_client.login("1234"):
                response = rcon_client.command(command)
                return response
    except Exception as e:
        return f"Error executing command: {e}"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!'):
        # Discord에서 !say 명령을 사용하면 Minecraft 서버에 /say hi 명령 전송
        minecraft_command = "say hi"
        response = execute_minecraft_command(minecraft_command)
        await message.channel.send(f'Minecraft 서버에 명령을 전송했습니다. 응답: {response}')

# 봇 실행
client.run(bot_token)
