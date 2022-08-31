import discord
from discord.ext import commands

from kasa import SmartBulb

class KasaControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.shelf = SmartBulb("192.168.1.196")
        self.overhead1 = SmartBulb("192.168.1.37")
        self.overhead2 = SmartBulb("192.168.1.246")

    @commands.slash_command(guild_ids = [776972325010407454])
    @discord.default_permissions( administrator=True )  
    async def lights(self, context):
        
        await self.shelf.update()
        await self.overhead1.update()
        await self.overhead2.update()

        if self.overhead1.light_state['on_off'] == 0 and self.overhead2.light_state['on_off'] == 0 and self.shelf.light_state['on_off'] == 0:
            await self.shelf.turn_on()
            await self.overhead1.turn_on()
            await self.overhead2.turn_on()
            await context.respond("Turned on Tofu's Bedroom lights")

        if self.overhead1.light_state['on_off'] == 1 and self.overhead2.light_state['on_off'] == 1 and self.shelf.light_state['on_off'] == 1:
            await self.shelf.turn_off()
            await self.overhead1.turn_off()
            await self.overhead2.turn_off()
            await context.respond("Turned off Tofu's Bedroom lights")