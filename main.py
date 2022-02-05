import openai
import discord
from discord.ext import commands
from discord.ext.commands import command

discordToken = open("discordKey.txt","r").read()
openAItoken = open("openAiKey.txt","r").read()
bot = commands.Bot(command_prefix = '!')

@bot.event
async def on_ready():
    print("ready for action")

@bot.command()
async def hello(ctx):
    await ctx.send("Hello There!")

@bot.event
async def on_message(message):
    channel = message.channel
    if message.channel.id == message.author.dm_channel.id:
        print("Hello")
        await channel.send("Hello")


bot.run(discordToken)