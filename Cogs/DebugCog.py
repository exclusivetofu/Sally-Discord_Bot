from email.policy import default
import discord
from discord.ext import commands
from discord.ui import Button, View
from discord.commands import permissions

class DebugCog(commands.Cog):
    def __init__(Self, Bot):
        Self.Bot       = Bot
        Self.DebugFlag = False

    @commands.command()
    async def dflag(Self, Context):
        if Self.DebugFlag:
            Self.DebugFlag = False
            await Context.send('Debug has been set to false.')
        else:
            Self.DebugFlag = True
            await Context.send('Debug has been set to true.')

    @commands.command()
    async def ping(Self, context):
        # Ping command that also tests button functionality
        button1 = Button(label = 'SUCK', style=discord.ButtonStyle.green)
        button2 = Button(label = 'MY'  , style=discord.ButtonStyle.blurple)
        button3 = Button(style = discord.ButtonStyle.red, emoji = '🍆')
        view = View(button1, button2, button3)
        await context.send('.', view = view)

    @commands.slash_command(guild_ids = [776972325010407454], default_permission = False)
    @permissions.is_user(456489836614909963)
    async def echo(
                    self,
                    context,
                    content: discord.commands.Option( str, 'what to say ',    required = True),
                    channel: discord.commands.Option( str, 'Time to set to ', required = False, default = 803104357221793812),
                   ):
        channel = discord.utils.find(lambda c: c.id == int(channel),
                                         self.Bot.guilds[0].channels
                                         )
        await  channel.trigger_typing()
        await  channel.send(content)

        await context.respond(f'Echo message sent to {channel.name}')

    