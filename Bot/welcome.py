import discord
from discord.ext import commands

SPECIAL_CHANNELS = ["introductions", "roles"]
MESSAGE = "Welcome to {guildname} {name}"

class Welcome(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print("running join")
        #member = message.author
        if member.name == self.bot.user.name:
            return
        channel = member.guild.system_channel
        channels = [ch for ch in  member.guild.channels if ch.name in SPECIAL_CHANNELS]
        intro = [ch for ch in channels if ch.name == SPECIAL_CHANNELS[0]][0] 
        roles = [ch for ch in channels if ch.name == SPECIAL_CHANNELS[1]][0] 

        if channel is not None:
            await channel.send(MESSAGE.format(guildname=member.guild.name,name=member.mention))#f"Welcome ... {member.mention}\n{roles.mention}\n{intro.mention}\nsome more info")

def setup(bot):
    bot.add_cog(Welcome(bot))