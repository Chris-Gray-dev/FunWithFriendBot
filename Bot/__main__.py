# __main__.py
import discord
from discord.ext import commands
import os
import dotenv

__version__ = "0.0.0.8"
# Setup
print(discord.__version__)
intents = discord.Intents.default()
intents.members = True
dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

# Settings
bot = commands.Bot(command_prefix = ">", intents = intents)

PLUGINS = ["welcome",
            "train"] # TODO make a system for loading plugins
for plugin in PLUGINS:
    bot.load_extension(plugin)

# Events
@bot.event
async def on_ready():
    print(f"{bot.user.name} v{__version__}, connected to discord.")

@bot.command()
async def about(ctx):
    await ctx.send("")

bot.run(TOKEN)