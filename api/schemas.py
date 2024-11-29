from typing import List
from pydantic import BaseModel

class Equipe(BaseModel):
    user:str
    pokemons:List[str]