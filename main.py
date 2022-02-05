import openai
import discord
import os
from discord.ext import commands
from discord.ext.commands import command
import keys

openai.api_key = os.getenv(keys.OPENAPI_KEY)
bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print("ready for action")

#Exclamation mark hello command 
@bot.command()
async def hello(ctx):
    await ctx.send("Hello There!")


#Just a test to see if it works in DM's only
@bot.event
async def on_message(message):
    channel = message.channel
    if message.channel.id == message.author.dm_channel.id:
        print("Hello")
        await channel.send("Hello")


bot.run(keys.DISCORD_KEY)