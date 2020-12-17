# __main__.py
import discord
from discord.ext import commands
import os
import dotenv

# Setup
dotenv.load_dotenv()
TOKEN = os.getenv('TOKEN')

# Settings
bot = commands.Bot(command_prefix=">") # TODO not final
PLUGINS = [] # TODO make a system for loading plugins

# Events
@bot.event
async def on_ready():
    print(f"{bot.user.name} connected to discord.")


bot.run(TOKEN)