import discord
from discord.ext import commands

class ReactRolesCog(commands.Cog):
    def __init__(Self, Bot):
        Self.Bot = Bot

        Self.Sel1  = '1️⃣'
        Self.Sel2  = '2️⃣'
        Self.Sel3  = '3️⃣'
        Self.Sel4  = '4️⃣'
        Self.Sel5  = '5️⃣'
        Self.Sel6  = '6️⃣'
        Self.Sel7  = '7️⃣'
        Self.Sel8  = '8️⃣'
        Self.Sel9  = '9️⃣'
        Self.Sel10 = '🔟'
        Self.Sel11 = '🇦'
        Self.Sel12 = '🇧'
        Self.Sel13 = '🟪'
        Self.Sel14 = '🟩'
        Self.Sel15 = '🟥'
        Self.Sel16 = '🟦'

    def SearchRoles(Self, RoleToSearchFor ):
        Result = discord.utils.find(lambda r: r.name == RoleToSearchFor, 
                                        Self.Bot.guilds[0].roles
                                        )
        return Result

    @commands.Cog.listener()
    async def on_raw_reaction_add(Self, Payload):

        print('raw reaction called')

        with open( 'Data/CogData/PronounRolesMsgID.txt' ) as File:
            PronounRolesMessage = int(File.read())
        with open( 'Data/CogData/AgeRolesMsgID.txt' )     as File:
            AgeRolesMessage     = int(File.read())
        with open( 'Data/CogData/HobbieRolesMsgID.txt' )  as File:
            HobbieRolesMessage  = int(File.read())
        with open( 'Data/CogData/PingsRolesMsgID.txt' )   as File:
            PingsRolesMessage   = int(File.read())
        with open( 'Data/CogData/GamerRolesMsgID.txt' )   as File:
            GamerRolesMessage   = int(File.read())

        Member     = Payload.member
        MessageID  = Payload.message_id
        EmojiName  = Payload.emoji.name

        if Member.display_name == 'Sally':
            print('passed bot check')
            return

        if MessageID == PronounRolesMessage:
            print('role type pronoun')
            if EmojiName == Self.Sel1:
                await Member.add_roles(Self.SearchRoles('He/Him'))
                print('gave he/him role')
            if EmojiName == Self.Sel2:
                await Member.add_roles(Self.SearchRoles('She/Her'))
            if EmojiName == Self.Sel3:
                await Member.add_roles(Self.SearchRoles('They/Them'))
        if MessageID == AgeRolesMessage:
            if EmojiName == Self.Sel1:
                await Member.add_roles(Self.SearchRoles('18+'))
            if EmojiName == Self.Sel2:
                await Member.add_roles(Self.SearchRoles('17'))
            if EmojiName == Self.Sel3:
                await Member.add_roles(Self.SearchRoles('-16'))
        if MessageID == HobbieRolesMessage:
            if EmojiName == Self.Sel1:
                await Member.add_roles(Self.SearchRoles('Gamer'))
            if EmojiName == Self.Sel2:
                await Member.add_roles(Self.SearchRoles('Artist'))
            if EmojiName == Self.Sel3:
                await Member.add_roles(Self.SearchRoles('Streamer/YouTuber'))
        if MessageID == PingsRolesMessage:
            if EmojiName == Self.Sel1:
                await Member.add_roles(Self.SearchRoles('Movie Night'))        
            if EmojiName == Self.Sel2:
                await Member.add_roles(Self.SearchRoles('Game Night'))
            if EmojiName == Self.Sel3:
                await Member.add_roles(Self.SearchRoles('Announcements'))
            if EmojiName == Self.Sel4:
                await Member.add_roles(Self.SearchRoles('Listen Along'))
            if EmojiName == Self.Sel5:
                await Member.add_roles(Self.SearchRoles('Frag-fest'))
        if MessageID == GamerRolesMessage:
            if EmojiName == Self.Sel1:
                await Member.add_roles(Self.SearchRoles('Apex Legends'))
            if EmojiName == Self.Sel2:
                await Member.add_roles(Self.SearchRoles('Call of Duty'))
            if EmojiName == Self.Sel3:
                await Member.add_roles(Self.SearchRoles('CS:GO'))
            if EmojiName == Self.Sel4:
                await Member.add_roles(Self.SearchRoles('Super Smash Bros.'))
            if EmojiName == Self.Sel5:
                await Member.add_roles(Self.SearchRoles('Battlefront'))
            if EmojiName == Self.Sel6:
                await Member.add_roles(Self.SearchRoles('Battlefield'))
            if EmojiName == Self.Sel7:
                await Member.add_roles(Self.SearchRoles('Rocket League'))
            if EmojiName == Self.Sel8:
                await Member.add_roles(Self.SearchRoles('Rainbow Six Siege'))
            if EmojiName == Self.Sel9:
                await Member.add_roles(Self.SearchRoles('Minecraft'))
            if EmojiName == Self.Sel10:
                await Member.add_roles(Self.SearchRoles('League of Legends'))
            if EmojiName == Self.Sel11:
                await Member.add_roles(Self.SearchRoles('Fifa'))
            if EmojiName == Self.Sel12:
                await Member.add_roles(Self.SearchRoles('Madden'))
            if EmojiName == Self.Sel13:
                await Member.add_roles(Self.SearchRoles('PC'))
            if EmojiName == Self.Sel14:
                await Member.add_roles(Self.SearchRoles('XBox'))
            if EmojiName == Self.Sel15:
                await Member.add_roles(Self.SearchRoles('Nintendo Switch'))
            if EmojiName == Self.Sel16:
                await Member.add_roles(Self.SearchRoles('Playstation'))
        
    @commands.Cog.listener()
    async def on_raw_reaction_remove(Self, Payload):
        
        print('raw reaction called')

        with open( 'Data/CogData/PronounRolesMsgID.txt' ) as File:
            PronounRolesMessage = int(File.read())
        with open( 'Data/CogData/AgeRolesMsgID.txt' )     as File:
            AgeRolesMessage     = int(File.read())
        with open( 'Data/CogData/HobbieRolesMsgID.txt' )  as File:
            HobbieRolesMessage  = int(File.read())
        with open( 'Data/CogData/PingsRolesMsgID.txt' )   as File:
            PingsRolesMessage   = int(File.read())
        with open( 'Data/CogData/GamerRolesMsgID.txt' )   as File:
            GamerRolesMessage   = int(File.read())

        Member     = discord.utils.find(lambda m: m.id == Payload.user_id, 
                                            Self.Bot.guilds[0].members
                                            )
        MessageID  = Payload.message_id
        EmojiName  = Payload.emoji.name

        if MessageID == PronounRolesMessage:
            print('role type pro')
            if EmojiName == Self.Sel1:
                await Member.remove_roles(Self.SearchRoles('He/Him'))
                print('removed he him role')
            if EmojiName == Self.Sel2:
                await Member.remove_roles(Self.SearchRoles('She/Her'))
            if EmojiName == Self.Sel3:
                await Member.remove_roles(Self.SearchRoles('They/Them'))
        if MessageID == AgeRolesMessage:
            if EmojiName == Self.Sel1:
                await Member.remove_roles(Self.SearchRoles('18+'))
            if EmojiName == Self.Sel2:
                await Member.remove_roles(Self.SearchRoles('17'))
            if EmojiName == Self.Sel3:
                await Member.remove_roles(Self.SearchRoles('-16'))
        if MessageID == HobbieRolesMessage:
            if EmojiName == Self.Sel1:
                await Member.remove_roles(Self.SearchRoles('Gamer'))
            if EmojiName == Self.Sel2:
                await Member.remove_roles(Self.SearchRoles('Artist'))
            if EmojiName == Self.Sel3:
                await Member.remove_roles(Self.SearchRoles('Streamer/YouTuber'))
        if MessageID == PingsRolesMessage:
            if EmojiName == Self.Sel1:
                await Member.remove_roles(Self.SearchRoles('Movie Night'))        
            if EmojiName == Self.Sel2:
                await Member.remove_roles(Self.SearchRoles('Game Night'))
            if EmojiName == Self.Sel3:
                await Member.remove_roles(Self.SearchRoles('Announcements'))
            if EmojiName == Self.Sel4:
                await Member.remove_roles(Self.SearchRoles('Listen Along'))
            if EmojiName == Self.Sel5:
                await Member.remove_roles(Self.SearchRoles('Frag-fest'))
        if MessageID == GamerRolesMessage:
            if EmojiName == Self.Sel1:
                await Member.remove_roles(Self.SearchRoles('Apex Legends'))
            if EmojiName == Self.Sel2:
                await Member.remove_roles(Self.SearchRoles('Call of Duty'))
            if EmojiName == Self.Sel3:
                await Member.remove_roles(Self.SearchRoles('CS:GO'))
            if EmojiName == Self.Sel4:
                await Member.remove_roles(Self.SearchRoles('Super Smash Bros.'))
            if EmojiName == Self.Sel5:
                await Member.remove_roles(Self.SearchRoles('Battlefront'))
            if EmojiName == Self.Sel6:
                await Member.remove_roles(Self.SearchRoles('Battlefield'))
            if EmojiName == Self.Sel7:
                await Member.remove_roles(Self.SearchRoles('Rocket League'))
            if EmojiName == Self.Sel8:
                await Member.remove_roles(Self.SearchRoles('Rainbow Six Siege'))
            if EmojiName == Self.Sel9:
                await Member.remove_roles(Self.SearchRoles('Minecraft'))
            if EmojiName == Self.Sel10:
                await Member.remove_roles(Self.SearchRoles('League of Legends'))
            if EmojiName == Self.Sel11:
                await Member.remove_roles(Self.SearchRoles('Fifa'))
            if EmojiName == Self.Sel12:
                await Member.remove_roles(Self.SearchRoles('Madden'))
            if EmojiName == Self.Sel13:
                await Member.remove_roles(Self.SearchRoles('PC'))
            if EmojiName == Self.Sel14:
                await Member.remove_roles(Self.SearchRoles('XBox'))
            if EmojiName == Self.Sel15:
                await Member.remove_roles(Self.SearchRoles('Nintendo Switch'))
            if EmojiName == Self.Sel16:
                await Member.remove_roles(Self.SearchRoles('Playstation'))            

    @commands.command()
    async def MakeRoleMenu( Self, Context ):
        RoleChannel = discord.utils.find(lambda c: c.id == 806787239316291634,
                                         Self.Bot.guilds[0].channels
                                         )

        with open('Data/CogData/PronounsRoleMenu.txt', encoding='UTF-8') as MenuText:
            Menu = await RoleChannel.send(MenuText.read())
        with open( 'Data/CogData/PronounRolesMsgID.txt', 'w' ) as File:
            File.write(str(Menu.id))

            await Menu.add_reaction(Self.Sel1)
            await Menu.add_reaction(Self.Sel2)
            await Menu.add_reaction(Self.Sel3)
        
        with open('Data/CogData/AgeRoleMenu.txt', encoding='UTF-8') as MenuText:
            Menu = await RoleChannel.send(MenuText.read())
        with open( 'Data/CogData/AgeRolesMsgID.txt', 'w' ) as File:
            File.write(str(Menu.id))

            await Menu.add_reaction(Self.Sel1)
            await Menu.add_reaction(Self.Sel2)
            await Menu.add_reaction(Self.Sel3)

        with open('Data/CogData/HobbiesRoleMenu.txt', encoding='UTF-8') as MenuText:
            Menu = await RoleChannel.send(MenuText.read())
        with open( 'Data/CogData/HobbieRolesMsgID.txt', 'w' ) as File:
            File.write(str(Menu.id))

            await Menu.add_reaction(Self.Sel1)
            await Menu.add_reaction(Self.Sel2)
            await Menu.add_reaction(Self.Sel3)

        with open('Data/CogData/PingsRoleMenu.txt', encoding='UTF-8') as MenuText:
            Menu = await RoleChannel.send(MenuText.read())
        with open( 'Data/CogData/PingsRolesMsgID.txt', 'w' ) as File:
            File.write(str(Menu.id))

            await Menu.add_reaction(Self.Sel1)
            await Menu.add_reaction(Self.Sel2)
            await Menu.add_reaction(Self.Sel3)
            await Menu.add_reaction(Self.Sel4)
            await Menu.add_reaction(Self.Sel5)

        with open('Data/CogData/GamerRoleMenu.txt', encoding='UTF-8') as MenuText:
            Menu = await RoleChannel.send(MenuText.read())
        with open( 'Data/CogData/GamerRolesMsgID.txt', 'w' ) as File:
            File.write(str(Menu.id))

            await Menu.add_reaction(Self.Sel1)
            await Menu.add_reaction(Self.Sel2)
            await Menu.add_reaction(Self.Sel3)
            await Menu.add_reaction(Self.Sel4)
            await Menu.add_reaction(Self.Sel5)
            await Menu.add_reaction(Self.Sel6)
            await Menu.add_reaction(Self.Sel7)
            await Menu.add_reaction(Self.Sel8)
            await Menu.add_reaction(Self.Sel9)
            await Menu.add_reaction(Self.Sel10)
            await Menu.add_reaction(Self.Sel11)
            await Menu.add_reaction(Self.Sel12)
            await Menu.add_reaction(Self.Sel13)
            await Menu.add_reaction(Self.Sel14)
            await Menu.add_reaction(Self.Sel15)
            await Menu.add_reaction(Self.Sel16)