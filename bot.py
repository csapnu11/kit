# main file for bot

import discord
from config import TOKEN, CHANNEL_ID  
from grocery_handler import COMMAND_MAP

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True
intents.messages = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    print(f'Listening to messages in channel ID {CHANNEL_ID}...')

@client.event
async def on_message(message):
    if message.channel.id != CHANNEL_ID:
        return

    # Avoid responding to itself
    if message.author == client.user:
        return

    # Print message to terminal
    print(f'[{message.author}]: {message.content}')

    # If the bot is mentioned in the message, process reply
    if client.user in message.mentions:
        await create_reply(message)


async def create_reply(message):
    # find command tag
    content_upper = message.content.upper()
    found = False

    for command, handler in COMMAND_MAP.items():
        if command in content_upper:
            await handler(message)
            found = True
            break  # Only run one command per message
    

    if not found:
        await message.channel.send("❓ Unknown command. Type `HELP GL` for available commands. Awowowowo~")




# start process
client.run(TOKEN)
