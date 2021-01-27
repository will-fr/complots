import discord
import os
import requests
import json
import random
from replit import db


client = discord.Client()



# login message
@client.event
async def on_ready():
  print ('Authentifié en tant que {0.user}'.format(client))



@client.event
async def on_message(message):
  if message.author == client.user:
    return

  msg = message.content

  print(f'Auteur {message.author}.')
  print("message" + msg)

  message.react('😄');


  if msg.startswith('$start'):
    await message.channel.send ("demarrage du jeu complots!")





client.run(os.getenv('TOKEN'))

