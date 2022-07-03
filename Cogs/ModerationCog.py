from random import choices
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

    @commands.slash_command(guild_ids = [776972325010407454])
    @permissions.has_any_role("OwOner")
    async def changestat(self, context, type: discord.commands.Option(str, required = True, choices = ['Playing', 'Watching', 'Streaming', 'clear']),
                         activity: discord.commands.Option(str, required = True)):
        
        if type == 'Playing':
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.playing, name=activity))
        if type == 'Watching':
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name=activity))
        if type == 'Streaming':
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.streaming, name=activity))
        if type == 'clear':
            # Currently dosnet work as intended.
            # For now just clears status.
            await self.bot.change_presence(activity=discord.Activity(type=discord.ActivityType.custom, name=activity))

        return await context.respond('Status Updated')