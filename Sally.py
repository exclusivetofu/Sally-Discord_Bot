import discord
from discord.ext import commands

SallysIntents = discord.Intents.all()
Sally = commands.Bot(command_prefix = '*', intents = SallysIntents, status = discord.Status.online)

@Sally.event
async def on_ready():
    await Sally.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name="Super Smash Bros. Melee"))
    from users import TOFU 
    Tofu = discord.utils.find(lambda Tofu: Tofu.id == TOFU, Sally.guilds[0].members)
    await Tofu.send('Awating orders master')
    print("ready")

#from Cogs.DebugCog import DebugCog
#Sally.add_cog(DebugCog(Sally))

from Cogs.ReactionRolesCog import ReactRolesCog
Sally.add_cog(ReactRolesCog(Sally))

from Cogs.MemVerCog import MemverCog
Sally.add_cog(MemverCog(Sally))

from Cogs.RequestCog import RequestCog
Sally.add_cog(RequestCog(Sally))

from Cogs.MorningAnccCog import MorningAnccCog
Sally.add_cog(MorningAnccCog(Sally))

from Cogs.ModerationCog import ModerationCog
Sally.add_cog(ModerationCog(Sally))

from Cogs.MIneControlCog import MineControl
Sally.add_cog(MineControl(Sally))

from Cogs.kasaControl import KasaControl
Sally.add_cog(KasaControl(Sally))

# from Cogs.MusicCog import MusicCog
# ally.add_cog(MusicCog(Sally))

from Cogs.CommunityCog import CommunityCog
Sally.add_cog(CommunityCog(Sally))

with open('token.txt') as File:
    Sally.run(File.read())
