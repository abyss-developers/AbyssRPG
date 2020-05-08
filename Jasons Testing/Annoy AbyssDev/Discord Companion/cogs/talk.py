import discord
from discord.ext import commands
import random

class talk(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def kay(self, ctx, *, status=""):
        if status == "what are you up to":
            kayResponses = [
                "school again i hate school",
                "bruh stfu im playing mc",
                "im trying to draw but i gave up",
                "idk what are you doing",
                "nothing lmao"
            ]
            await ctx.me.edit(nick="buyonegetonefree")
            await ctx.send("{}".format(random.choice(kayResponses)))
            await ctx.me.edit(nick="")
        if status == "hi":
            kayResponses = [
                "hello",
                "HI",
                "hihi"
            ]
            await ctx.me.edit(nick="buyonegetonefree")
            await ctx.send("{}".format(random.choice(kayResponses)))
            await ctx.me.edit(nick="")
        if status == "how are you":
            kayResponses = [
                "im good :)",
                "bad",
                "good, u?",
                "Are you Real?"
            ]
            await ctx.me.edit(nick="buyonegetonefree")
            await ctx.send("{}".format(random.choice(kayResponses)))
            await ctx.me.edit(nick="")
        if status == "":
            await ctx.send("> `AbyssBOT:` Please put one of the three sentences. For more info, ask Jason.")

    @commands.command()
    async def jason(self, ctx, *, status=""):
        if status == "what are you up to":
            jasonResponses = [
                "Coding atm",
                "doing homework",
                "lmao bro idfk what im doing",
                "talking to u ;)",
                "probably playing league... HAHA BRO U THINK I PLAY LEAUGE"
            ]
            await ctx.me.edit(nick="jatgm")
            await ctx.send("{}".format(random.choice(jasonResponses)))
            await ctx.me.edit(nick="")
        if status == "hi":
            jasonResponses = [
                "hello",
                "ayo whassup",
                "hey"
            ]
            await ctx.me.edit(nick="jatgm")
            await ctx.send("{}".format(random.choice(jasonResponses)))
            await ctx.me.edit(nick="")
        if status == "how are you":
            jasonResponses = [
                "doing pretty well",
                "mmmm good",
                "bad bad bad",
                "AttributionError: EOF when reading a line (32,4)"
            ]
            await ctx.me.edit(nick="jatgm")
            await ctx.send("{}".format(random.choice(jasonResponses)))
            await ctx.me.edit(nick="")
        if status == "":
            await ctx.send("> `AbyssBOT:` Please put one of the three sentences. For more info, ask Jason.")

    @commands.command()
    async def nate(self, ctx, *, status=""):
        if status == "what are you up to":
            nateResponses = [
                "bumberger",
                "your dad",
                "a warm grapefruit with a hole in it"
            ]
            await ctx.me.edit(nick="kandydead")
            await ctx.send("{}".format(random.choice(nateResponses)))
            await ctx.me.edit(nick="")
        if status == "hi":
            nateResponses = [
                "helo",
                "ok",
                "r"
            ]
            await ctx.me.edit(nick="kandydead")
            await ctx.send("{}".format(random.choice(nateResponses)))
            await ctx.me.edit(nick="")
        if status == "how are you":
            nateResponses = [
                "i dont know",
                "tired",
                "in constant fear"
            ]
            await ctx.me.edit(nick="kandydead")
            await ctx.send("{}".format(random.choice(nateResponses)))
            await ctx.me.edit(nick="")
        if status == "":
            await ctx.send("> `AbyssBOT:` Please put one of the three sentences. For more info, ask Jason.")


def setup(client):
    client.add_cog(talk(client))

if __name__ == "__main__":
    print("You ran the wrong thing! Rookie mistake. lmao")