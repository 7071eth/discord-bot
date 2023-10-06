import requests

def handle_response(message) -> str:

    p_message = message.lower()

    url = f'https://huggingface.co/api/models?search={p_message}&limit=5'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        model_ids =[]
        for x in data:
            model_id = x['modelId']
            model_ids.append(model_id)
        print(model_ids)
        return str(model_ids)

    else:
        return "No results found"

    # if p_message == 'hello':
    #     return 'Namaste !'
    # if p_message == 'roll':
    #     return str("Not a good idea i guess")
    
    # else:
    #     return 'Please stop pinging me!'

