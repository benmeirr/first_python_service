from typing import Optional, List

from model.customer import Customer
from model.customer_status import CustomerStatus
from repository import customer_repository


async def get_by_id(customer_id: int) -> Optional[Customer]:
    return await customer_repository.get_by_id(customer_id)


async def get_all() -> List[Customer]:
    return await customer_repository.get_all()


async def create_customer(customer: Customer):
    if customer.status == CustomerStatus.VIP:
        vip_customers = await customer_repository.get_by_status(CustomerStatus.VIP)
        if len(vip_customers) < 3:
            await customer_repository.create_customer(customer)
        else:
            raise Exception("Can't create new VIP customer - Out of limit")
    else:
        await customer_repository.create_customer(customer)


async def update_customer(customer_id: int, customer: Customer):
    existing_customer = await customer_repository.get_by_id(customer_id)
    if existing_customer is not None:
        if customer.status == CustomerStatus.VIP:
            if existing_customer.status is not CustomerStatus.VIP:
                vip_customers = await customer_repository.get_by_status(CustomerStatus.VIP)
                if len(vip_customers) < 10:
                    await customer_repository.update_customer(customer_id, customer)
                else:
                    raise Exception("Can't update VIP customer - Out of limit")
            else:
                await customer_repository.update_customer(customer_id, customer)

        else:
            await customer_repository.update_customer(customer_id, customer)
    else:
        raise Exception(f"Can't update customer with id {customer_id}, id is not existing")


async def delete_customer(customer_id):
    await customer_repository.delete_customer(customer_id)
