import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    print(f'{message.author}로부터 메시지: {message.content}')



client.run("MTE3NDc4MjUzODU3Nzg3NDk0NA.G0U0u7.rSM1lIeDxlfwdZHeZQRvjyb9eGRalscJYSHswQ")