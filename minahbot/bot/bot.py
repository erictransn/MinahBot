import os

# modules to handle URL's
from discord.utils import get
import urllib.parse, urllib.request, re

import discord
from dotenv import load_dotenv

from discord.ext import commands

# grab minah token from environment variable
# guild are the same as server and not necessary for most cases
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

# set up intents for bot to subsrcibe to events specifically infor from discord guild/server
intents = discord.Intents.default()
intents.members = True

# set bot prefix
bot = commands.Bot(command_prefix='!', intents=intents)

# Says when bot is connected and ready
@bot.event
async def on_ready():
    print(f'{bot.user.name} bot has connected to Discord!')

@bot.command()
async def test(ctx):
    await ctx.send('test works')

# Youtube search video
@bot.command()
async def yt(ctx, *, search):
    query_string = urllib.parse.urlencode({'search_query': search})
    html_content = urllib.request.urlopen('http://www.youtube.com/results?' + query_string)
    search_results = re.findall(r'/watch\?v=(.{11})', html_content.read().decode())
    await ctx.send('https://www.youtube.com/watch?v=' + search_results[0])

bot.run(TOKEN)