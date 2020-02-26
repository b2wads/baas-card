from typing import List

from aiohttp import web
from asyncworker import RouteTypes

from baas.app import app
from baas.http import parse_body, parse_id
from baas.models import Card, Compra
from baas.services.card import CardService


@app.route(["/cards"], type=RouteTypes.HTTP, methods=["POST"])
@parse_body(Card)
async def create_card(card: Card) -> Card:
    await CardService.save_card(card.acc_id, card)
    return web.json_response(card.dict())


@app.route(["/cards"], type=RouteTypes.HTTP, methods=["GET"])
async def list_cards() -> List[Card]:
    cards = CardService.list_cards()
    return web.json_response([card.dict() for card in cards])


@app.route(["/cards/{card_id}"], type=RouteTypes.HTTP, methods=["GET"])
@parse_id(str)
async def get_card_by_id(card_id: str) -> Card:
    card = CardService.get_card_by_id(card_id)
    return web.json_response(card.dict())


@app.route(["/cards/{card_id}/compra"], type=RouteTypes.HTTP, methods=["POST"])
@parse_body(Compra)
async def nova_compra(compra: Compra) -> Compra:
    CardService.save_compra(compra.card_id, compra)
    return web.json_response(compra.dict())


@app.route(["/health"], type=RouteTypes.HTTP, methods=["GET"])
async def health():
    return web.json_response({"OK": True})
