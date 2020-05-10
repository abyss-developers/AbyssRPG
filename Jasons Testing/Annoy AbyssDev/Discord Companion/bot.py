import discord
from discord.ext import commands, tasks
from itertools import cycle
import os

client = commands.Bot(command_prefix = '!')
client.remove_command('quit')

statuses = cycle([
    '!kay | Be Nice!',
    '!8ball | Jason was here >:D',
    '!ping | Fork this on GitHub!',
    '!prune | Treat yourself!',
    '!purge | I love you! <3',
    "!help | Thank Jason! <3",
    "!annoying | Drink water!",
    'Made with Love by Jason (and feedback from Kay)'])

@tasks.loop(seconds=5)
async def change_status():
    await client.change_presence(status=discord.Status.dnd, activity=discord.Game(next(statuses)))

@client.event
async def on_ready():
    print("AbyssBOT is now online.")
    print("Coded by Jason, run on Python with Discord.py.")
    print("Please steal with permission!")
    change_status.start()

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingRequiredArgument):
        await ctx.send('> `AbyssBOT:` Please pass in all required arguments (or objects).')
    if isinstance(error, commands.CommandNotFound):
        print("{}: Invalid command used (or mistaken)".format(ctx.message.author))

@client.command(aliases=['bot-commands','commands'])
async def _botcommands(ctx):
    embed = discord.Embed(
        title = "Help",
        description = "These are the commands in the AbyssBOT bot! Make sure to ask Jason for any additional help.",
        colour = discord.Colour.blue()
    )

    embed.set_footer(text='Coded and designed by Jason!')
    embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/695088637167140888/708149018534084648/original.png')
    embed.set_author(name="Coded in Python by Jason")

    embed.add_field(name="!kay", value="Talk to Kay virtually!", inline=True)
    embed.add_field(name="!jason", value="Talk to Jason virtually!", inline=True)
    embed.add_field(name="!nate", value="Talk to Nate virtually!", inline=True)
    embed.add_field(name="!8ball", value="Play 8ball!", inline=True)
    embed.add_field(name="!ping", value="Shows bot latency (ping)", inline=True)
    embed.add_field(name="!prune", value="Prunes for you (and works!)", inline=True)
    embed.add_field(name="!annoying", value="Insecure? You're in luck!", inline=True)

    await ctx.send(embed=embed)

@client.command()
async def load(extention):
    client.load_extension("cogs.{}".format(extention))

@client.command()
async def unload(extention):
    client.unload_extension("cogs.{}".format(extention))

@client.command()
async def reload(extention):
    client.unload_extension("cogs.{}".format(extention))
    client.load_extension("cogs.{}".format(extention))

for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension("cogs.{}".format(filename[:-3])) # cuts example.py to example

