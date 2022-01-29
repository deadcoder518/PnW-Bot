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
    nationid = tradeData["lowestbuy"]["nationid"]
    time = tradeData["lowestbuy"]["date"]
    nationlink = "https://politicsandwar.com/nation/id="+nationid
    embed = discord.Embed(url=nationlink)
    embed.add_field(name="Time of Trade",value=date)
    await ctx.send(embed)

#running bot
bot.run(TOKEN)