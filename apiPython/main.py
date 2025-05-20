import requests

base_url = "https://pokeapi.co/api/v2/"


def get_pokemon_info(pokemon_name):
    url = f"{base_url}pokemon/{pokemon_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"Name: {data['name']}")
        print(f"Height: {data['height']}")
        print(f"Weight: {data['weight']}")
        print(
            f"Abilities: {[ability['ability']['name'] for ability in data['abilities']]}")
    else:
        print("Pokemon not found.")


pokemon_name = "pikachu"
get_pokemon_info(pokemon_name)
