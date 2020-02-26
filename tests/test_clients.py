from aioresponses import aioresponses
from asynctest import TestCase

from baas.clients.account import AccountClient
from baas.models import Account


class AccountClientTest(TestCase):
    async def test_get_by_id(self):
        acc = Account(nome="Dalton", cpf="42", saldo=400)
        with aioresponses() as rsps:
            rsps.get(
                "http://accounts.api/accounts/42",
                payload=acc.dict(),
                status=200,
            )

            account = await AccountClient.get_by_id("42")
            self.assertEqual(acc.dict(), account.dict())
