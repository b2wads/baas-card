from aiohttp.client import ClientSession

from baas.conf import settings
from baas.models import Account


class AccountClient:
    @classmethod
    async def get_by_id(cls, acc_id) -> Account:
        async with ClientSession() as session:
            async with session.get(
                f"{settings.ACCOUNT_SERVICE_ADDRESS}/accounts/{acc_id}"
            ) as resp:
                data = await resp.json()
                return Account(**data)
