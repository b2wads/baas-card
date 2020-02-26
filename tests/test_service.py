from asynctest import TestCase

from baas.models import Card, Compra
from baas.services.card import CardService


class ServiceTest(TestCase):
    async def test_save_card(self):
        card = Card(numero="10", acc_id="1234")
        await CardService.save_card(card.acc_id, card)
        self.assertEqual(card, CardService.get_card_by_id("10"))

    async def test_list_all_card(self):
        card = Card(numero="10", acc_id="1234")
        card_2 = Card(numero="11", acc_id="4321")
        await CardService.save_card(card.acc_id, card)
        await CardService.save_card(card_2.acc_id, card_2)

        self.assertEqual([card, card_2], CardService.list_cards())

    async def test_save_compra(self):
        compra = Compra(data="2020-02-26", valor=100, card_id="10")
        card = Card(numero="10", acc_id="1234")

        await CardService.save_card(card.acc_id, card)
        CardService.save_compra("10", compra)

        self.assertEqual([compra], CardService.list_compras_by_card_id("10"))

    async def test_list_compra_por_card_id_empty_list(self):
        self.assertEqual([], CardService.list_compras_by_card_id("10"))
