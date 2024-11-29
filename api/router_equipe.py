from fastapi import APIRouter
from fastapi.responses import JSONResponse
import requests
import json
from .schemas import Equipe

router = APIRouter()


@router.post("/criar_equipe")
def criar_equipe(dado:Equipe):

    equipe = {
        "treinador": dado.user
    }

    time_pokemon = []

    if len(dado.pokemons) > 6:
        return JSONResponse(status_code=422,content={"resultado":"Uma equipe pokemon pode ter apenas até 6 pokemons"})
    
    for pokemon in dado.pokemons:
        response = requests.get(f"https://pokeapi.co/api/v2/pokemon/{pokemon}")

        data = response.json()
        
        pokemon_data = {
            "pokedex_number" : data["id"],
            "nome" : data["name"],
            "peso" : data["weight"],
            "altura" : data["height"]
        }

        time_pokemon.append(pokemon_data)
    
    equipe["pokemons"] = time_pokemon
    print(equipe)
    with open('equipes.json','r') as arq:
        dados = json.load(arq)
    

    equipe["id_equipe"] = len(dados["equipes"])+1
    dados["equipes"].append(equipe)
    print(dados)

    with open('equipes.json', 'w') as arquivo:
        json.dump(dados, arquivo, indent=4)
        
        

    return JSONResponse(status_code=200,content={"resultado":"Equipe criada!"})
