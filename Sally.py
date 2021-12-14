import discord
from discord.ui import Button, View
from discord.ext import commands

SallysIntents = discord.Intents.all()
Doing = discord.Game(name = "Halo Infinite")
Sally = commands.Bot(command_prefix = '*',
                     intents = SallysIntents,
                     status = discord.Status.online
                    )

@Sally.event
async def on_ready():
    await Sally.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="old Pewdiepie videos"))
    from users import TOFU 
    Tofu = discord.utils.find(lambda Tofu: Tofu.id == TOFU, Sally.guilds[0].members)
    await Tofu.send('Awating orders master')

from Cogs.DebugCog import DebugCog
Sally.add_cog(DebugCog(Sally))

from Cogs.ReactionRolesCog import ReactRolesCog
Sally.add_cog(ReactRolesCog(Sally))

from Cogs.MemVerCog import MemverCog
Sally.add_cog(MemverCog(Sally))

from Cogs.RequestCog import RequestCog
Sally.add_cog(RequestCog(Sally))

with open('token.txt') as File:
    Sally.run(File.read())