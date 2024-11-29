from fastapi import FastAPI
from api import router_equipe, router_habilidade
tags_metadata = [
    {
        "name": "Equipe",
        "description": "Gerenciamento de equipes pokemon",
    },
    {
        "name": "Habilidade",
        "description": "Gerenciamento de habilidades"

    }
]


app = FastAPI(title="Api Gerencia Pokemon",
            description="Api para gerenciar equipes pokemon",
            version="1.0.0",
            openapi_tags=tags_metadata)

app.include_router(router_equipe.router, tags=['Equipe'])
# app.include_router(router_habilidade.router, tags=['Habilidade'])