from datetime import date
from pydoc import describe
import discord
import os
from dotenv.main import load_dotenv
from discord.ext import commands
import requests
import random

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
        await ctx.send("This nation currently has the best " + type + " for " + resource + ". Hope it's you! If it's not, go undercut now!!! Testing final.")
    except KeyError:
        await ctx.send("Can you use me properly please. Make sure you enter !tp followed by buy/sell and the resource. Like this:")
        await ctx.send("!tp buy steel")
        #await ctx.send("Enter !help if you're still struggling.")

#ground battle simulator (runs 100000 sims)
@bot.command()
async def ground(ctx, aSoldiers, aTanks, dSoldiers, dTanks):
    """Fetches the current highest buy/lowest sell price of a resource on the GTO."""
    try:
        aSoldiers = int(aSoldiers)
        aTanks = int(aTanks)
        dSoldiers = int(dSoldiers)
        dTanks = int(dTanks)

        aValue = (aSoldiers * 1.75) + (aTanks * 40)
        dValue = (dSoldiers * 1.75) + (dTanks * 40)

        immense = 0
        moderate = 0
        pyrrhic = 0
        failure = 0

        for i in range(100000):
            w = 0
            for i in range(3):
                aRollValue = random.uniform((0.4*aValue),aValue)
                dRollValue = random.uniform((0.4*dValue),dValue)
                if aRollValue > dRollValue:
                    w += 1
            if w == 3:
                immense += 1
            elif w == 2:
                moderate += 1
            elif w == 1:
                pyrrhic += 1
            else:
                failure += 1

        await ctx.send("100,000 Simulations:")
        await ctx.send("Immense Triumphs: " + str(immense) + " (" + str((immense/100000)*100) + ")")
        await ctx.send("Moderate Successes: " + str(moderate) + " (" + str((moderate/100000)*100) + ")")
        await ctx.send("Pyrrhic Victories: " + str(pyrrhic) + " (" + str((pyrrhic/100000)*100) + ")")
        await ctx.send("Utter Failures: " + str(failure) + " (" + str((failure/100000)*100) + ")")
        await ctx.send("Assuming soldiers are using munitionz.")        
    except KeyError:
        await ctx.send("You didn't enter the command properly. Ping Sabo for help because I'm useless and can't help you myself.")

#running bot
bot.run(TOKEN)