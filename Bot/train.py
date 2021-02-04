import discord
from discord.ext import commands
from IDs import ID_DICT as IDs

MESSAGE = ":train2: {riley} the train goes into a tunnel :train2:"

#TODO move to a helper file e.g. helper.py
def _get_member(members, id): 
    try:
        return [mem for mem in members if mem.id == id][0]
    except:
        return None

class Train(commands.Cog):
    def __init__(self,bot):
        self.bot = bot

    @commands.command() 
    async def train(self, ctx):
        riley = _get_member(ctx.guild.members, IDs["Riley"])
        await ctx.send(MESSAGE.format(riley=riley.mention))

def setup(bot):
    bot.add_cog(Train(bot))
    print("Train cog loaded")