import os
from dotenv import load_dotenv
import discord
import asyncio
import psycopg2
import cred as cr

nickedReason = {}
nickedUser = {}

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


#@client.event
#async def on_guild_emojis_update(guild, before, after):
#	channel = client.get_channel(711110467120136254)
#	async for entry in guild.audit_logs(action=discord.AuditLogAction.emoji_delete, limit=1):
#		for emoji in before:
#			if emoji.id != target.id:
#				continue
#			else:
#				await channel.send('{0.user} a supprimé le sticker '.format(entry) + emoji.name)

client.run(TOKEN)
