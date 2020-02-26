from asynctest import TestCase

from baas.models import Card, Compra
from baas.services.card import CardStorage


class StorageTest(TestCase):
    async def setUp(self):
        self.storage = CardStorage()
        self.acc_id = "123"
        self.acc_id_2 = "321"

    async def test_list_cards(self):
        card = Card(numero="11", acc_id=self.acc_id)
        card_2 = Card(numero="12", acc_id=self.acc_id_2)
        self.storage.save_card(card.acc_id, card)
        self.storage.save_card(card_2.acc_id, card_2)

        self.assertEqual([card, card_2], self.storage.list_cards())

    async def test_get_card_by_id(self):
        card = Card(numero="11", acc_id=self.acc_id)
        card_2 = Card(numero="12", acc_id=self.acc_id_2)
        self.storage.save_card(card.acc_id, card)
        self.storage.save_card(card_2.acc_id, card_2)

        self.assertEqual(card, self.storage.get_by_card_id(card.numero))
        self.assertEqual(card_2, self.storage.get_by_card_id(card_2.numero))

    async def test_list_compras_by_data(self):
        compra = Compra(valor=20, card_id="11", data="2020-02-26")
        self.storage.save_compra(compra.card_id, compra)

        self.assertEqual(
            [compra], self.storage.list_compras_by_date("2020-02-26")
        )
        self.assertEqual([], self.storage.list_compras_by_date("2020-01-10"))

    async def test_save_nova_compra(self):
        compra = Compra(valor=20, card_id="11", data="2020-02-26")
        self.storage.save_compra(compra.card_id, compra)

        self.assertEqual([compra], self.storage.list_compras_by_card_id("11"))
