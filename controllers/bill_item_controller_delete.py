from repositories import ItemRepository
from models import Session
from schemas import get_default_error, get_default_success, RequestDeleteSchema

# Rota de DELETE do endpoint de Bill Items
def delete_bill_items(form: RequestDeleteSchema):
    try:
        # Cria sessão
        session = Session()

        # Procura campo id no body
        id = int(form.id)

        # Instancia reposirtório
        item_repository = ItemRepository(session)

        # Deleta item
        if not item_repository.delete(id):
            raise ValueError("Não foi possível deletar conta")
        
        # Executa commit no banco de dados
        session.commit()

        # Retorno de sucesso da rota
        return get_default_success()
    except Exception as e:
        # Retorno de erro da rota
        return get_default_error(str(e))