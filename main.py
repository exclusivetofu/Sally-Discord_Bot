import discord
from discord.ui import Button, View
from discord.ext import commands

Sally = commands.Bot(command_prefix='*')

@Sally.event
async def on_ready():
    print(f'{Sally.user} Ready!')

@Sally.command()
async def ping(ctx):
    button1 = Button(label='SUCK', style=discord.ButtonStyle.green)
    button2 = Button(label='MY'  , style=discord.ButtonStyle.blurple)
    button3 = Button(style=discord.ButtonStyle.red, emoji='🍆')
    view = View(button1, button2, button3)

    await ctx.send('.', view= view)

from token import TOKEN
Sally.run(TOKEN)