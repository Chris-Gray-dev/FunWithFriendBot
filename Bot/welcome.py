import discord
from discord.ext import commands
from IDs import ID_DICT as IDs

SPECIAL_CHANNELS = ["introductions",
                    "roles",
                    "house-keeping"]

ADMINS = [IDs["Autumn"], 
         IDs["Chris"]]

MESSAGE = "Welcome to {guildname}, {name}!\nThis server is for games, events, interests, and friends!\nFor the server rules, please go to {rules}.\nFor introductions, please go to {intro}.\nFor roles, please go to {roles}.\nLet {autumn} or {chris} know which colour you would like to be, and do not hesitate to contact them for help.\nHave fun! :)"

#TODO move to a new helper file
def _get_channel(channels, name):
    try:
        return [ch for ch in channels if ch.name == name][0]
    except:
        return None
        
#TODO move to a new helper file
def _get_member(members, id):
    try:
        return [mem for mem in members if mem.id == id][0]
    except:
        return None

class Welcome(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("running join")

        channel = member.guild.system_channel
        guild = member.guild
        if (channel is None) or (member.bot):
            print("exiting join")
            return 

        channels = [ch for ch in guild.channels if ch.name in SPECIAL_CHANNELS]

        intro = _get_channel(channels, SPECIAL_CHANNELS[0]) 
        roles = _get_channel(channels, SPECIAL_CHANNELS[1])
        rules = _get_channel(channels, SPECIAL_CHANNELS[2])
        
        members = [mem for mem in guild.members if mem.id in ADMINS]

        autumn = _get_member(members, AUTUMN_ID)
        chris  = _get_member(members, CHRIS_ID)

        await channel.send(MESSAGE.format(guildname=member.guild.name,name=member.mention, rules=rules.mention, intro = intro.mention, roles=roles.mention, autumn=autumn.mention,chris=chris.mention))

def setup(bot):
    bot.add_cog(Welcome(bot))
    print("Welcome cog loaded")