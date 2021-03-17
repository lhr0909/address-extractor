from typing import List
import pyap

from .models import PyapAddress

def pyap_parse(text: str, **kwargs) -> List[PyapAddress]:
    addresses = pyap.parse(text, **kwargs)
    return [PyapAddress.parse_obj(address.as_dict()) for address in addresses]
