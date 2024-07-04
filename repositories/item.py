from models import Session, Month, Item
from schemas.edit import ItemEditSchema
from typing import List

class ItemRepository():
    # Propriedade de tipo da conta
    types = ["income", "outcome"]

    # Inicializa repositório
    def __init__(self, session: Session):
        self.__session = session

    # Método create do repositório
    def create(self, month: Month, user_id: str, name: str, type_string: str, value: float):
        if not self.is_valid(type_string):
            raise ValueError("Item is not valid.")

        item = Item(user_id, name, type_string, value)
        
        month.add_item(item)
    
    # Método read do repositório
    def read(self, month: Month, user_id: str) -> List[Item]:
        items = self.__session.query(Item).filter(Item.month == month.id).filter(user_id == Item.user_id).all()
        return items

    # Método update do repositório
    def update(self, schema: ItemEditSchema):
        if not self.is_valid(schema.type):
            raise ValueError("Item is not valid.")

        self.__session.query(Item).filter(Item.id == schema.id).update(
            {
                "name": schema.name,
                "type": schema.type,
                "value": schema.value
            }
        )

    # Método delete do repositório
    def delete(self, item_id: int) -> bool:
        count = self.__session.query(Item).filter(Item.id == item_id).delete()

        if count:
            return True
        else:
            return False

    # Método is_valid do repositório
    def is_valid(self, type_string: str) -> bool:
        if type_string in self.types: 
            return True
        else:
            return False