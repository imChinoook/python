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
