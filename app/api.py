import requests

def get_pokemon(pokemon_name):
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.ok:
        data = response.json()
        if 'id' not in data:
            return None
        product = {
        'pokemon_id' : data["id"],
        'pokemon_name' : data["name"],
        'abilities' : data["abilities"],
        'base_experience' : data["base_experience"],
        'attack': data["attack"],
        'sprite_url' : data["sprite_url"],
        'hp' : data["hp"],
        'defense' : data["defense"]
        }
        return product
    else:
        return None
    