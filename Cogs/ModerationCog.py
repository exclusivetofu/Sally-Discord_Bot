import discord
from discord.ext import commands
from discord.commands import permissions

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids = [776972325010407454], default_permission = False)
    @permissions.has_any_role("Admin")
    async def purge(
                    self,
                    context,
                    amount: discord.commands.Option( int, 'How many messages to purge', required = False, default = 10),
                   ):
        deleted = await context.channel.purge(limit=amount)
        await context.respond(f'Deleted {len(deleted)} message(s)')