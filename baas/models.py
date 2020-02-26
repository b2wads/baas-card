from pydantic import BaseModel


class Account(BaseModel):
    nome: str
    cpf: str


class Card(BaseModel):
    numero: str
    acc_id: str
    limite: int = 15000
    bloqueado: bool = False


class Compra(BaseModel):
    valor: int
    data: str
