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

def getAttacker():
    randomNum = random.randint(0,attackersNum - 1)
    randomAttacker = operator["operators"]["attackers"][randomNum]
    return randomAttacker

def getDefender():
    randomNum = random.randint(0,defendersNum - 1)
    randomDefender = operator["operators"]["defenders"][randomNum]
    return randomDefender


class myView(discord.ui.View):
    @discord.ui.button(label="Attacker", style=discord.ButtonStyle.blurple)
    async def attacker(self,  interaction: discord.interactions, button: discord.ui.Button):
        attacker = getAttacker()
        print(f"{interaction.user.global_name} got: {attacker}")
        await interaction.response.send_message(f"{interaction.user.global_name} got: {attacker}", delete_after=30)

    @discord.ui.button(label="Defender", style=discord.ButtonStyle.danger)
    async def defender(self,  interaction: discord.interactions, button: discord.ui.Button):
        defender = getDefender()
        print(f"{interaction.user.global_name} got: {defender}")
        await interaction.response.send_message(f"{interaction.user.global_name} got: {defender}" , delete_after=30)


@bot.event
async def on_ready(): 
    print("Online")


@bot.command()
async def rndOps(ctx):
    view = myView(timeout=None)
    await ctx.send(view=view)


bot.run(TOKEN)




# @bot.command(name="attacker")
# async def attacker(ctx):
#     randomNum = random.randint(0,attackersNum - 1)
#     randomAttacker = operator["operators"]["attackers"][randomNum]
#     print(f"{ctx.author.global_name} got: {randomAttacker}")
#     await ctx.send(f"{ctx.author.global_name} got: {randomAttacker}", delete_after=30)


# @bot.command(name="defender")
# async def defender(ctx):
#     randomNum = random.randint(0,defendersNum - 1)
#     randomDefender = operator["operators"]["defenders"][randomNum]
#     print(f"{ctx.author.global_name} got: {randomDefender}")
#     await ctx.send(f"{ctx.author.global_name} got: {randomDefender}", delete_after=30)
