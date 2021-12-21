from discord.ext import tasks, commands
import discord
from datetime import datetime

class MorningAnccCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update.start
        print('Anouncements cog started')

    def cog_unload(self):
        self.update.cancel()

    @tasks.loop(seconds=3.0)
    async def update(self):
        now = datetime.now().hour
        print(now)