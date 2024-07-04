import json
from models import Item

class ItemSchema:

    # Inicializa response
    def __init__(self, item: Item):
        self.id: str = item.id
        self.name: str = item.name
        self.id: int = item.id
        self.type: str = item.type
        self.value: float = item.value
    
    # Transforma objeto em json
    def to_json(self):
        return {
            "name": self.name,
            "id": self.id,
            "type": self.type,
            "value": self.value
        }
