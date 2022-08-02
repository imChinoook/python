import discord
import os
import discord.ext
from discord.ext import commands
from keep_alive import keep_alive
import random


import asyncio

client = client = commands.Bot(command_prefix = 'm!') 
client.remove_command("help")




gifs = [
 "https://c.tenor.com/j0KEi6tfpRcAAAAC/minecraft-boxer.gif",
 "https://giffiles.alphacoders.com/136/13659.gif",
 "https://c.tenor.com/-HtgekCqZt0AAAAd/minecraft-villager.gif" 
]
hugs = [
  "https://c.tenor.com/OXCV_qL-V60AAAAM/mochi-peachcat-mochi.gif",
  "https://1stnews.com/wp-content/uploads/2019/10/Different-types-of-hugs-reveal-what-your-relationship-is-really-like.gif",
  "http://25.media.tumblr.com/tumblr_ma7l17EWnk1rq65rlo1_500.gif",
  "https://thumbs.gfycat.com/FrenchShimmeringAmericanmarten-size_restricted.gif"
]
talking = [
  "https://c.tenor.com/BqEIl80jagYAAAAd/xqcow-discord.gif",
  "https://media0.giphy.com/media/Q7LNc6oY2a7OqfMqr7/giphy.gif"
]

@client.event
async def on_ready():
  print("Logged in as {0.user}".format(client))
  await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name= "Metricate's Server | m!faq"))

@client.command()
async def gif(ctx):
  embed=discord.Embed(title="", color=0xff0000)
  embed.set_image(url=random.choice(gifs))
  await ctx.send(embed=embed)

@client.command()
async def hug(ctx,*, member):
  author_name = ctx.message.author.name
  await ctx.send(f"{author_name} has hugged {member}")
  embed=discord.Embed(title="", color=0xfe4de7)
  embed.set_image(url=random.choice(hugs))
  await ctx.send(embed=embed)



@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
  responses = ["It is certain.",
  "It is decidedly so.",
  "Without a doubt.",
  "Yes - definitely.",
  "You may rely on it.",
  "As I see it, yes.",
  "Most likely.",
  "Outlook good.",
  "Yes.",
  "Signs point to yes.",
  "Reply hazy, try again.",
  "Ask again later.",
  "Better not tell you now.",
  "Cannot predict now.",
  "Concentrate and ask again.",
  "Don't count on it.",
  "My reply is no.",
  "My sources say no.",
  "Outlook not so good.",
  "Very doubtful."]
  embed=discord.Embed(title=question, description=random.choice(responses), color=0x00eeff)
  await ctx.send(embed=embed)

@client.command(aliases=['developer'])
async def credits(ctx):
  embed=discord.Embed(title="Credits", url="https://www.github.com/imchinoook", description="Developed with ❤️ by Wayne#4389 for Metricate", color=0xff0000)
  embed.set_thumbnail(url="https://yt3.ggpht.com/PSHTIKxbjIPUibCbBONIy1SZs8GouSAG5hSYRz4iBTH2tF3PeXBeJSaYU_j64Vsp8xdPur1i=s88-c-k-c0x00ffffff-no-rj")
  await ctx.send(embed=embed)


@client.command(aliases=['questions'])
async def faq(ctx):
  embed=discord.Embed(title="Frequently Asked Questions", url='https://www.youtube.com/c/Metricate/join', color=0x00e1ff)

  embed.set_thumbnail(url='https://yt3.ggpht.com/ytc/AKedOLR2XRSKFE01okbKZGA_x9RIIbAybU8ZlLjvymeNrg=s900-c-k-c0x00ffffff-no-rj')
  embed.add_field(name="What texture pack does metricate use?", value="Metricate uses mixture of textures from Vanilla Tweaks", inline=False)
  embed.add_field(name="Where can I download Metricate's worlds", value="The world download is being released to Youtube Members & Patreon Supporters. I also kindly request that dont ask for the world download if you are not a patron / youtube member ", inline=False)
  embed.add_field(name="What Recording software and editing software does he use", value="He uses OBS Studio to record & stream, and edits his videos with Adobe Premiere Pro", inline=False)
  embed.add_field(name="Can I play with Metricate?", value="Metricate only plays with members that are either Iron Patrons or have Tier 2 access as a Youtube Member on his SMP, to find out how to become a Patron / Member please do m!support", inline=False)
  embed.add_field(name="Where can I DM Metricate", value="His DM's are closed everywhere, and he only DM's people he knows. If you want to contact staff please open up a ticket after reading the <#776874923749670963> or you can contact him via his business email, metricate.contact@gmail.com", inline=False)
  embed.add_field(name="Does Metricate have an Upload Schedule?",value="Metricate doesn't have either due to University and studying commitments. Sticking to a schedule is difficult as every week for me is different and busy. When videos are ready, they will be posted. Streams will become more frequent but videos will always take priority.")
  embed.add_field(name="Can I post on self promotion", value="Self Promotion is  available for all members now, however we ask that you post child-friendly content")
  await ctx.send(embed=embed)
