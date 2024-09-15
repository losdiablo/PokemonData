import requests

base_URL="https://pokeapi.co/api/v2/"
def get_pokemon_info(name):
    url=f"{base_URL}/pokemon/{name}"
    response = requests.get(url)
    # print(response)
    if response.status_code==200:
        # print("yooohooo")
        pokemon_data=response.json()
        return pokemon_data
    else:
        print(f"failed to retrive data {response.status_code}")
    
    
    
    
pokemon_name=input("enter name: ")
pokemon_info = get_pokemon_info(pokemon_name)

if pokemon_info:
    print(f"{pokemon_info["name"]}")    
    print(f"{pokemon_info["id"]}")    
    print(f"{pokemon_info["height"]}")    
    print(f"{pokemon_info["weight"]}")    