import discord
from discord.ext import commands
from discord.ui import Button, View

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
    async def ping(ctx):
        button1 = Button(label = 'SUCK', style=discord.ButtonStyle.green)
        button2 = Button(label = 'MY'  , style=discord.ButtonStyle.blurple)
        button3 = Button(style = discord.ButtonStyle.red, emoji = '🍆')
        view = View(button1, button2, button3)

        await ctx.send('.', view = view)

    @commands.command()
    async def react(Self, Context):
        ...