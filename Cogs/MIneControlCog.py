import discord
from mcrcon import MCRcon
from discord.ext import commands
from discord.commands import permissions

class MineControl(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(guild_ids = [776972325010407454], default_permission = False, discription = 'A Command to set the Minecraft server time')
    @permissions.has_any_role("MC Mod")
    async def timeset(
                    self,
                    context,
                    time: discord.commands.Option( str, 'Time to set to ', required = True, choices = ['day', 'noon', 'dusk', 'night', 'midnight', 'dawn']),
                    
                   ):
        
        with MCRcon("localhost", "oceanman133") as mineControl:
            if time == 'day':
                mineControl.command('/time set 1000')
            if time == 'noon':
                mineControl.command('/time set 6000')
            if time == 'dusk':
                mineControl.command('/time set 12000')
            if time == 'night':
                mineControl.command('/time set 13000')
            if time == 'midnight':
                mineControl.command('/time set 18000')
            if time == 'dawn':
                mineControl.command('/time set 23000')    

        await context.respond(f'Set time in minecraft server to {time}')

    @commands.slash_command(guild_ids = [776972325010407454], default_permission = False)
    @permissions.has_any_role("MC Mod")
    async def weatherset(
                    self,
                    context,
                    weather: discord.commands.Option( str, 'Weather to set to ', required = True, choices = ['rain', 'thunder', 'clear']),                    
                   ):
        
        with MCRcon("localhost", "oceanman133") as mineControl:
            if weather == 'rain':
                mineControl.command('/weather rain')
            if weather == 'thunder':
                mineControl.command('/weather thunder')
            if weather == 'clear':
                mineControl.command('/weather clear') 

        await context.respond(f'Set weather in minecraft server to {weather}')

    @commands.slash_command(guild_ids = [776972325010407454], default_permission = False)
    @permissions.has_any_role("MC Mod")
    async def whitelist(
                    self,
                    context,
                    option: discord.commands.Option( str, 'Choose to add or remove a player', required = True, choices = ['Add', 'Remove']), 
                    name: discord.commands.Option( str, 'Minecraft username', required = True),
                    member: discord.commands.Option( discord.Member, 'Server member to assiciate with', required = True),
                    operator: discord.commands.Option( bool, 'Choose to add or remove a player', required = True, defualt = False),             
                   ):
        
        with MCRcon("localhost", "oceanman133") as mineControl:
            if option == 'Add':
                mineControl.command(f'/whitelist add {name}')
                with open( 'MinecraftMemberList.tofu', 'a' ) as File:
                    File.write(f'Discord ID: {str(member.id)} Discord Name: {member.name}#{member.discriminator} Minecraft Username: {name}\n Is Operater: {operator}')
                
                messageMember = await member.create_dm()

                if operator == True:
                    embed = discord.Embed(title = 'An Invitaion to Play', description = context.author.display_name + " you have been invited to Moderate Tofu's Community Minecraft Server", color=0xff00ff)
                    embed.add_field(name = 'Server Address', value = '45.79.65.17', inline = True)
                    file = discord.File("server-icon.png", filename="image.png")
                    embed.set_thumbnail(url="attachment://image.png")
                    await messageMember.send(file = file, embed = embed)

                    return await context.respond('Invitation Sent')

                embed = discord.Embed(title = 'An Invitaion to Play', description = context.author.display_name + " you have been invited to Tofu's Community Minecraft Server", color=0xff00ff)
                embed.add_field(name = 'Server Address', value = '45.79.65.17', inline = True)
                file = discord.File("server-icon.png", filename="image.png")
                embed.set_thumbnail(url="attachment://image.png")
                await messageMember.send(file = file, embed = embed)

                return await context.respond('Invitation Sent')

            if option == 'Remove':
                await context.respond('An Error Occured')
                ...
            
        