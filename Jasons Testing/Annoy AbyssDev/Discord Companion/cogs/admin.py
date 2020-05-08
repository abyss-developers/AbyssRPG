import discord
from discord.ext import commands

class admin(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command(aliases = ['purge'])
    async def prune(self, ctx, amount=0):
        if amount <= 0:
            await ctx.send("> `AbyssBOT:` Missing Arguments: Amount (Usage: !prune/!purge <amount>) (or just ask jason lmao)")
        else:
            await ctx.channel.purge(limit=amount + 1)
    
    @commands.command()
    async def kick(self, ctx, member : discord.Member, *, reason=None): # reads that object as a Member object from import discord
        await member.kick(reason=reason)
        print("{} was kicked for reason: {}".format(member, reason))
        await ctx.send("> `AbyssBOT:` {} was kicked for reason: {}".format(member, reason))

    @commands.command()
    async def ban(self, ctx, member : discord.Member, *, reason=None): # reads that object as a Member object from import discord
        await member.ban(reason=reason)
        print("{} was banned for reason: {}".format(member, reason))
        await ctx.send("> `AbyssBOT:` {} was banned for reason: {}".format(member.mention, reason))

    @commands.command()
    async def unban(self, ctx, *, member):
        banned_users = await ctx.guild.bans()
        member_name, member_discriminator = member.split('#')
        for ban_entry in banned_users:
            user = ban_entry.user
            if (user.name, user.discriminator) == (member_name, member_discriminator):
                await ctx.guild.unban(user)
                await ctx.send("> `AbyssBOT:` {} has been unbanned.".format(user.mention))
                return
        await ctx.send("> `AbyssBOT:` Cannot find banned user. (Usage: !unban <username#tag>) (Or once again, just ask Jason.)")

    @commands.command()
    async def control(self, ctx):
        print("Control session started.")
        while True:
            x = input("BOT: ")
            if x == "quit":
                print("Control session stopped.")
                return
            await ctx.send(x)

def setup(client):
    client.add_cog(admin(client))

if __name__ == "__main__":
    print("You ran the wrong thing! Rookie mistake. lmao")