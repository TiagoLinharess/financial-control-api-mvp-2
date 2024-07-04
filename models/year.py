from sqlalchemy import Column, String, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from typing import Union

from models import Base, Month

class Year(Base):
    __tablename__ = 'year'

    id = Column("pk_year" , Integer, primary_key=True)
    year = Column(String(4))
    date_insert = Column(DateTime, default=datetime.now())

    # Definição do relacionamento entre o Year e um Month.
    # Aqui está sendo definido a coluna 'months' que vai guardar
    # a referencia ao months, a chave estrangeira que relaciona
    # varios months ao year.
    months = relationship("Month")

    def __init__(self, year: str, date_insert:Union[DateTime, None] = None):
        """
        Cria um Year

        Arguments:
            year: o ano a ser criado.
            data_insercao: data de quando o comentário foi feito ou inserido
                           à base
        """
        self.year = year
        if date_insert:
            self.date_insert = date_insert
    
    def add_month(self, month:Month):
        self.months.append(month)