from models import Year
from typing import List
from pydantic import BaseModel

class ResponseErrorSchema(BaseModel):
    error: str = "Ocorreu um erro"

class ResponseSuccessSchema(BaseModel):
    success: bool = True

class ResponseIncomeSchema(BaseModel):
    id: int = 1
    name: str = "Bill"
    type: str = "income"
    value: float = 100

class ResponseOutcomeSchema(BaseModel):
    id: int = 2
    name: str = "Bill"
    type: str = "saída"
    value: float = 100

class ResponseMonthSchema(BaseModel):
    id: int = 1
    month: str = "april"
    incomes: List[ResponseIncomeSchema]
    outcomes: List[ResponseOutcomeSchema]

class ResponseYearSchema(BaseModel):
    year: str = "2024"
    id: int = 1
    months: List[ResponseMonthSchema]

class ResponseYearsListSchema(BaseModel):
    years: List[ResponseYearSchema]

# Retorno padrão de erro
def get_default_error(exception: str):
    return {
        "error": exception
    }, 400

# Retorno padrão de sucesso
def get_default_success():
    return { "success": True }, 200