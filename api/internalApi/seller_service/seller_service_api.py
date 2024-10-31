from typing import Optional

import httpx

from api.internalApi.seller_service.model.item_response import ItemResponse
from config.config import Config

config = Config()


async def get_lowest_price_item_by_name(item_name: str) -> Optional[ItemResponse]:
    url = f"{config.SELLER_SERVICE_BASE_URL}/item/search/"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, params={"item_name": item_name})
            response.raise_for_status()

            data = response.json()

            item_response = ItemResponse(
                id=data.get("id"),
                seller_id=data.get("seller_id"),
                item_name=data.get("item_name"),
                price=data.get("price")
            )

            return item_response
        except httpx.HTTPStatusError as exception:
            print(f"Error in getting item details for item name {item_name} with error: {exception.response}")
            return None


async def get_item_by_item_id(item_id: int) -> Optional[ItemResponse]:
    url = f"{config.SELLER_SERVICE_BASE_URL}/item/{item_id}"

    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url)
            response.raise_for_status()

            data = response.json()

            item_response = ItemResponse(
                id=data.get("id"),
                seller_id=data.get("seller_id"),
                item_name=data.get("item_name"),
                price=data.get("price")
            )

            return item_response
        except httpx.HTTPStatusError as exception:
            print(f"Error in getting item details for item id {item_id} with error: {exception.response}")
            return None
