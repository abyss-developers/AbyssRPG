import discord
from discord.ext import commands
import random
import asyncio

class misc(commands.Cog):
    def __init__(self, client):
        self.client = client

    # events
    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("{} has joined the server.".format(member))

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print("{} has left the server.".format(member))
    
    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        self.message_id = payload.message_id
        if self.message_id == 709664558050050168:
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.client.guilds)
            member = discord.utils.find(lambda m : m.id == payload.user_id, guild.members)
            if payload.emoji.name == '🔴':
                role = discord.utils.get(guild.roles, name='Red')
                await member.add_roles(role)
            if payload.emoji.name == '🩸':
                role = discord.utils.get(guild.roles, name='Scarlet')
                await member.add_roles(role)
            if payload.emoji.name == '🟠':
                role = discord.utils.get(guild.roles, name='Orange')
                await member.add_roles(role)
            if payload.emoji.name == '🟡':
                role = discord.utils.get(guild.roles, name='Yellow')
                await member.add_roles(role)
            if payload.emoji.name == '💴':
                role = discord.utils.get(guild.roles, name='Light yellow')
                await member.add_roles(role)
            if payload.emoji.name == '🥬':
                role = discord.utils.get(guild.roles, name='Electric green')
                await member.add_roles(role)
            if payload.emoji.name == '🟢':
                role = discord.utils.get(guild.roles, name='Green')
                await member.add_roles(role)
            if payload.emoji.name == '👥':
                role = discord.utils.get(guild.roles, name='Teal')
                await member.add_roles(role)
            if payload.emoji.name == '🟦':
                role = discord.utils.get(guild.roles, name='Light blue')
                await member.add_roles(role)
            if payload.emoji.name == '️🍶':
                role = discord.utils.get(guild.roles, name='Blue')
                await member.add_roles(role)
                print("lol")
            if payload.emoji.name == '🟣':
                role = discord.utils.get(guild.roles, name='Light purple')
                await member.add_roles(role)
            if payload.emoji.name == '🍇':
                role = discord.utils.get(guild.roles, name='Purple')
                await member.add_roles(role)
            if payload.emoji.name == '🐖':
                role = discord.utils.get(guild.roles, name='Pink')
                await member.add_roles(role)
                
                
              

    # commands
    @commands.command()
    async def ping(self, ctx):
        await ctx.send('> `AbyssBOT:` Pong! {}ms'.format(round(self.client.latency * 1000)))
    
    @commands.command(aliases=['8ball', 'eightball'])
    async def _8ball(self, ctx, *, question):  # The star means that you can take in like sentences with spaces
        responses = [
            'It is certain.',
            'It is decidedly so.',
            'Without a doubt.',
            'Yes - definitely.',
            'You may rely on it.',
            'No lmao bruh',
            'YES! Yes it will be true!',
            'As certain as Luverin\'s upload schedule.',
            'As certain as Nate\'s upload schedule.',
            'As certain as Kay uploading to the #art channel.',
            'As certain as Jason uploading to the #art channel.',
            'As certain as Jason uploading to the #coding channel.',
            'As certain as anyone uploading to the #the-actual-roleplay channel.',
            'No, but i love u too bb <33 0///0']
        await ctx.send("> Question : {}\n> Answer: {}".format(question, random.choice(responses)))

    @commands.command()
    async def annoy(self, ctx):
        script = ("lol")
        for x in script.split():
            await ctx.send(x)
            await asyncio.sleep(0.50)
        

    @commands.command()
    async def annoying(self, ctx):
        await ctx.send("> `AbyssBOT:` You, {}, are {}% annoying.".format(ctx.message.author, round(random.uniform(0,100))))

    @commands.command()
    async def schedule(self, ctx):
        x = input("Date: ")
        x1 = input("Item: ")
        x1a = input("Description: ")
        x2 = input("Item: ")
        x2a = input("Description: ")
        x3 = input("Item: ")
        x3a = input("Description: ")
        x4 = input("Item: ")
        x4a = input("Description: ")
        x5 = input("Item: ")
        x5a = input("Description: ")

        embed = discord.Embed(
            title = x,
            description = "Schedule for {}".format(x),
            colour = discord.Colour.blue()
        )

        embed.set_footer(text='Coded and designed by Jason!')
        embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/695088637167140888/708149018534084648/original.png')
        embed.set_author(name="Coded in Python by Jason")

        embed.add_field(name="{}".format(x1a), value="{}".format(x1), inline=True)
        embed.add_field(name="{}".format(x2a), value="{}".format(x2), inline=True)
        embed.add_field(name="{}".format(x3a), value="{}".format(x3), inline=True)
        embed.add_field(name="{}".format(x4a), value="{}".format(x4), inline=True)
        embed.add_field(name="{}".format(x5a), value="{}".format(x5), inline=True)

        await ctx.channel.purge(limit=1)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(misc(client))

if __name__ == "__main__":
    print("You ran the wrong thing! Rookie mistake. lmao")