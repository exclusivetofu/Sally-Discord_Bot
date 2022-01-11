import discord
from discord.ext import commands

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids = [776972325010407454])
    async def purge(
                    self,
                    context,
                    amount: discord.commands.Option( int, 'How many messages to purge', required = False, default = 10),
                   ):
        await context.send(f'I will delete {amount} message(s)')
        deleted = await context.channel.purge(limit=amount)
        await context.channel.send(f'Deleted {len(deleted)} message(s)')