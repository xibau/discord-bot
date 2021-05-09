
import os
from dotenv import load_dotenv
import discord
import asyncio
nickedUser = {}
nickedReason = {}
load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
	if message.content.startswith('!rename'):
		if message.mentions:
			nickedUser = message.mentions[0].id
			nickReason = message.content[len(str(nickedUser)) + 12:]
			await message.mentions[0].edit(nick=nickReason)
			await message.delete()
		else :
			await message.author.edit(nick=message.content[8:])
			await message.delete()

client.run(TOKEN)