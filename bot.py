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

@bot.command(name="whoxen")
async def identify(ctx):
    xen = "Xen is the greatest of all time!"
    await ctx.send(xen)
    #could've done embeds but they're very easy!

key = os.getenv("API_KEY")

tradeData = requests.get(f"https://politicsandwar.com/api/tradeprice/?resource=steel&key="+key)
tradeData = tradeData.json()

#fetches buy steel price
@bot.command(name="steelsell")
async def steelsell(ctx):
    nationID = tradeData["lowestbuy"]["nationid"]
    tradeTime = tradeData["lowestbuy"]["date"]
    nationLink = "https://politicsandwar.com/nation/id="+nationID
    nationData = requests.get(f"https://politicsandwar.com/api/nation/id="+nationID+"/&key="+key)
    nationData = nationData.json()
    embed = discord.Embed(title=nationData["name"],url=nationLink)
    embed.set_thumbnail(url=nationData["flagurl"])
    embed.add_field(name="Time of Trade",value=tradeTime)
    await ctx.send(embed=embed)

#running bot
bot.run(TOKEN)