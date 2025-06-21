from fastapi import APIRouter, status
from interfaces.usuario import usuarios

route = APIRouter()

users = [{"user_id": 1}, {"user_id": 2}, {"user_id": 3}, {"user_id": 4}, {"user_id": 5}]

@route.get('/usuarios', response_model=usuarios, operation_id=  "get_users_id", tags= ["Users"], status_code=status.HTTP_200_OK, response_description="Retorna todos os usuários")
async def retorna_usuario():
    return users


@route.get('/usuarios/{user_id}', operation_id=  "get_user_id", tags= ["Users"], status_code=status.HTTP_200_OK, response_description="Retorna um usuário")
async def retorna_usuario(user_id: int):
    return user_id