@client.command(aliases=['patreon','membership'])
async def support(ctx):
  embed=discord.Embed(title="How do I support Metricate?",color=0x00bfff)
  embed.add_field(name="Youtube", value="Metricate's Youtube Membership can be accessed here: https://www.youtube.com/channel/UC7whwalXB4J01Dk1F5yN3AQ/join")
  embed.add_field(name="Patreon", value="Metricate's Patreon can be accessed here:  https://www.patreon.com/Metricate")
@client.command()
async def mods(ctx):
  embed=discord.Embed(title="What mods does Metricate use?",color=0x00bfff,description="**Metricate uses the following mods**")
  embed.add_field(name="Camera Utils")
  embed.add_field(name="Gamma Utils")
  embed.add_field(name="Litematica")
  embed.add_field(name="Replay Mod")
  embed.add_field(name="Sodium")
  embed.add_field(name="World Edit")
async def socials(ctx):
  embed=discord.Embed(title="Does Metricate use social media?",color=0x00bfff,description="**Metricate only uses the following platforms outside of Discord, Youtube & Twitch**")
  embed.add_field(name="Twitter",value="https://twitter.com/Metricate")
  embed.add_field(name="Instagram",value="https://www.instagram.com/metricatemc/")
@client.command(aliases=['texturepack'])
async def pack(ctx):
    embed=discord.Embed(title="Texture Pack", url="https://vanillatweaks.net/picker/resource-packs/", description="Metricate uses Vanilla tweaks", color=0x00bfff)
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AKedOLR2XRSKFE01okbKZGA_x9RIIbAybU8ZlLjvymeNrg=s900-c-k-c0x00ffffff-no-rj")
    embed.set_footer(text="Wayne#4389")
    await ctx.send(embed=embed)
@client.command()
async def help(ctx):
    embed=discord.Embed(title="Help Page", url="https://www.youtube.com/c/Metricate/join", color=0x00bfff)
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AKedOLR2XRSKFE01okbKZGA_x9RIIbAybU8ZlLjvymeNrg=s900-c-k-c0x00ffffff-no-rj")
    embed.add_field(name="m!help", value="Shows this page", inline=False)
    embed.add_field(name="m!faq", value="Shows the most frequently asked questions", inline=False)
    embed.add_field(name="m!rules", value="Shows the rules", inline=False)
    embed.add_field(name="m!credits", value="Shows the developer", inline=False)
    embed.add_field(name="m!pack", value="Shows what texture pack Metricate uses", inline=False)
    embed.add_field(name="m!8ball", value="Speak to the almighty 8ball!", inline=False)
    embed.add_field(name="m!gif", value="Want to see some epic minecraft gifs?", inline=False)
    embed.add_field(name="m!hug @user", value="Hug someone who could be feeling down", inline=False)
    embed.set_footer(text="Developed By Wayne#4389")
    await ctx.send(embed=embed)

@client.command()
async def rules(ctx):
  embed=discord.Embed(title="Rules", description="<#776874923749670963>", color=0x00ccff)
  embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AKedOLR2XRSKFE01okbKZGA_x9RIIbAybU8ZlLjvymeNrg=s900-c-k-c0x00ffffff-no-rj")
  embed.set_footer(text="Developed by Wayne#4389")
  await ctx.send(embed=embed)


