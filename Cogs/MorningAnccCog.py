from discord.ext import tasks, commands
import discord
import datetime as dt

class MorningAnccCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update.start()
        self.canSend = False
        self.announcements = ''

    def cog_unload(self):
        self.update.cancel()

    @tasks.loop(seconds=5)
    async def update(self):
        with open('MorningAnnouncment.txt') as File:
            self.announcements = File.read()

        hour   = dt.datetime.now().hour
        minute = dt.datetime.now().minute
        second = dt.datetime.now().second

        hourToCheck   = 8
        minToCheck    = 46
        secondToCheck = 20
        
        self.canSend = False

        if hour == hourToCheck and minute == minToCheck and second == secondToCheck:
            self.canSend = True
            if self.canSend:
                from users import TOFU
                Tofu = discord.utils.find(lambda Tofu: Tofu.id == TOFU, self.bot.guilds[0].members)
                await Tofu.send(self.announcements)
                self.canSend = False