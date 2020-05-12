import discord
from discord.ext import commands

class embeds(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    async def rules(self, ctx, parameter=0):
        if parameter == 1:
            embed = discord.Embed(
                title = "Rules",
                description = "Rule One",
                colour = discord.Colour.blue()
            )
            embed.set_footer(text='Love from the AbyssDEV Team')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/695088637167140888/708149018534084648/original.png')

            embed.add_field(name="1: No spamming.", value="We would like to keep our chat relatively clean. Please try not to send the same like pieces of text repeadedly.")
            
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)

        if parameter == 2:
            embed = discord.Embed(
                title = "Rules",
                description = "Rule Two",
                colour = discord.Colour.blue()
            )
            embed.set_footer(text='Love from the AbyssDEV Team')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/695088637167140888/708149018534084648/original.png')

            embed.add_field(name="2: No NSFW content.", value="Although we aren't restricting you from saying (questionable) things, try not to send any NSFW images or media alike.")
            
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)

        if parameter == 3:
            embed = discord.Embed(
                title = "Rules",
                description = "Rule Three",
                colour = discord.Colour.blue()
            )
            embed.set_footer(text='Love from the AbyssDEV Team')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/695088637167140888/708149018534084648/original.png')

            embed.add_field(name="3: No harrassment or verbal abuse.", value="Playing around is fine, but please try to be weary of your words.")
            
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)

        if parameter == 4:
            embed = discord.Embed(
                title = "Rules",
                description = "Rule Four",
                colour = discord.Colour.blue()
            )
            embed.set_footer(text='Love from the AbyssDEV Team')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/695088637167140888/708149018534084648/original.png')

            embed.add_field(name="4: Keep swearing moderated.", value="Swearing is fine, but try to keep it moderated, including no slurs, etc.")
            
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)

        if parameter == 0:
            embed = discord.Embed(
                title = "Rules",
                description = "Welcome to the AbyssDEV community server. These rules are meant to guide us, not to restrict us. If you have any questions, please contact a staff member. Anyways, lets get started!",
                colour = discord.Colour.blue()
            )

            embed.set_footer(text='Love from the AbyssDEV Team')
            embed.set_thumbnail(url='https://cdn.discordapp.com/attachments/695088637167140888/708149018534084648/original.png')

            embed.add_field(name="1: No spamming.", value="We would like to keep our chat relatively clean. Please try not to send the same like pieces of text repeadedly.")
            embed.add_field(name="2: No NSFW content.", value="Although we aren't restricting you from saying (questionable) things, try not to send any NSFW images or media alike.")
            embed.add_field(name="3: No harrassment or verbal abuse.", value="Playing around is fine, but please try to be weary of your words.")
            embed.add_field(name="4: Keep swearing moderated.", value="Swearing is fine, but try to keep it moderated, including no slurs, etc.")
            
            embed2 = discord.Embed(
                title = "Additional Info",
                description = "Thank you for checking out our server! For any additional info, please do not hesitate to @ one of our admins/mods. We want this place to feel as safe as possible!",
                colour = discord.Colour.blue()
            )

            embed2.set_footer(text='Love from the AbyssDEV Team')
            embed2.set_thumbnail(url='https://cdn.discordapp.com/attachments/695088637167140888/708149018534084648/original.png')

            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)
            await ctx.send(embed=embed2)


def setup(client):
    client.add_cog(embeds(client))

if __name__ == "__main__":
    print("You ran the wrong thing! Rookie mistake. lmao")