import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

    channel_id = 1174781890067181652  # 원하는 채널 ID로 변경해야 합니다.
    channel = client.get_channel(channel_id)

    if channel:
        await channel.send('On')  # 'On' 메시지를 해당 채널에 보냅니다.

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('/this'):
        channel_id = message.channel.id
        await message.channel.send(f'The ID of this channel is: {channel_id}')

client.run('MTE3NDc4MjUzODU3Nzg3NDk0NA.Ga6e6p.4eN5ylJ3po-I6Jq3Y9jU1esVyKuXyetAvvIrj4')