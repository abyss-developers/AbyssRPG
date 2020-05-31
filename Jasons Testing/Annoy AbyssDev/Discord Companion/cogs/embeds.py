import discord
from discord.ext import commands

class embeds(commands.Cog):
    def __init__(self, client):
        self.client = client
    
    @commands.command()
    @commands.has_role('Admin')
    async def colorassigner(self, ctx):
        embed = discord.Embed(
            title = "Color Roles",
            description = "Choose the colors you would like!",
            colour = discord.Colour.blue()
        )
        embed.set_footer(text='Love from the AbyssDEV Team')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

        embed.add_field(name=":red_circle: Red", value="Use this emoji for red.")
        embed.add_field(name=":drop_of_blood: Scarlet", value="Use this emoji for scarlet.")
        embed.add_field(name=":orange_circle: Orange", value="Use this emoji for orange.")
        embed.add_field(name=":yellow_circle: Yellow", value="Use this emoji for yellow.")
        embed.add_field(name=":yen: Light yellow", value="Use this emoji for light yellow.")
        embed.add_field(name=":leafy_green: Electric green", value="Use this emoji for electric green.")
        embed.add_field(name=":green_circle: Green", value="Use this emoji for green.")
        embed.add_field(name=":busts_in_silhouette: Teal", value="Use this emoji for teal.")
        embed.add_field(name=":blue_square: Light blue", value="Use this emoji for light blue.")
        embed.add_field(name=":sake: Blue", value="Use this emoji for blue.")
        embed.add_field(name=":purple_circle: Light purple", value="Use this emoji for light purple.")
        embed.add_field(name=":grapes: Purple", value="Use this emoji for purple.")
        embed.add_field(name=":pig2: Pink", value="Use this emoji for pink.")

        await ctx.channel.purge(limit=1)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🔴')
        await msg.add_reaction('🩸')
        await msg.add_reaction('🟠')
        await msg.add_reaction('🟡')
        await msg.add_reaction('💴')
        await msg.add_reaction('🥬')
        await msg.add_reaction('🟢')
        await msg.add_reaction('👥')
        await msg.add_reaction('🟦')
        await msg.add_reaction('🍶')
        await msg.add_reaction('🟣')
        await msg.add_reaction('🍇')
        await msg.add_reaction('🐖')

    @commands.command()
    @commands.has_role('Admin')
    async def rolepicker(self, ctx):
        embed = discord.Embed(
            title = "Hobby Picker",
            description = "Choose the hobbies you would like!",
            colour = discord.Colour.blue()
        )
        embed.set_footer(text='Love from the AbyssDEV Team')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

        embed.add_field(name=":desktop: Programmer", value="Use this emoji for red.")
        embed.add_field(name=":pencil: Writer", value="Use this emoji for scarlet.")
        embed.add_field(name=":art: Artist", value="Use this emoji for orange.")

        await ctx.channel.purge(limit=1)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('🖥️')
        await msg.add_reaction('📝')
        await msg.add_reaction('🎨')

    @commands.command()
    @commands.has_role('Admin')
    async def pronounpicker(self, ctx):
        embed = discord.Embed(
            title = "Pronoun Picker",
            description = "Choose the pronoun(s) you would like!",
            colour = discord.Colour.blue()
        )
        embed.set_footer(text='Love from the AbyssDEV Team')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

        embed.add_field(name=":white_circle: they/them/theirs", value="Use this emoji for they/them/theirs.")
        embed.add_field(name=":blue_circle: he/him/his", value="Use this emoji for he/him/his.")
        embed.add_field(name=":red_circle: she/her/hers", value="Use this emoji for she/her/hers.")

        await ctx.channel.purge(limit=1)
        msg = await ctx.send(embed=embed)
        await msg.add_reaction('⚪')
        await msg.add_reaction('🔵')
        await msg.add_reaction('🔴')

    @commands.command()
    async def rules(self, ctx, parameter=0):
        if parameter == 1:
            embed = discord.Embed(
                title = "Rules",
                description = "Rule One",
                colour = discord.Colour.blue()
            )
            embed.set_footer(text='Love from the AbyssDEV Team')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

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
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

            embed.add_field(name="2: No NSFW content.", value="Please try not to say anything, or post anything NSFW at all. You CAN be suggestive, just don't outright say anything NSFW.")
            
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)

        if parameter == 3:
            embed = discord.Embed(
                title = "Rules",
                description = "Rule Three",
                colour = discord.Colour.blue()
            )
            embed.set_footer(text='Love from the AbyssDEV Team')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

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
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

            embed.add_field(name="4: Keep swearing moderated.", value="Swearing is fine, but try to keep it moderated, including no slurs, etc.")
            
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)

        if parameter == 5:
            embed = discord.Embed(
                title = "Rules",
                description = "Rule Five",
                colour = discord.Colour.blue()
            )
            embed.set_footer(text='Love from the AbyssDEV Team')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

            embed.add_field(name="5: Talk in respective channels.", value="Please leave any off topic chats to the off topic channel, bot comamnds to bot, adverts to advertisement etc.")
            
            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)


        if parameter == 0:
            embed = discord.Embed(
                title = "Rules",
                description = "Welcome to the AbyssDEV community server. These rules are meant to guide us, not to restrict us. If you have any questions, please contact a staff member. Anyways, lets get started!",
                colour = discord.Colour.blue()
            )
            embed.set_footer(text='Love from the AbyssDEV Team')
            embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

            embed.add_field(name="1: No spamming.", value="We would like to keep our chat relatively clean. Please try not to send the same like pieces of text repeadedly.")
            embed.add_field(name="2: No NSFW content.", value="Please try not to say anything, or post anything NSFW at all. You CAN be suggestive, just don't outright say anything NSFW.")
            embed.add_field(name="3: No harrassment or verbal abuse.", value="Playing around is fine, but please try to be weary of your words.")
            embed.add_field(name="4: Keep swearing moderated.", value="Swearing is fine, but try to keep it moderated, including no slurs, etc.")
            embed.add_field(name="5: Talk in respective channels.", value="Please leave any off topic chats to the off topic channel, bot comamnds to bot, adverts to advertisement etc.")
            
            embed2 = discord.Embed(
                title = "Additional Info",
                description = "Thank you for checking out our server! For any additional info, please do not hesitate to @ one of our admins/mods. We want this place to feel as safe as possible! \n\n To obtain access to the rest of the server, please click the **Red Circle**. This is to trick people who just breeze through the rules without reading them!",
                colour = discord.Colour.blue()
            )

            embed2.set_footer(text='Love from the AbyssDEV Team')
            embed2.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

            await ctx.channel.purge(limit=1)
            await ctx.send(embed=embed)
            msg = await ctx.send(embed=embed2)
            await msg.add_reaction('🟢')
            await msg.add_reaction('🔴')

    @commands.command()
    async def introduce(self, ctx):
        embed = discord.Embed(
            title = "Introduction",
            description = "Hello! I am AbyssBOT, a bot coded by Jason as a multimedia moderation bot. Hopefully you won't need to see me (unless its for fun!) I will see you around sometime, and if I am offline, that means Jason is an idiot or he is asleep.",
            colour = discord.Colour.blue()
        )
        embed.set_footer(text='Love from the AbyssDEV Team')
        embed.set_thumbnail(url='https://media.discordapp.net/attachments/715985032359182422/716537624763826226/Server_Icon_Abyss.png?width=671&height=684')

        embed.add_field(name="Social Media(s)", value="I have none! Just @ me or @jatgm#2482.")
        embed.add_field(name="Preferred name/nickname", value="AbyssBOT (with BOT all caps)")
        embed.add_field(name="Pronouns", value="I have no preference")
        embed.add_field(name="Any extra information: Something else you'd like for us to know about you?", value="I have one command that just completely shuts me down lmao")
        
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(embeds(client))

if __name__ == "__main__":
    print("You ran the wrong thing! Rookie mistake. lmao")