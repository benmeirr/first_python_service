from typing import Optional

from model.customer_order import CustomerOrder
from model.customer_order_request import CustomerOrderRequest
from model.customer_order_response import CustomerOrderResponse
from repository import customer_order_repository, customer_repository
from service import customer_service


async def get_by_id(customer_order_id: int) -> Optional[CustomerOrder]:
    return await customer_order_repository.get_by_id(customer_order_id)


async def create_customer_order(customer_order_request: CustomerOrderRequest) -> CustomerOrderResponse:
    selected_customer = customer_order_request.customer
    if selected_customer.id is None:
        customer_id = await customer_service.create_customer(selected_customer)
        selected_customer = await customer_service.get_by_id(customer_id)
        customer_order_request.customer_order.customer_id = selected_customer.id
    else:
        existing_customer = await customer_service.get_by_id(selected_customer.id)
        if existing_customer is None:
            raise Exception(f"Can't find existing customer with id: {selected_customer.id}")
        else:
            customer_order_request.customer_order.customer_id = existing_customer.id
            selected_customer = existing_customer

    customer_order = customer_order_request.customer_order
    await customer_order_repository.create_customer_order(customer_order)

    customer_orders = await customer_order_repository.get_by_customer_id(selected_customer.id)
    return CustomerOrderResponse(customer=selected_customer, customer_orders=customer_orders)







async def update_customer_order(customer_order_id: int, customer_order: CustomerOrderRequest) -> CustomerOrderResponse:
    ## Homework - complete the update logic
    pass


async def delete_by_id(customer_order_id: int):
    await customer_order_repository.delete_by_id(customer_order_id)
