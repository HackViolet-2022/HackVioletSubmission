import openai
import discord
import os
from discord.ext import commands
from discord.ext.commands import command
import keys

#Initialize bots
bot = commands.Bot(command_prefix = '!')


#This function will reply based on message sent from user (exapnd with MongoDB later for optimization)
def talk(message):
    openai.api_key = keys.OPENAPI_KEY
    response = openai.Completion.create(
        engine="text-curie-001",
        prompt = message,
        temperature = 0.8,
        max_tokens = 150,
        top_p = 1,
        frequency_penalty = 0,
        presence_penalty = 0.3
    )
    content = response.choices[0].text.split('.')
    print(content)
    return response.choices[0].text




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
        x = message.author.id #store message author
        print(message.content)
        await channel.send(talk(message.content))
        

        #check if its in db, if not store it
        #store id into mongo db
        #call talk(message), store the query + answer, talk returns (optimize)

        #if new user:
            #do some probing 

    


bot.run(keys.DISCORD_KEY)