import discord
import os
from keep_alive import keep_alive

client =  discord.Client(activity=discord.Activity(type=discord.ActivityType.watching, name="Metricate's server | m!faq"))

@client.event
async def on_ready():
    print("Logged in as {0.user}".format(client))
 

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if 'hardcore world' in message.content:
        await message.channel.send("It's not being released due to personal reasons, however the seed will be released. Also please dont ask for the world download 🤗")
    if 'texture' in message.content:
        await message.channel.send('Metricate uses Vanilla tweaks which can be found here: https://vanillatweaks.net/picker/resource-packs/')
    async def on_member_join(member):
        await member.send("Welcome to Metricate's discord server, to view some of the frequently asked questions, just do m!faq")
    if message.content.startswith('m!faq'):
      embed=discord.Embed(title="Frequently Asked Questions", description="These are the most asked questions on this discord", color=0x00ffee)
      embed.set_thumbnail(url='https://yt3.ggpht.com/ytc/AKedOLR2XRSKFE01okbKZGA_x9RIIbAybU8ZlLjvymeNrg=s900-c-k-c0x00ffffff-no-rj')
      embed.add_field(name="What texture pack does metricate use?", value="He uses a mixture of packs from Vanilla Tweaks and Jerms Better Leaves texture pack.", inline=False)
      embed.add_field(name="Where can I download his hardcore world", value="It's not being released due to personal reasons, however the seed will be released. Also please dont ask for the world download 🤗", inline=False)
      embed.add_field(name="What Recording software and editing software does he use", value="He uses OBS Studio to record & stream, and edits his videos with Adobe Premiere Pro", inline=False)
      embed.add_field(name="Can I play with Metricate?", value="He doesn’t currently play with viewers on or off stream. This is something he is planning to change though at some point. As to when he doesn't know. It is something he has in mind for the future", inline=False)
      embed.add_field(name="Where can I DM Metricate", value="His DM's are closed everywhere, and he only DM's people he knows. If you want to contact staff please open up a ticket after reading the <#776874923749670963> or you can contact him via his business email, metricate.contact@gmail.com", inline=True)
      embed.set_footer(text="Developed by Wadairity#0706")
      await message.channel.send(embed=embed)

keep_alive()
client.run(os.getenv('TOKEN'))
