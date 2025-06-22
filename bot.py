# main file for bot

import discord

TOKEN = 'YOUR_BOT_TOKEN'          # Replace with your bot token
CHANNEL_ID = 123456789012345678   # Replace with your channel ID (as an integer)

intents = discord.Intents.default()
intents.message_content = True  # Required to read message content

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print(f'Listening to messages in channel ID {CHANNEL_ID}...')

@client.event
async def on_message(message):
    # Ignore messages from other channels or from the bot itself
    if message.channel.id != CHANNEL_ID or message.author == client.user:
        return

    print(f'[{message.author}]: {message.content}')

client.run(TOKEN)
