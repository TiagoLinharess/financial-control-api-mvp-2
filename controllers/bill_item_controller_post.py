from repositories import YearRepository, MonthRepository, ItemRepository
from models import Session, Year, Month
from schemas import DefaultRequestSchema, get_default_error, get_default_success, RequestPostSchema

# Rota de POST do endpoint de Bill Items
def post_bill_items(form: RequestPostSchema):
    try:
        # Cria sessão
        session = Session()

        # Cria Schema
        schema = read_post_body(form)
        
        # Cria ano se não existir
        year = save_year(session, schema.get_year())

        # Cria mês se não existir
        month = save_month(session, schema.get_month(), year)

        # Cria item
        save_item(session, schema.get_user_id(), schema.get_name(), schema.get_type(), schema.get_value(), month)

        # Executa commit no banco de dados
        session.commit()

        # Retorno de sucesso da rota
        return get_default_success()
    except Exception as e:
        # Retorno de erro da rota
        return get_default_error(str(e))

def read_post_body(form: RequestPostSchema) -> DefaultRequestSchema:
    # Busca body da rota de POST
    user_id = form.user_id
    year = form.year
    month = form.month.lower()
    bill_type = form.type.lower()
    name = form.name
    value = float(form.value)

    # Verifica valor do body
    if not year or not month or not bill_type or not name or not value:
        raise ValueError("Invalid params.")

    # Retornos do schema
    return DefaultRequestSchema(user_id, year, month, bill_type, name, value)

def save_year(session: Session, year: str) -> Year:
    try:
        # Instancia repositório
        year_repository = YearRepository(session)

        # Cria ano se existir no repositório
        return year_repository.create(year)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on saving year: " + str(e))

def save_month(session: Session, month_string: str, year: Year) -> Month:
    try:
        # Instancia repositório
        month_repository = MonthRepository(session)

        # Cria mês se não existir no repositório
        return month_repository.create(month_string, year)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on saving month: " + str(e))

def save_item(session: Session, user_id: str, name: str, type_string: str, value: float, month: Month):
    try:
        # Instancia repositório
        item_repository = ItemRepository(session)

        # Cria item
        item_repository.create(month, user_id, name, type_string, value)
    except Exception as e:
        # Tratativa de erro do repostirório
        raise ValueError("Error on saving item: " + str(e))