import discord
import responses
from dotenv import load_dotenv
from discord import Intents
import os

#intents permission
intents = discord.Intents.default()
intents.typing = True
intents.presences = True

load_dotenv()

async def send_message(message,user_message,is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = os.getenv("TOKEN")
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')
    
    client.run(TOKEN)