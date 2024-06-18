import os
import discord
from dotenv import load_dotenv
from discord.ext import commands
import json
import random

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='/', intents=intents)

operator = json.load(open('operators.json'))
attackersNum = len(operator["operators"]["attackers"])
defendersNum = len(operator["operators"]["defenders"])


@bot.event
async def on_ready(): 
    print("Online")

@bot.command(name="attacker")
async def attacker(ctx):
    randomNum = random.randint(0,attackersNum - 1)
    randomAttacker = operator["operators"]["attackers"][randomNum]
    print(f"{ctx.author.global_name} got: {randomAttacker}")
    await ctx.send(f"{ctx.author.global_name} got: {randomAttacker}", delete_after=30)


@bot.command(name="defender")
async def defender(ctx):
    randomNum = random.randint(0,defendersNum - 1)
    randomDefender = operator["operators"]["defenders"][randomNum]
    print(f"{ctx.author.global_name} got: {randomDefender}")
    await ctx.send(f"{ctx.author.global_name} got: {randomDefender}", delete_after=30)

bot.run(TOKEN)