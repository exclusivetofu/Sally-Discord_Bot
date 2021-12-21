from discord.ext import tasks, commands
import discord
from datetime import datetime

class ServerTime(commands.Cog):
    def __init__(self, bot, timeChat):
        self.bot = bot
        self.update.start()
        self.timeChat = timeChat

    def cog_unload(self):
        self.update.cancel()

    @tasks.loop(seconds=15.0)
    async def update(self):

        if len(self.bot.guilds) == 0:
            print('Time Channel Not Ready')
            return
        
        now = datetime.now.()
        time = now.strftime("local-time-%H-%M")
        print(time)
        await self.timeChat.edit(name=time)
        #print(self.bot.guilds)