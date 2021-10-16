import discord
import os
from keep_alive import keep_alive

client =  discord.Client(activity=discord.Game(name='Watching Metricates Server'))

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
 

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'hardcore world' in message.content:
        await message.channel.send('Sorry! But Metricates Hardcore World is limited to Patrons and Channel Members only!')
    if 'texture' in message.content:
        await message.channel.send('Metricate uses Vanilla tweaks which can be found here: https://vanillatweaks.net/picker/resource-packs/')


keep_alive()
client.run(os.getenv('TOKEN'))
