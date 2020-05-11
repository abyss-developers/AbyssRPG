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
        script = ("Lyrics거리 위 텅 빈 듯한 이 느낌 (ridin' and rollin')열기로 가득 채워 reloading (ridin' and rollin')경계를 break break out어디든지 겨눠 봐이젠 우리가 방아쇨 당겨 잘 봐We're back no more brakes모두 다 sit back이젠 마주해 날 향한 scream오랜 기다림의 끝에 불을 붙여시동 거는 순간 it's game over yaTalk talk 어딜 가도Talk talk 내 얘기로다들 떠들썩해 (ridin' and rollin')찢어지는 듯한 마찰음 위로 난선을 넘어서시간을 자유롭게 ah ah ah ah더 뜨겁게 이 순간을 달궈Burn up the road날 넘어설 그때까지거리 위 텅 빈 듯한 이 느낌 (ridin' and rollin')열기로 가득 채워 reloading (ridin' and rollin')경계를 break break out어디든지 겨눠 봐이젠 우리가 방아쇨 당겨 잘 봐Ridin' and rollin' oh baby reloadingRidin' and rollin' oh baby reloading지금 우린 running (지금 우린 running)Reloading oh yea새롭게 날 채워 다시 (새롭게 날 채워 다시)Whip fast 거침없이 핸들 더 꺾어 (꺾어)붕 뜨는 몸은 마치Like a roller coaster (coaster)터질 듯 엑셀을 밟아봐We outta control ya yaWe won't stop the racing till it's over ya (let's go)Talk talk 어떤 말도Talk talk 이 순간 속우릴 설명 못 해 (ridin' and rollin')가장 눈부신 이 속도에 올라타모두 놀랄 그 장면 속 우릴 향해 oh oh oh oh몇 번이고 한곌 뛰어넘어Burn up the road다시 내일이 올 때까지심장 속 터질 듯한 energy (ridin' and rollin')끝까지 나를 던져 reloading (ridin' and rollin')기록은 break break out매번 갈아치워 가이젠 세상에 우릴 쏴 올려 잘 봐Ridin' and rollin' oh baby reloadingRidin' and rollin' oh baby reloading지금 우린 running (지금 우린 running)Reloading oh yea새롭게 날 채워 다시 (새롭게 날 채워 다시)눈 앞에 펼쳐진 세상을 봐 eh꿈꿔왔던 story 더는 꿈이 아냐새롭게 뜬 태양을 마주 봐Flying down the road (let's roll)도로 위로 가득한붉은 불빛들은 날멈춰 있으라지만Woah woah woah woah더는 같은 길을 향해가지 않아 이젠 switch my lane나만의 새로운 길을 만들어벗어나 rush hour심장 속 터질 듯한 energy (ridin' and rollin')끝까지 나를 던져 reloading (ridin' and rollin')기록은 break break out매번 갈아치워 가이젠 세상에 우릴 쏴 올려 잘 봐Ridin' and rollin' oh baby reloadingRidin' and rollin' oh baby reloading지금 우린 running (지금 우린 running)Reloading oh yea새롭게 날 채워 다시 (새롭게 날 채워 다시)")
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