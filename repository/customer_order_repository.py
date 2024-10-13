from typing import Optional, List

from model.customer_order import CustomerOrder
from .database import database

TABLE_NAME = "customer_order"


async def get_by_id(customer_order_id: int) -> Optional[CustomerOrder]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE id=:customer_order_id"
    result = await database.fetch_one(query, values={"customer_order_id": customer_order_id})
    if result:
        return CustomerOrder(**result)
    else:
        return None


async def get_all() -> list[CustomerOrder]:
    query = f"SELECT * FROM {TABLE_NAME}"
    results = await database.fetch_all(query)
    return [CustomerOrder(**result) for result in results]


async def create_customer_order(customer_order: CustomerOrder):
    query = f"""
        INSERT INTO {TABLE_NAME} (customer_id, item_name, price)
        VALUES (:customer_id, :item_name, :price)
    """
    values = {"customer_id": customer_order.customer_id, "item_name": customer_order.item_name,
              "price": customer_order.price}

    await database.execute(query, values)


async def update_customer_order(customer_order_id: int, customer_order: CustomerOrder):
    query = f"""
        UPDATE {TABLE_NAME}
        SET customer_id = :customer_id,
        item_name = :item_name,
        price = :price
        WHERE id = :customer_order_id
    """
    values = {"customer_order_id": customer_order_id, "customer_id": customer_order.customer_id,
              "item_name": customer_order.item_name, "price": customer_order.price}
    await database.execute(query, values)


async def delete_by_id(customer_order_id: int):
    query = f"DELETE FROM {TABLE_NAME} WHERE id=:customer_order_id"
    await database.execute(query, values={"customer_order_id": customer_order_id})


async def get_by_customer_id(customer_id: int) -> List[CustomerOrder]:
    query = f"SELECT * FROM {TABLE_NAME} WHERE customer_id=:customer_id"
    results = await database.fetch_all(query, values={"customer_id": customer_id})
    return [CustomerOrder(**result) for result in results]











