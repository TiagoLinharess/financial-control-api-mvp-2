import json
from models import Item

class ItemSchema:

    # Inicializa response
    def __init__(self, item: Item):
        self.id: str = item.user_id
        self.name: str = item.name
        self.id: int = item.id
        self.type: str = item.type
        self.value: float = item.value
    
    # Transforma objeto em json
    def to_json(self):
        return {
            "user_id": self.user_id,
            "name": self.name,
            "id": self.id,
            "type": self.type,
            "value": self.value
        }
