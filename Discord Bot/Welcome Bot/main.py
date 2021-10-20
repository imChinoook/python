import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

# CHECK IF BOT HAS PRESENCE INTENT ON https://discord.com/developers/applications/

intents = discord.Intents.default()
intents.members = True
client =  discord.Client(intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name="ENTER_STATUS"))


@client.event
async def on_member_join(member):
  guild = client.get_guild(ENTER_YOUR_SERVER_ID)
  channel = guild.get_channel(ENTER_WELCOME_CHANNEL)
  await channel.send(f'Welcome to the server {member.mention}! :partying_face:')
  embed=discord.Embed(title="Welcome!", url='ENTER_URL', description="ENTER_WELCOME_MESSAGE"
  embed.set_thumbnail(url='ENTER THUMBNAIL URL')
  embed.set_footer(text="Developed By Wadairity#0706")
  await member.send(embed=embed)

keep_alive()

# MAKE AN ENV ON REPL.IT OR RESPECTED HOST. IF NOT ON REPL REMOVE keep_alive()
client.run(os.getenv('TOKEN'))
