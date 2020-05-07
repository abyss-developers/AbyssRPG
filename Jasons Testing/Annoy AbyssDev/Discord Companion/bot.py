import discord
from discord.ext import commands
import random

client = commands.Bot(command_prefix = '!')

@client.event
async def on_ready():
    print("Bot is up 'n runnin!")

@client.event
async def on_member_join(member):
    print("{} has joined the server.".format(member))

@client.event
async def on_member_remove(member):
    print("{} has left the server".format(member))

@client.command()
async def ping(ctx):
    await ctx.send('> `AbyssBOT:` Pong! {}ms'.format(round(client.latency * 1000)))

@client.command(aliases=['8ball', 'eightball'])
async def _8ball(ctx, *, question):  # The star means that you can take in like sentences with spaces
    responses = [
        'It is certian.',
        'It is decidedly so.',
        'Without a doubt.',
        'Yes - definitely.',
        'You may rely on it.',
        'No lmao bruh',
        'YES! Yes it will be true!',
        'As certian as Luverin\'s upload schedule.',
        'As certian as Nate\'s upload schedule.',
        'As certian as Kay uploading to the #art channel.',
        'As certian as Jason uploading to the #art channel.',
        'As certian as Jason uploading to the #coding channel.',
        'As certian as anyone uploading to the #the-actual-roleplay channel.']
    await ctx.send("> Question : {}\n> Answer: {}".format(question, random.choice(responses)))

@client.command()
async def kay(ctx, *, status):
    if status == "what are you up to":
        kayResponses = [
            "school again i hate school",
            "bruh stfu im playing mc",
            "im trying to draw but i gave up"
        ]
        await ctx.me.edit(nick="buyonegetonefree")
        await ctx.send("{}".format(random.choice(kayResponses)))
        await ctx.me.edit(nick="")

@client.command(aliases = ['purge'])
async def prune(ctx, amount=0):
    if amount <= 0:
        await ctx.send("> `AbyssBOT:` Missing Arguments: Amount (Usage: !prune/!purge <amount>) (or just ask jason lmao)")
    else:
        await ctx.channel.purge(limit=amount + 1)

@client.command()
async def kick(ctx, member : discord.Member, *, reason=None): # reads that object as a Member object from import discord
    await member.kick(reason=reason)
    print("{} was kicked for reason: {}".format(member, reason))
    await ctx.send("> `AbyssBOT:` {} was kicked for reason: {}".format(member, reason))

@client.command()
async def ban(ctx, member : discord.Member, *, reason=None): # reads that object as a Member object from import discord
    await member.ban(reason=reason)
    print("{} was banned for reason: {}".format(member, reason))
    await ctx.send("> `AbyssBOT:` {} was banned for reason: {}".format(member.mention, reason))

@client.command()
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send("> `AbyssBOT:` {} has been unbanned.".format(user.mention))
            return
    await ctx.send("> `AbyssBOT:` Cannot find banned user. (Usage: !unban <username#tag>) (Or once again, just ask Jason.)")

@client.command()
async def control(ctx):
    print("Control session started.")
    while True:
        x = input("BOT: ")
        if x == "quit":
            print("Control session stopped.")
            return
        await ctx.send(x)


client.run('NzA4MDEzMzI2MjE4ODIxNjY2.XrRo1g.qZSjGz8LCpYm5Eu6Ta5R7i2OyUM')
