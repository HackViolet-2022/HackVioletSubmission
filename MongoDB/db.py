import discord
import pymongo
from pymongo import MongoClient



client = pymongo.MongoClient('mongodb+srv://Harp:N5QFEFlYEu5dZD5U@cluster0.v7mnf.mongodb.net/DiscordBotDB?retryWrites=true&w=majority')


db = client["DiscordBotDB"]
collection = db["Users"]
  if "checking" in str(ctx.content.lower()):
        post = {"_id": ctx.author.id, "messages_sent": 1}
    collection.insert_one(post)
    await ctx.channel.send('added')
