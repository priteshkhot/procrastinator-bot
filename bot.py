# This example requires the 'message_content' intent.

import discord
from dotenv import load_dotenv
import os

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.channel.id == int(os.getenv('UPDATE_CHANNEL_ID')):
        if message.content.startswith('$hello'):
            await message.add_reaction('✅')
            await message.channel.send('Hello!')

client.run(os.getenv("BOT_TOKEN"))
