from fastapi import APIRouter


router = APIRouter()


@router.get("/buscar_habilidades")
def buscar_habilidades():

    return 0