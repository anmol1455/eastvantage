# routes/address.py

from typing import List
from fastapi import APIRouter, HTTPException
from fastapi_sqlalchemy import db
from models.address import Address, AddressCreate, AddressUpdate, AddressDB
from utils.distance import calculate_distance


router = APIRouter()


@router.post("/addresses/", response_model=AddressDB)
def create_address(address: AddressCreate):
    # Create a new address in the database
    db_address = AddressDB(**address.dict())
    db.session.add(db_address)
    db.session.commit()
    db.session.refresh(db_address)
    return db_address


@router.get("/addresses/{address_id}", response_model=AddressDB)
def read_address(address_id: int):
    # Retrieve an address from the database by its ID
    db_address = db.session.query(AddressDB).filter(AddressDB.id == address_id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    return db_address


@router.put("/addresses/{address_id}", response_model=AddressDB)
def update_address(address_id: int, address: AddressUpdate):
    # Update an address in the database
    db_address = db.session.query(AddressDB).filter(AddressDB.id == address_id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    for key, value in address.dict(exclude_unset=True).items():
        setattr(db_address, key, value)
    db.session.add(db_address)
    db.session.commit()
    db.session.refresh(db_address)
    return db_address


@router.delete("/addresses/{address_id}")
def delete_address(address_id: int):
    # Delete an address from the database
    db_address = db.session.query(AddressDB).filter(AddressDB.id == address_id).first()
    if not db_address:
        raise HTTPException(status_code=404, detail="Address not found")
    db.session.delete(db_address)
    db.session.commit()


@router.get("/addresses", response_model=List[AddressDB])
def list_addresses():
    # Retrieve a list of all addresses from the database
    return db.session.query(AddressDB).all()


@router.get("/addresses/nearby", response_model=List[AddressDB])
def list_addresses_nearby(latitude: float, longitude: float, distance: float):
    # Retrieve a list of addresses within a given distance of a set of coordinates
    addresses = db.session.query(AddressDB).all()
    nearby_addresses = []
    for db_address in addresses:
        address = Address(**db_address.__dict__)
        if calculate_distance(latitude, longitude, address.latitude, address.longitude) <= distance:
            nearby_addresses.append(db_address)
    return nearby_addresses
