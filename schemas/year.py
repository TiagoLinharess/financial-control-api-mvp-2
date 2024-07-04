from models import Month, Year
from typing import List
from schemas.month import MonthSchema

class YearSchema:

    # Inicializa response
    def __init__(self, year: Year):
        self.year = year.year
        self.id = year.id
        self.months: List[MonthSchema] = list(map(get_month, year.months))

    # Transforma objeto em json
    def to_json(self):
        return {
            "year": self.year,
            "id": self.id,
            "months": list(map(get_month_json, self.months))
        }

class YearListSchema:

    # Inicializa response
    def __init__(self, years: List[Year]):
        self.years = get_schema_list(years)

    # Transforma objeto em json
    def to_json(self):
        return {
            "years": get_schema_list_json(self.years)
        }

# Transforma model Year em  para Json
def get_schema(year: Year) -> YearSchema:
    return YearSchema(year)

# Transforma lista Years para Json
def get_schema_list(years: List[Year]) -> List[YearSchema]:
    return list(map(get_schema, years))
        
# Transforma YearSchema para Json
def get_schema_json(year: YearSchema):
    return year.to_json()

# Transforma YearListSchema para Json
def get_schema_list_json(years: List[YearSchema]):
    return list(map(get_schema_json, years))

# Transforma model Month para MonthSchema
def get_month(month: Month) -> MonthSchema:
    return MonthSchema(month)

# Transforma model MonthSchema para Json
def get_month_json(month: MonthSchema):
    return month.to_json()

    