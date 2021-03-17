from typing import List

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from . import models
from .pyap_address_parser import pyap_parse

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/extract/pyap", response_model=List[models.PyapAddress])
def extract_using_pyap(input: models.PyapParseOptions):
    return pyap_parse(input.text, country=input.country, rule_name=input.rule_name)
