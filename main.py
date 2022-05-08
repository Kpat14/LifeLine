import discord
from discord.ext import commands
import asyncio
import discord.client
from discord.ext.commands import bot
import requests
import json

client = discord.Client()
keywords = ["suicide","I'm going to die","depression","loneliness","kill myself"
,"lonely"]

def getQuote():
  response =  requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]["q"] + " -" + json_data[0]["a"]
  return(quote)


@client.event
async def on_ready():
  print("Bot Ready")


@client.event
async def on_message(message):
  for i in range (len(keywords)):
    if keywords[i] in message.content:
      await message.author.send ('STAY STRONG AND HEALTHY! THERES ALWAYS A SOLUTION! THIS IS NOT THE END!')
      for j in range(3):
        quote = getQuote()
        await message.author.send("-------------------------------------------------------------------------")

        await message.author.send (quote)

      await message.author.send("--------------------------------------------------------------------------")
      await message.author.send("\n We noticed you've been feeling a little down. Just remember everything will get better. Here are some resources that may help you.\n ")
        
      await message.author.send('https://www.crisisservicescanada.ca/en/')
      await message.author.send('https://youtu.be/g-jwWYX7Jlo')

client.run("OTcyNzY4MTQyNjY3NDQ0MjI0.GG2IcN.NYqzQXriaYbi6CCUJl-frUqnwxh_qZGml4TqeE")
