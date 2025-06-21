from pydantic import BaseModel
from typing import List


class usuario(BaseModel):
    user_id: int


class usuarios(BaseModel):
    usuarios: List[usuario]
