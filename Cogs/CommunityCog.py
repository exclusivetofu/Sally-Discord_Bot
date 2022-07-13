import discord
from discord.ext import commands
import json

class CommunityCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.sel1  = '1️⃣'
        self.sel2  = '2️⃣'

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
                    cho1: discord.commands.Option(str, 'First Choice for your poll', required = True),
                    cho2: discord.commands.Option(str, 'Second Choice for your poll', required = True),
 
                   ):
            embed = discord.Embed(title = context.author.display_name + ' has created a poll', description = name, color=0xff00ff)
            embed.add_field(name = '[' + self.sel1 + '] ' + cho1, value = 'Option 1', inline=False)
            embed.add_field(name = '[' + self.sel2 + '] ' + cho2, value = 'Option 2', inline=False)
        
            billboard = discord.utils.find(lambda c: c.id == 808100225721303041,
                                         self.bot.guilds[0].channels
                                         )
            poll = await billboard.send(embed=embed)
            await poll.add_reaction(self.sel1)
            await poll.add_reaction(self.sel2)

            await context.respond("I've Posted your poll to the billboard")

            with open('polls/tilte.txt', 'a') as file:
                file.write_through
                file.write(name)
                file.close()
            with open('polls/choice1.txt', 'a') as file:
                file.write(cho1)
                file.close()
            with open('polls/choice2.txt', 'a') as file:
                file.write(cho2)
                file.close()
            with open('polls/id.txt', 'a') as file:
                file.write(str(poll.id))
                file.close
            with open('polls/votesOne.txt', 'a') as file:
                file.write('0')
                file.close()
            with open('polls/votesTwo.txt', 'a') as file:
                file.write('0')
                file.close()


    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        with open('polls/id.txt', 'r') as poll:
            pollID = int(poll.read())

            if payload.message_id == pollID:
                
                if payload.member.id == 776921914139607051:
                    return

                if payload.emoji.name == self.sel1:
                    global votes

                    with open('polls/votesOne.txt', 'r') as file:
                        votes = int(file.read())
                        file.close()
                    
                    votes + 1

                    print(votes)

                    with open('polls/votesOne.txt', 'a') as file:
                        file.write(str(votes))
                        file.close()

                