import discord
import os
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
client =  discord.Client(intents=intents, activity=discord.Activity(type=discord.ActivityType.watching, name="Metricate's server | m!faq"))

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'hardcore world' in message.content.lower():
        await message.channel.send("It's not being released due to personal reasons, however the seed will be released. Also please dont ask for the world download 🤗")
    if 'join the smp' in message.content.lower():
      await message.channel.send('Sorry! But joining the SMP is on an invite only basis')
    if 'texture' in message.content.lower():
        await message.channel.send('Metricate uses Vanilla tweaks which can be found here: https://vanillatweaks.net/picker/resource-packs/')
    async def on_member_join(member):
        await member.send("Welcome to Metricate's discord server, to view some of the frequently asked questions, just do m!faq")
    if message.content.startswith('m!faq'):
      embed=discord.Embed(title="Frequently Asked Questions", url='https://www.youtube.com/c/Metricate/join', color=0x00e1ff)

    if 'join imperial' in message.content.lower():
      await message.channel.send('Sorry! But joining the SMP is on an invite only basis')
    if message.content.startswith('m!faq'):      
      embed.set_thumbnail(url='https://yt3.ggpht.com/ytc/AKedOLR2XRSKFE01okbKZGA_x9RIIbAybU8ZlLjvymeNrg=s900-c-k-c0x00ffffff-no-rj')
      embed.add_field(name="What texture pack does metricate use?", value="He uses a mixture of packs from Vanilla Tweaks and Jerms Better Leaves texture pack.", inline=False)
      embed.add_field(name="Where can I download his hardcore world", value="It's not being released due to personal reasons, however the seed will be released. Also please dont ask for the world download 🤗", inline=False)
      embed.add_field(name="What Recording software and editing software does he use", value="He uses OBS Studio to record & stream, and edits his videos with Adobe Premiere Pro", inline=False)
      embed.add_field(name="Can I play with Metricate?", value="He doesn’t currently play with viewers on or off stream. However, only Diamond and Netherite members on youtube can play with him on Minecraft once a month ", inline=False)
      embed.add_field(name="Where can I DM Metricate", value="His DM's are closed everywhere, and he only DM's people he knows. If you want to contact staff please open up a ticket after reading the <#776874923749670963> or you can contact him via his business email, metricate.contact@gmail.com", inline=False)
      embed.add_field(name="Can I join imperial / become staff", value="Sorry, but becoming a staff member or joining the smp is strictly on an invite only basis!", inline=False)
      embed.set_footer(text="Developed by Wadairity#0706")
      await message.channel.send(embed=embed)
    if message.content.startswith('m!credits'):
        await message.channel.send('This bot was developed by <@805472705771733012> for Metricate.')

@client.event
async def on_member_join(member):
  guild = client.get_guild(754740304942202913)
  channel = guild.get_channel(887703033885102160)
  await channel.send(f'Welcome to the server {member.mention}! :partying_face:')
  embed=discord.Embed(title="Welcome!", url='https://www.youtube.com/c/Metricate/join', description="Welcome to the Metricate discord server {member.mention} 🥳! Make sure to do m!faq to read all the frequently asked questions", color=0x00d9ff)
  embed.set_thumbnail(url='https://yt3.ggpht.com/ytc/AKedOLR2XRSKFE01okbKZGA_x9RIIbAybU8ZlLjvymeNrg=s900-c-k-c0x00ffffff-no-rj')
  embed.set_footer(text="Developed By Wadairity#0706")
  await member.send(embed=embed)


keep_alive()
client.run(os.getenv('TOKEN'))