@client.event
async def on_message(message):
  if 'do i level up' in message.content.lower():

    embed=discord.Embed(title="In order to level up, you need to talk more!", color=0x00ffd5)
    embed.set_image(url=random.choice(talking))

    await message.channel.send(embed=embed)
  if 'join the imperial smp' in message.content.lower():

    embed=discord.Embed(title="Can I join Imperial SMP?", description="Sorry, but becoming a staff member or joining the smp is strictly on an invite only basis!",color=0x00ffd5)
    embed.set_image(url='https://c.tenor.com/DMBiLJZqF7UAAAAC/invite-sad.gif')
    await message.channel.send(embed=embed)
  if 'join imperial smp' in message.content.lower():

    embed=discord.Embed(title="Can I join Imperial", description="Sorry, but joining the smp is strictly on an invite only basis!",color=0x00ffd5)
    embed.set_image(url='https://c.tenor.com/DMBiLJZqF7UAAAAC/invite-sad.gif')
    await message.channel.send(embed=embed)
  if 'how to level up' in message.content.lower():

    embed=discord.Embed(title="In order to level up, you need to talk more!", color=0x00ffd5)
    embed.set_image(url=random.choice(talking))

    await message.channel.send(embed=embed)
  banned_words = [
      "fuck",
      "shit",
      "piss",
      "cunt",
      "ass",
      "sod",
      "bastard",
      "bollocks",
      "wanker",
      "tosser",
      "asshole",
      "dick",
      "pussy",
      "bitch",
      "twat"
    
  ]
  if message.content.lower() in banned_words:
      print(f"{message.author} has said a naughty word")
      embed=discord.Embed(title="Huh?", description=f"{message.author}, you have been ***KICKED*** from the metricate server for swearing, you can join back but you have been warned", color=0xff9500)
      embed.set_image(url="https://cdn4.vectorstock.com/i/1000x1000/76/48/no-swearing-rubber-stamp-vector-13537648.jpg")
      await message.author.send(embed=embed)
      await message.guild.ban(message.author, reason="Swearing")
      await asyncio.sleep(1)
      await message.guild.unban(message.author)
      guild = client.get_guild(900461111780978719)
      channel = guild.get_channel(904799118067630100)
      await channel.send(f'Kicked {message.author} for "SWEARING"')      

  await client.process_commands(message)


@client.command(aliases=['k'])
@commands.has_permissions(kick_members = True)
async def kick(ctx,member: discord.Member,*, reason="No reason provided"):
  await member.kick(reason=reason)

  try: 
    embed=discord.Embed(title="Kicked!", description="You have been ***KICKED*** from the Metricate discord server!", color=0xff9500)
    embed.add_field(name="Reason", value=f"{reason}", inline=False)
    embed.set_footer(text="Developed by Wayne#4389")
    
    await ctx.send(f"{member} has been kicked")
    await member.send(embed=embed)
  except:
    await ctx.send(f"Reason could not be sent to {member} as DM's have been disabled")


@client.command(aliases=['b'])
@commands.has_permissions(ban_members = True)
async def ban(ctx,member: discord.Member,*, reason="No reason provided"):
  await member.ban(reason=reason)
  try:
    embed=discord.Embed(title="Banned!", description="You have been ***BANNED*** from the Metricate discord server!", color=0xff9500)
    embed.add_field(name="Reason", value=f"{reason}", inline=False)
    embed.set_footer(text="Developed by Wayne#4389")
    await member.send(embed=embed)

  except:
    await ctx.send(f"{member} could not be sent a reason as they have their DM's disabled")
  await ctx.send(f"{member} has been banned")
@client.command(aliases=['ub'])
@commands.has_permissions(ban_members = True)
async def unban(ctx,*,member):
  banned_users = await ctx.guild.bans()
  member_name, member_disc = member.split('#')

  for banned_entry in banned_users:
    user = banned_entry.user

    if (user.name, user.discriminator)==(member_name,member_disc):

      await ctx.guild.unban(user)
      await ctx.send(f"{member} has been unbanned!")
      return

  await ctx.send(f"{member} was not found or is invalid")









keep_alive()
client.run(os.environ['TOKEN'])
