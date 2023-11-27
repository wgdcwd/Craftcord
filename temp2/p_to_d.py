import discord
import asyncio

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

async def get_user_input():
    while True:
        user_input = input('내용을 입력하세요: ')
        channel = client.get_channel(1178436506130595850)  # YOUR_CHANNEL_ID에 디스코드 채널의 ID를 넣어주세요.
        await channel.send(f'입력 내용: {user_input}')

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    await get_user_input()

client.run("MTE3NDc4MjUzODU3Nzg3NDk0NA.G0U0u7.rSM1lIeDxlfwdZHeZQRvjyb9eGRalscJYSHswQ")