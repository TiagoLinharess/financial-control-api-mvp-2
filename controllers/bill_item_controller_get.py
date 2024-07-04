from repositories import YearRepository, MonthRepository, ItemRepository
from models import Session, Year, Month, Item
from schemas import YearListSchema, get_default_error, RequestGetSchema
from typing import List

# Rota de GET do endpoint de Bill Items
def get_bill_items(query: RequestGetSchema):
    try:
        if query.user_id == "":
            raise ValueError("Please, insert a valid user_id")

        # Cria sessão
        session = Session()

        # Procura anos
        years = get_years(session)

        # Loop para buscar os meses
        for year in years:

            # Procura os meses
            months = get_months(session, year)

            # Atribui meses ao ano
            year.months = months

            # Loop para buscar os items
            for month in months:

                # Atribui items ao mês
                month.items = get_items(session, month, query.user_id)
        
        # Loop para deletar os anos e meses se necessário
        formatted_years = remove_empty_years_and_months(years)

        # Transforma Model em JSON
        year_list_schema_json = YearListSchema(formatted_years).to_json()

        # Ordena JSON
        year_list_schema_json['years'] = sorted(year_list_schema_json['years'], key=extract_year, reverse=True)

        # Retorna resultado
        return year_list_schema_json
    except Exception as e:
        # Retorno de erro da rota
        return get_default_error(str(e))

def extract_year(json):
    return int(json['year'])


def get_years(session: Session) -> List[Year]:
    try:
        # Instancia repositório
        year_repository = YearRepository(session)

        # Busca anos se existirem no repositório
        return year_repository.read()
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on fetching year: " + str(e))

def get_months(session: Session, year: Year) -> List[Month]:
    try:
        # Instancia repositório
        month_repository = MonthRepository(session)

        # Busca meses se existirem no repositório
        return month_repository.read(year)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on fetching month: " + str(e))

def get_items(session: Session, month: Month, user_id: str) -> List[Item]:
    try:
        # Instancia repositório
        item_repository = ItemRepository(session)

        # Busca meses se existirem no repositório
        return item_repository.read(month, user_id)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on fetching items: " + str(e))

def remove_empty_years_and_months(years: List[Year]) -> List[Year]:
    for year in years[:]:
        
        # Loop para deletar os meses se necessário
        for month in year.months[:]:
            if not month.items:
                year.months.remove(month)
        
        # Loop para deletar os anos se necessário
        if not year.months:
            years.remove(year)

    return years

    
    