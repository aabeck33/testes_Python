from typing import AsyncIterator
from pydantic import BaseModel
import asyncio


class MyFirstClass(BaseModel):
    nome: str
    idade: int
    email: str

item1 = MyFirstClass(nome='Alvaro', idade=52, email='abeck@gmail.com')

print(item1)
