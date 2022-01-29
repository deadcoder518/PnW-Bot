import discord
import os
from dotenv.main import load_dotenv
from discord.ext import commands
import requests
import json

load_dotenv()

bot = commands.Bot(command_prefix="!")
TOKEN = os.getenv("DISCORD_TOKEN")

@bot.command(name="whoxen")
async def identify(ctx):
    xen = "Xen is the greatest of all time!"
    await ctx.send(xen)
    #could've done embeds but they're very easy!

@bot.command(name="steelsell")
async def steelsell(ctx):
    tradeData = requests.get(f"https://politicsandwar.com/api/tradeprice/?resource=steel&key="+str(os.getenv("API_KEY")))
    tradeData = tradeData.json()
    nationid = tradeData["lowestbuy"]["nationid"]
    nationlink = "https://politicsandwar.com/nation/id="+nationid
    await ctx.send(nationlink)

#running bot
bot.run(TOKEN)