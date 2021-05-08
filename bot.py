
import os
import discord
import asyncio
nickedUser = {}
nickedReason = {}


TOKEN = 'ODQwMzAyMjA0Mjk5OTAyOTk3.YJWOaQ.W6qhix3K8_NNRu8wNv34anSmu7M'
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.content.startswith('!rename'):
		if message.mentions:
			nickedUser = message.mentions[0].id
			nickReason = message.content[len(str(nickedUser)) + 13:]
			await message.mentions[0].edit(nick=nickReason)
			await message.delete()
		else :
			await message.author.edit(nick=message.content[8:])
			await message.delete()

client.run(TOKEN)