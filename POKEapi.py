import requests

base_url = "https://pokeapi.co/api/v2/"

def getPokemonInfo(name):
    url = f"{base_url}pokemon/{name}"
    response = requests.get(url)
    print(response)
    if(response.status_code == 200):
        pokemonData = response.json()
        return pokemonData
    else:
        print("Pokemon not found")


while(True):
    pokemonName = input("Enter pokemon name: ").lower().strip()
    pokemonInfo = getPokemonInfo(pokemonName)

    if pokemonInfo:
        print(f"Name: {pokemonInfo['name']}")
        print(f"Height: {pokemonInfo['height']}")
        print(f"Weight: {pokemonInfo['weight']}")
        #print(f"Type: {pokemonInfo['type']}")