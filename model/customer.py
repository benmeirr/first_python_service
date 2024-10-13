from typing import Optional

from pydantic import BaseModel

from model.customer_status import CustomerStatus


class Customer(BaseModel):
    id: Optional[int] = None
    first_name: str
    last_name: str
    email: str
    status: CustomerStatus

