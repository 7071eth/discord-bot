import requests
import discord
def handle_response(message) -> str:

    p_message = message.lower()

    #Hugging face api
    url = f'https://huggingface.co/api/models?search={p_message}&limit=5'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        titles =[]
        links=[]
        for x in data:
            title = x['modelId']
            link =str(f'https://huggingface.co/{title}')
            titles.append(title)
            links.append(link)
        
        embed = discord.Embed(color=0xFF5733)
        for title, link in zip(titles, links):
            embed.add_field(name=title, value=link, inline=False)
        return embed

    else:
        return "No results found"

    # if p_message == 'hello':
    #     return 'Namaste !'
    # if p_message == 'roll':
    #     return str("Not a good idea i guess")
    
    # else:
    #     return 'Please stop pinging me!'

