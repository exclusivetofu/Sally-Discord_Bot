import discord
from discord.ext import commands
import json

class CommunityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.sel1  = '1️⃣'
        self.sel2  = '2️⃣'
        self.sel3  = '3️⃣'

    @commands.slash_command(guild_ids = [776972325010407454])
    async def gamer( self, context, platform: discord.commands.Option(str, 'Your primary gaming platform', required = True, choices = ['Steam', 'Uplay', 'Epic', 'Battle.net', 'Xbox', 'PSN', 'Nintendo']), 
                                          tag: discord.commands.Option(str, 'How other people can add you', required = True)):
        file = open('MemberInfo/' + str(context.author.id) + ".json")
        memberInfo = json.load(file)
        print(memberInfo[0])

    @commands.slash_command(guild_ids = [776972325010407454])
    async def poll(
                    self,
                    context,
                    name: discord.commands.Option(str, 'The name for your poll', required = True),
                    size: discord.commands.Option(int, 'How many choices for your poll', required = True, choices = [2, 3]),
                    cho1: discord.commands.Option(str, 'First Choice for your poll', required = True),
                    cho2: discord.commands.Option(str, 'First Choice for your poll', required = True),
                    cho3: discord.commands.Option(str, 'First Choice for your poll', required = False, default = 'none'),   
                   ):
        if size == 2:
            embed = discord.Embed(title = context.author.display_name + ' has created a poll', description = name, color=0xff00ff)
            embed.add_field(name = '[' + self.sel1 + '] ' + cho1, value = 'Option 1', inline=False)
            embed.add_field(name = '[' + self.sel2 + '] ' + cho2, value = 'Option 2', inline=False)
        
            billboard = discord.utils.find(lambda c: c.id == 808100225721303041,
                                         self.bot.guilds[0].channels
                                         )
            poll = await billboard.send(embed=embed)
            await poll.add_reaction(self.sel1)
            await poll.add_reaction(self.sel2)

            return await context.respond("I've Posted your poll to the billboard")

        if size == 3:
            if cho3 == 'none':
                return await context.respond('A poll with the size of 3 must have 3 choices')

            embed = discord.Embed(title = context.author.display_name + ' has created a poll', description = name, color=0xff00ff)
            embed.add_field(name = '[' + self.sel1 + '] ' + cho1, value = 'Option 1', inline=False)
            embed.add_field(name = '[' + self.sel2 + '] ' + cho2, value = 'Option 2', inline=False)
            embed.add_field(name = '[' + self.sel3 + '] ' + cho3, value = 'Option 3', inline=False)
        
            billboard = discord.utils.find(lambda c: c.id == 808100225721303041,
                                         self.bot.guilds[0].channels
                                         )
            poll = await billboard.send(embed=embed)
            await poll.add_reaction(self.sel1)
            await poll.add_reaction(self.sel2)
            await poll.add_reaction(self.sel3)

            return await context.respond("I've Posted your poll to the billboard")
