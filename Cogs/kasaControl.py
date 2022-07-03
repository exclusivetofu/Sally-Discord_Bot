import discord
from discord.ext import commands
from discord.commands import permissions

import asyncio
from kasa import SmartBulb

class KasaControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids = [776972325010407454])
    @permissions.has_any_role("OwOner")
    async def kasa_test(self, context):
        shelf = SmartBulb("192.168.1.194")
        overhead1 = SmartBulb("192.168.1.35")
        overhead2 = SmartBulb("192.168.1.244")

        await shelf.update()
        await overhead1.update()
        await overhead2.update()

        print(shelf.alias)
        print(overhead1.alias)
        print(overhead2.alias)

        print(shelf.emeter_realtime)
        print(overhead1.emeter_realtime)
        print(overhead2.emeter_realtime)

        await shelf.turn_off()
        await overhead1.turn_off()
        await overhead2.turn_off()

        await context.respond("Turned off Tofu's Bedroom lights")