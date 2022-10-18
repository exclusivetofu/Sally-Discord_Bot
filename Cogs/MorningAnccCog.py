from discord.ext import tasks, commands
import discord
import time

class MorningAnccCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update.start()
        self.canSend = False
        self.announcements = ''

    def cog_unload(self):
        self.update.cancel()

    @tasks.loop(seconds=45)
    async def update(self):
        with open('MorningAnnouncment.txt') as File:
            self.announcements = File.read()

        currentTime = str(time.strftime("%H:%M"))
        print(currentTime)

        alertTime = "8:30"
        
        self.canSend = False

        if currentTime == alertTime:
            self.canSend = True
            
        if self.canSend:
            from users import TOFU
            billboard = discord.utils.find(lambda billboard: billboard.id == 808100225721303041, self.bot.guilds[0].channels)
            await billboard.send(self.announcements)
            self.canSend = False

    @commands.command()
    async def peekAnnc(self, Context):
        billboard = discord.utils.find(lambda billboard: billboard.id == 1003707714549067847, self.bot.guilds[0].channels)
        await billboard.send(self.announcements)