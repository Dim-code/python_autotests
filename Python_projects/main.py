import requests

token = 'f30138cd908cfb006f5212f76ad9f754'
response = requests.post ('https://pokemonbattle.me:9104/trainers/reg',
              headers = {'Content-Type' : 'application/json'},
              json= {"trainer_token": token,"email":"Genna@gmail.ru",
                     "password": "iLoveqa117"})

print( response.json() )


response_confirm = requests.post ('https://pokemonbattle.me:9104/trainers/confirm_email',
              headers = {'Content-Type' : 'application/json'},
              json= {"trainer_token": token})

print( response_confirm.json() )



token = 'f30138cd908cfb006f5212f76ad9f754'
add_pokemon_response = requests.post ('https://pokemonbattle.me:9104/pokemons',
              headers = {'Content-Type' : 'application/json','trainer_token': token},
              json= {"name": "Хитрo",
    "photo": "https://dolnikov.ru/pokemons/albums/097.png"})

print( add_pokemon_response.json())


token = '0e43c49437ba86451e420741c845f937'
change_pokemon_response = requests.put ('https://pokemonbattle.me:9104/pokemons',
              headers = {'Content-Type' : 'application/json','trainer_token': token},
              json= {
    "pokemon_id": 6085,
    "name": "Gusto",
    "photo": "https://dolnikov.ru/pokemons/albums/097.png"}
)

print( change_pokemon_response.json())

token = 'f30138cd908cfb006f5212f76ad9f754'
add_pokebol_response = requests.post ('https://pokemonbattle.me:9104/trainers/add_pokeball',
              headers = {'Content-Type' : 'application/json','trainer_token': token},
              json= { "pokemon_id": "6085"})

print( add_pokebol_response.json())
