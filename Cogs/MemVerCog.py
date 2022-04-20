import discord
from discord.ext import commands
import json

class MemverCog(commands.Cog):
    def __init__( Self, Bot ):
        Self.Bot = Bot

    @commands.Cog.listener()
    async def on_member_join(Self, NewMember):
        Unverified = discord.utils.find(lambda m: m.name == 'Unverified',
                                        Self.Bot.guilds[0].roles)
        await NewMember.add_roles(Unverified)

    @commands.Cog.listener()
    async def on_raw_reaction_add(Self, Payload):
        Unverified = discord.utils.find(lambda m: m.name == 'Unverified',
                                        Self.Bot.guilds[0].roles)

        MemberRole = discord.utils.find(lambda m: m.name == 'Member',
                                        Self.Bot.guilds[0].roles)
        RuleMessageID = ''
        with open('Data/CogData/RuleMessageID.txt') as File:
            RuleMessageID = File.read()

        GenChat = discord.utils.find(lambda c: c.name == 'hg-development', 
                                     Self.Bot.guilds[0].channels)

        if Payload.message_id == int(RuleMessageID):
            if Payload.emoji.name == '👍':
                await Payload.member.add_roles(MemberRole)
                await Payload.member.remove_roles(Unverified)
                await GenChat.send(Payload.member.mention + ', welcome to the server!')                

                memberInfo = {
                    "MemberDetails":[
                    {
                    "memberID": Payload.member.id,
                    "displayName": Payload.member.name,
                    "tag": Payload.member.discriminator,
                    "whiteListedMC": False,
                    "lastActive": '',
                    "mainGamingPlat": '',
                    "gamerTag": ''
                    }
                 ]
                }
                memberJson = json.dumps(memberInfo, indent = 1)
                with open("MemberInfo/" + str(Payload.member.id) + ".json", "w") as file:
                    file.write(memberJson)
        
    @commands.command()
    async def rules( Self, Context ):
        if Context.author.id == '456489836614909963':
            return await Context.send('You are not allowed to do that.',
                                      delete_after = 3
                                     )

        Rules = discord.utils.find(lambda r: r.name == '📖rule-book',
                                   Self.Bot.guilds[0].channels
                                  )

        RuleMessage = ''

        with open('Data/CogData/ServerRules.txt') as File:
            RuleMessage = await Rules.send(File.read())
        await RuleMessage.add_reaction('👍')
        RuleMessageID = RuleMessage.id
        with open('Data/CogData/RuleMessageID.txt', 'w') as File:
            File.write(str(RuleMessageID))