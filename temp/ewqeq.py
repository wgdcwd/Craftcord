import discord
from datetime import datetime
 
TOKEN = 'MTE3NDc4MjUzODU3Nzg3NDk0NA.Ga6e6p.4eN5ylJ3po-I6Jq3Y9jU1esVyKuXyetAvvIrj4'
CHANNEL_ID = '1174781890067181652'
 
 
class MyClient(discord.Client):
    async def on_ready(self):
        print('Logged on as {0}!'.format(self.user))
        await self.change_presence(status=discord.Status.online, activity=discord.Game("대기중"))
 
 
intents = discord.Intents.default()
intents.message_content = True
client = MyClient(intents=intents)
client.run(TOKEN)