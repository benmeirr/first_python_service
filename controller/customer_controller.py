from fastapi import APIRouter, HTTPException

from model.customer import Customer
from typing import List
from service import customer_service

router = APIRouter(
    prefix="/customer",
    tags=["customer"]
)


@router.get("/{customer_id}", response_model=Customer)
async def get_customer(customer_id: int):
    customer = await customer_service.get_by_id(customer_id)
    if not customer:
        raise HTTPException(status_code=404, detail=f"Customer with id: {customer_id} not found")
    return customer


@router.post("/")
async def create_customer(customer: Customer):
    try:
        await customer_service.create_customer(customer)
    except Exception:
        raise HTTPException(
            status_code=404, detail="Can't create new VIP customer - Out of limit"
        )


@router.put("/{customer_id}")
async def update_customer(customer_id: int, customer: Customer):
    existing_customer = await customer_service.get_by_id(customer_id)
    if not existing_customer:
        raise HTTPException(
            status_code=404, detail=f"Can't update customer with id: {customer_id}, customer not found"
        )
    await customer_service.update_customer(customer_id, customer)


@router.delete("/{customer_id}", response_model=Customer)
async def delete_customer(customer_id: int):
    await customer_service.delete_customer(customer_id)


@router.get("/", response_model=List[Customer])
async def get_customers():
    return await customer_service.get_all()
