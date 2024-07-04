from flask_openapi3 import OpenAPI, Info, Tag
from flask_cors import CORS
from flask import redirect
from controllers import post_bill_items
from schemas import ResponseErrorSchema, ResponseSuccessSchema, RequestPostSchema

# Inicializa API
info = Info(title="Financial Control API MVP 2", version="1.0.0")
app = OpenAPI(__name__, info=info)
CORS(app)

# Documentação
home_tag = Tag(name="Documentação", description="Seleção de documentação: Swagger, Redoc ou RapiDoc")
@app.get('/', tags=[home_tag])
def home():
    return redirect('/openapi')

# Rota POST
post_bill_items_tag = Tag(name="Criar conta", description="Cria conta agrupada por mês e ano.")
@app.post('/bill_items', tags=[post_bill_items_tag], responses={"201": ResponseSuccessSchema, "400": ResponseErrorSchema})
def post(form: RequestPostSchema):
    return post_bill_items(form)