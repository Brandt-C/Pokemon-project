import requests

def search_pokemon(name):
    url = f"https://pokeapi.co/api/v2/pokemon/{name}"
    response = requests.get(url)

    if response.status_code == 200:
        pokemon = response.json()
        return pokemon
    else:
        return None