import discord
from discord.ext import commands
from discord.commands import permissions
import youtube_dl

class MusicCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

        self.ytdl_format_options = {
            "format": "bestaudio/best",
            "outtmpl": "%(extractor)s-%(id)s-%(title)s.%(ext)s",
            "restrictfilenames": True,
            "noplaylist": True,
            "nocheckcertificate": True,
            "ignoreerrors": False,
            "logtostderr": False,
            "quiet": True,
            "no_warnings": True,-
            "default_search": "auto",
            "source_address": "0.0.0.0",
        }

        self.ffmpeg_options = {"options": "-vn"}

        self.ytdl = youtube_dl.YoutubeDL(self.ytdl_format_options)

    @commands.slash_command(guild_ids = [776972325010407454])
    async def join(self, context, channel: discord.commands.Option(discord.VoiceChannel, required = True)):
        if context.voice_client is not None:
            return await context.voice_client.move_to(channel)

        await channel.connect()
        await context.respond(f'I sucsessfully connected to {channel.name}')

    @commands.slash_command(guild_ids = [776972325010407454])
    async def leave(self, context):
        await context.voice_client.disconnect()
        await context.respond("Til' next time")
