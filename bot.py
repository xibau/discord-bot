
import os
import discord
import asyncio
nickedUser = {}
nickedReason = {}


TOKEN = 'ODQwMzAyMjA0Mjk5OTAyOTk3.YJWOaQ.L-S2WAdU6G4Yux_MRiHa1JSqTeM'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.content.startswith('!autorename'):
		await message.author.edit(nick=message.content[12:])

@client.event
async def on_message(message):
	if message.content.startswith('!rename'):
		nickedUser = message.mentions[0].id
		nickReason = message.content[len(str(nickedUser)) + 13:]
		await message.mentions[0].edit(nick=nickReason)

client.run(TOKEN)