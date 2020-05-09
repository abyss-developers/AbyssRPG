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
        script = ("Fill 'em with the venom and eliminate 'em Other words, I Minute Maid 'em I don't wanna hurt 'em, but I did, I'm in a fit of rage I'm murderin' again, nobody will evade I'm fittin' to kill 'em and dumpin' their fuckin' bodies in the lake Obliterating everything, incinerate a renegade I'm here to make anybody who want it with the pen afraid But don't nobody want it, but they're gonna get it anyway 'Cause I'm beginnin' to feel like I'm mentally ill I'm Attila, kill or be killed, I'm a killer bee, the vanilla gorilla You're bringin' the killer within me outta me You don't wanna be the enemy of the demon who entered me Or be on the receivin' end of me, what stupidity it'd be Every bit of me's the epitome of a spitter When I'm in the vicinity, motherfucker, you better duck Or you finna be dead the minute you run into me A hundred percent of you is a fifth of a percent of me I'm 'bout to fuckin' finish you, bitch, I'm unfadable You wanna battle, I'm available, I'm blown up like an inflatable I'm undebatable, I'm unavoidable, I'm unevadable I'm on the toilet bowl, I got a trailer full of money and I'm paid in full I'm not afraid to pull a—")
        for x in script.split():
            await ctx.send(x)
            await asyncio.sleep(0.50)

    @commands.command()
    async def annoying(self, ctx):
        await ctx.send("> `AbyssBOT:` You, {}, are {}\% annoying.".format(ctx.message.author, round(random.uniform(0,100))))

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