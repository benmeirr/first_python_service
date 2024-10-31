from typing import Optional, List

from api.internalApi.seller_service import seller_service_api
from model.customer_favorite_item import CustomerFavoriteItem
from model.customer_favorite_item_request import CustomerFavoriteItemRequest
from model.customer_favorite_item_response import CustomerFavoriteItemResponse
from repository import customer_favorite_item_repository
from service import customer_service


async def get_by_id(favorite_item_id: int) -> Optional[CustomerFavoriteItemResponse]:
    customer_favorite_item = await customer_favorite_item_repository.get_by_id(favorite_item_id)
    if customer_favorite_item is not None:
        item_details = await seller_service_api.get_item_by_item_id(customer_favorite_item.item_id)
        if item_details is not None:
            return CustomerFavoriteItemResponse(
                id=customer_favorite_item.id,
                customer_id=customer_favorite_item.customer_id,
                item_response=item_details
            )
    return None


async def get_favorite_items_by_customer_id(customer_id: int) -> List[CustomerFavoriteItemResponse]:
    customer_favorite_items = await customer_favorite_item_repository.get_favorite_items_by_customer_id(customer_id)
    response_list = [
        CustomerFavoriteItemResponse(
            id=favorite_item.id,
            customer_id=favorite_item.customer_id,
            item_response=(await seller_service_api.get_item_by_item_id(favorite_item.item_id))
        )
        for favorite_item in customer_favorite_items
    ]
    return response_list


async def create_favorite_item(customer_favorite_item_request: CustomerFavoriteItemRequest) -> Optional[int]:
    customer = await customer_service.get_by_id(customer_favorite_item_request.customer_id)
    if customer is not None:
        item_details = await seller_service_api.get_lowest_price_item_by_name(customer_favorite_item_request.item_name)
        if item_details is not None:
            existing_favorite_item = await customer_favorite_item_repository.get_by_customer_id_and_item_id(customer.id, item_details.id)
            if existing_favorite_item is None:
                customer_favorite_item = CustomerFavoriteItem(customer_id=customer.id, item_id=item_details.id)
                return await customer_favorite_item_repository.create_favorite_item(customer_favorite_item)
    return None
