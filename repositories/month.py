from models import Session, Year, Month
from typing import List

class MonthRepository():
    # Propriedade de meses
    months = ["january", "february", "march", "april", "may", "june", "july", "august", "september", "october", "november", "december"]

    # Inicializa repositório
    def __init__(self, session: Session):
        self.__session = session

    # Método create do repositório
    def create(self, month_string: str, year: Year) -> Month:
        print(1)
        existent_month = self.exist_month(month_string, year)

        if not self.is_valid(month_string):
            raise ValueError("Month is not valid.")

        if existent_month:
            return existent_month

        month = Month(month_string)
        year.add_month(month)
        return month
    
    # Método read do repositório
    def read(self, year: Year) -> List[Month]:
        months = self.__session.query(Month).filter(Month.year == year.id).all()
        return months
    
    # Método exist do repositório
    def exist_month(self, month_string: str, year: Year) -> Month:
        existent_months = self.read(year)

        for month in existent_months:
            if month.month == month_string:
                return month
        
        return

    # Método is_valid do repositório
    def is_valid(self, month_string: str) -> bool:
        if month_string in self.months: 
            return True
        else:
            return False