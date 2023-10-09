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
        print(response)
        
        # embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
    

       
        await message.channel.send(embed=response)
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
           
        except Exception as e:
            print(e)

    
    client.run(TOKEN)