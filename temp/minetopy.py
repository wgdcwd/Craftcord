import discord
from mctools import RCONClient

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
server_address = "your_minecraft_server_address"
rcon_port = 25575  # RCON 포트 (기본값은 25575)
rcon_password = "your_rcon_password"

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!minecraft_command'):
        # 여기서 'your_command'를 실행하고 결과를 가져옵니다.
        result = execute_minecraft_command('your_command')
        await message.channel.send(f'Minecraft 서버 명령 결과: {result}')

def execute_minecraft_command(command):
    try:
        # RCON 연결
        with RCONClient(server_address, rcon_port, rcon_password) as client:
            response = client.command(command)
        return response
    except Exception as e:
        return f"Error executing command: {e}"

# 봇을 실행합니다.
client.run('YOUR_BOT_TOKEN')