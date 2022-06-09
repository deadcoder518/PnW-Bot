from datetime import date
from pydoc import describe
import discord
import os
from dotenv.main import load_dotenv
from discord.ext import commands
import requests

load_dotenv()

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

key = os.getenv("API_KEY")

#test command (checks if bot is working)
@bot.command(name="test")
async def test(ctx):
    await ctx.send("Working!")

#gets tradeprices (highest buy/lowest sell) for any resource
@bot.command()
async def tp(ctx, type, resource):
    """Fetches the current highest buy/lowest sell price of a resource on the GTO."""
    try:
        section = ""
        if type == "sell":
            section = "lowestbuy"
        elif type == "buy":
            section = "highestbuy"
        tradeData = requests.get(f"https://politicsandwar.com/api/tradeprice/?resource="+resource+"&key="+key)
        tradeData = tradeData.json()
        nationID = tradeData[section]["nationid"]
        nationLink = "https://politicsandwar.com/nation/id="+nationID
        await ctx.send(nationLink)
        await ctx.send("This nation currently has the best " + type + " for " + resource + ". Hope it's you! If it's not, go undercut now!!! Testing..")
    except KeyError:
        await ctx.send("Can you use me properly please. Make sure you enter !tp followed by buy/sell and the resource. Like this:")
        await ctx.send("!tp buy steel")
        #await ctx.send("Enter !help if you're still struggling.")

#running bot
bot.run(TOKEN)