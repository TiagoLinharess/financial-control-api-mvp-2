import json
from schemas.item import ItemSchema
from models import Month, Item
from typing import List

class MonthSchema:

    # Inicializa response
    def __init__(self, month: Month):
        self.month: str = month.month
        self.id: int = month.id
        self.incomes: List[ItemSchema] = get_item_income(month.items)
        self.outcomes: List[ItemSchema] = get_item_outcome(month.items)
    
    # Transforma objeto em json
    def to_json(self):
        return {
            "month": self.month,
            "id": self.id,
            "incomes": list(map(get_item_json, self.incomes)),
            "outcomes": list(map(get_item_json, self.outcomes))
        }

# Transforma model Item para ItemSchema
def get_item_income(items: List[Item]) -> List[ItemSchema]:
    return get_item_schema(items, "income")

# Transforma model Item para ItemSchema
def get_item_outcome(items: List[Item]) -> List[ItemSchema]:
    return get_item_schema(items, "outcome")

# Transforma model Item para ItemSchema
def get_item_schema(items: List[Item], type: str):
    item_schema: List[ItemSchema] = []

    for item in items:
        if item.type == type:
            item_schema.append(ItemSchema(item))

    return item_schema

# Transforma model ItemSchema para Json
def get_item_json(item: ItemSchema):
    return item.to_json()