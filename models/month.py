from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from models import Base, Item

class Month(Base):
    __tablename__ = 'month'

    id = Column("pk_month", Integer, primary_key=True)
    month = Column(String(20))
    date_insert = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o Months e um Year.
    # Aqui está sendo definido a coluna 'year' que vai guardar
    year = Column(Integer, ForeignKey("year.pk_year"), nullable=False)
    items = relationship("Item")

    def __init__(self, month: str, date_insert:Union[DateTime, None] = None):
        """
        Cria um Month
        Arguments:
            month: o mês a ser criado.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.month = month
        if date_insert:
            self.date_insert = date_insert
    
    def add_item(self, item: Item):
        self.items.append(item)