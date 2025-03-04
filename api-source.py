from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from datetime import date
import uuid

app = FastAPI()

class Item(BaseModel):
    nome: str = Field(max_length=25)
    valor: float
    data: date

@app.post("/processar-item/")
async def processar_item(item: Item):
    if item.data > date.today():
        raise HTTPException(status_code=400, detail="A data não pode ser no futuro.")
    
    return item.model_dump() | {"uuid": str(uuid.uuid4())}