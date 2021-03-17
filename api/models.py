from typing import Optional
from pydantic import BaseModel

class PyapAddress(BaseModel):
    full_address: Optional[str] = None
    full_street: Optional[str] = None
    street_number: Optional[str] = None
    street_name: Optional[str] = None
    street_type: Optional[str] = None
    route_id: Optional[str] = None
    post_direction: Optional[str] = None
    floor: Optional[str] = None
    building_id: Optional[str] = None
    occupancy: Optional[str] = None
    city: Optional[str] = None
    region1: Optional[str] = None
    postal_code: Optional[str] = None
    country_id: str
    match_start: int
    match_end: int

class PyapParseOptions(BaseModel):
    text: str
    country: str
    rule_name: Optional[str] = None
