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
            'As certian as anyone uploading to the #the-actual-roleplay channel.',
            'No, but i love u too bb <33 0///0']
        await ctx.send("> Question : {}\n> Answer: {}".format(question, random.choice(responses)))

    @commands.command()
    async def annoy(self, ctx):
        script = "According to all laws of aviation"
        for i in range(30):
            for x in script.split():
                await ctx.send(x)
                await asyncio.sleep(0.75)

def setup(client):
    client.add_cog(misc(client))

if __name__ == "__main__":
    print("You ran the wrong thing! Rookie mistake. lmao")