from typing import Optional

from pydantic import BaseModel


class Account(BaseModel):
    nome: str
    cpf: str


class Card(BaseModel):
    numero: str
    limite: int = 15000
    bloqueado: bool = False
    acc_id: str


class Compra(BaseModel):
    valor: int
    card_id: str
    data: str
