
from typing import Optional
from pydantic import BaseModel


class AddressCreate(BaseModel):
    name: str
    address: str
    latitude: float
    longitude: float


class AddressUpdate(BaseModel):
    name: Optional[str]
    address: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]


class AddressDB(AddressCreate):
    id: int

    class Config:
        orm_mode = True


class Address(AddressCreate):
    id: int

    class Config:
        orm_mode = True
