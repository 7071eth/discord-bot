import discord
import responses
from dotenv import load_dotenv
from discord import Intents
import os

#intents permission
intents = discord.Intents.all()

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

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return
        
    

        print(message)
        username = str(message.author)
        user_message = str(message.content)
        print(user_message)
        channel = str(message.channel)

        print(f"{username} said: '{user_message} ({channel})")

        try:
            if user_message[0] == '?':
                user_message = user_message[1:]
                await send_message(message, user_message, is_private=False)
            else:
                await send_message(message,user_message,is_private=False)
        except Exception as e:
            print(e)

    
    client.run(TOKEN)