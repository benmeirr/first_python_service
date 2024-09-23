from typing import List, Optional

from starlette import status
from fastapi import APIRouter, HTTPException, Query
from starlette import status

from model.order import Order

router = APIRouter(
    prefix="/order",
    tags=["order"]
)

orders = {}  # order_id --> Order


# Full CRUD for Order entity:
@router.get("/{order_id}", response_model=Order, status_code=status.HTTP_200_OK)
def get_order_by_id(order_id: int) -> Order:
    order = orders.get(order_id)
    if not order:
        raise HTTPException(status_code=400, detail=f"Order with order_id: {order_id} not found")
    else:
        return order


@router.post("/", response_model=Order, status_code=status.HTTP_201_CREATED)
def create_order(order: Order) -> Order:
    if order.order_id in orders:
        raise HTTPException(status_code=400, detail=f"Order Id {order.order_id} is already existing")
    else:
        orders[order.order_id] = order
        return order


@router.put("/{order_id}", response_model=Order, status_code=status.HTTP_200_OK)
def update_order(order_id: int, order: Order) -> Order:
    if order_id not in orders:
        raise HTTPException(status_code=400, detail=f"Can't update order Id {order_id}, order_id is not existing")
    else:
        orders[order_id] = order
        return order


@router.delete("/{order_id}", status_code=status.HTTP_200_OK)
def delete_order(order_id: int):
    try:
        orders.pop(order_id)
    except:
        pass


@router.get("/customer/name", response_model=List[Order])
def get_orders_by_customer(customer_name: Optional[str] = Query(None)) -> List[Order]:
    order_results = []
    for order in orders.values():
        if order.customer_name == customer_name:
            order_results.append(order)
    return order_results

