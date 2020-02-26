from collections import defaultdict
from typing import List

from baas.models import Card, Compra


class CardStorage:
    def __init__(self):
        self.__card_by_acc_id = defaultdict(list)
        self.__compra_by_card_id = defaultdict(list)
        self.__card_by_id = {}
        self.__compra_by_date = defaultdict(list)

    def save_card(self, acc_id: str, card: Card):
        self.__card_by_acc_id[acc_id].append(card)
        self.__card_by_id[card.numero] = card

    def get_by_card_id(self, card_id: str) -> Card:
        return self.__card_by_id[card_id]

    def list_cards(self):
        return [card[1] for card in self.__card_by_id.items()]

    def save_compra(self, card_id: str, compra: Compra):
        self.__compra_by_card_id[card_id].append(compra)
        self.__compra_by_date[compra.data].append(compra)

    def list_compras_by_date(self, date: str):
        return self.__compra_by_date[date]

    def list_compras_by_card_id(self, card_id: str) -> List[Compra]:
        return self.__compra_by_card_id[card_id]


class CardService:

    storage = CardStorage()

    @classmethod
    async def save_card(cls, acc_id: str, card: Card):
        cls.storage.save_card(acc_id, card)

    @classmethod
    def list_cards(cls) -> List[Card]:
        return cls.storage.list_cards()

    @classmethod
    def get_card_by_id(cls, card_id: str) -> Card:
        return cls.storage.get_by_card_id(card_id)

    @classmethod
    def save_compra(cls, card_id: str, compra: Compra):
        cls.storage.save_compra(card_id, compra)

    @classmethod
    def list_compras_by_card_id(cls, card_id: str) -> List[Compra]:
        return cls.storage.list_compras_by_card_id(card_id)
