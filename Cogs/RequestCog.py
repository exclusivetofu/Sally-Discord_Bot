from discord.ext import commands
from datetime import date

class RequestCog(commands.Cog):
    def __init__( Self, Bot):
        Self.Bot = Bot

    @commands.command()
    async def request( Self, Context, *Arguments):
        Today = date.today()
        Request = ' '.join(Arguments)

        with open('Logs/Requests.txt', 'a') as File:
            File.write('<' + str(Today) + '> From ' + Context.author.display_name + ': ' + Request + '\n')
            print('<' + str(Today) + '> From ' + Context.author.display_name + ': ' + Request)
    
    @commands.command()
    async def listRequests(Self, Context):
        if not Context.author.id ==  456489836614909963: return

        with open('Logs/Requests.txt') as File:
            Reqs = File.read()
            if Reqs == '':
                return await Context.send('No requests to show')
            await Context.send(Reqs)

    @commands.command()
    async def clearRequests(Self, Context):
        if not Context.author.id ==  456489836614909963: return

        with open('Logs/Requests.txt', 'r+') as File:
            File.truncate(0)
