import discord
import os
from discord.ext import commands
from keep_alive import keep_alive
import random
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

@client.command()
async def slap(ctx,*, member):
  slap = [
  "https://c.tenor.com/k4_iBaFWIAYAAAAC/slapping.gif",
  "https://c.tenor.com/nAiuA2RdCIkAAAAM/baby-slap.gif",
  "https://media3.giphy.com/media/Vf39XQd9eS9YlZdwWo/200.gif",
  "https://static.wikia.nocookie.net/038b3e72-7077-4fd9-af55-ee885e06f82c",
  "https://media4.giphy.com/media/gSIz6gGLhguOY/200.gif"
  ]
  author_name = ctx.message.author.name
  await ctx.send(f"{author_name} has slapped {member}")
  embed=discord.Embed(title="", color=0xfe4de7)
  embed.set_image(url=random.choice(slap))
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
  embed=discord.Embed(title="Credits", url="https://www.github.com/imchinoook", description="Developed with ❤️ by Wadairity#0706 for Metricate", color=0xff0000)
  embed.set_thumbnail(url="https://yt3.ggpht.com/PSHTIKxbjIPUibCbBONIy1SZs8GouSAG5hSYRz4iBTH2tF3PeXBeJSaYU_j64Vsp8xdPur1i=s88-c-k-c0x00ffffff-no-rj")
  await ctx.send(embed=embed)


@client.command(aliases=['questions'])
async def faq(ctx):
  embed=discord.Embed(title="Frequently Asked Questions", url='https://www.youtube.com/c/Metricate/join', color=0x00e1ff)

  embed.set_thumbnail(url='https://yt3.ggpht.com/ytc/AKedOLR2XRSKFE01okbKZGA_x9RIIbAybU8ZlLjvymeNrg=s900-c-k-c0x00ffffff-no-rj')
  embed.add_field(name="What texture pack does metricate use?", value="He uses a mixture of packs from Vanilla Tweaks and Jerms Better Leaves texture pack.", inline=False)
  embed.add_field(name="Where can I download his hardcore world", value="It's not being released due to personal reasons, however the seed will be released. Also please dont ask for the world download 🤗", inline=False)
  embed.add_field(name="What Recording software and editing software does he use", value="He uses OBS Studio to record & stream, and edits his videos with Adobe Premiere Pro", inline=False)
  embed.add_field(name="Can I play with Metricate?", value="He doesn’t currently play with viewers on or off stream. However, only Diamond and Netherite members on youtube can play with him on Minecraft once a month ", inline=False)
  embed.add_field(name="Where can I DM Metricate", value="His DM's are closed everywhere, and he only DM's people he knows. If you want to contact staff please open up a ticket after reading the <#776874923749670963> or you can contact him via his business email, metricate.contact@gmail.com", inline=False)
  embed.add_field(name="Can I join imperial / become staff", value="Sorry, but becoming a staff member or joining the smp is strictly on an invite only basis!", inline=False)
  embed.add_field(name="Can I post on self promotion", value="Self Promotion is ONLY available for Server Boosters and the Imperial SMP members! Everyone else can read, but cannot send messages.")
  await ctx.send(embed=embed)
@client.command(aliases=['texturepack'])
async def pack(ctx):
    embed=discord.Embed(title="Texture Pack", url="https://vanillatweaks.net/picker/resource-packs/", description="Metricate uses Vanilla tweaks which can be found by clicking on the blue Texture Pack and Jerms Better Leaves texture pack.", color=0x00bfff)
    embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AKedOLR2XRSKFE01okbKZGA_x9RIIbAybU8ZlLjvymeNrg=s900-c-k-c0x00ffffff-no-rj")
    embed.set_footer(text="Developed By Wadairity#0706")
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
    embed.set_footer(text="Developed By Wadairity#0706")
    await ctx.send(embed=embed)

@client.command()
async def rules(ctx):
  embed=discord.Embed(title="Rules", description="<#776874923749670963>", color=0x00ccff)
  embed.set_thumbnail(url="https://yt3.ggpht.com/ytc/AKedOLR2XRSKFE01okbKZGA_x9RIIbAybU8ZlLjvymeNrg=s900-c-k-c0x00ffffff-no-rj")
  embed.set_footer(text="Developed by Wadairity#0706")
  await ctx.send(embed=embed)


keep_alive()
client.run(os.environ['TOKEN'])
