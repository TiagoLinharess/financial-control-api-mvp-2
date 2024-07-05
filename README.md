# Financial Control API MVP 2

Este pequeno projeto é a segunda versão da API do MVP do Financial Control

O objetivo do projeto é um crud completo com criação, listagem, edição e deleção de contas voltadas para a organização financeira, sendo agrupadas por usuário meses e anos, contendo 4 rotas.

**GET BILL ITEMS**: Uma rota para buscar as contas do mês e ano do usuário.

**POST BILL ITEMS**: Uma rota para salvar a conta do mês e ano do usuário.

**PUT BILL ITEMS**: Uma rota para editar a conta do mês e ano do usuário.

**DELETE BILL ITEMS**: Uma rota para deletar a conta do mês e ano do usuário.

---
## Como executar

Será necessário ter todas as libs python listadas no `requirements.txt` instaladas, é bem simples o processo.

Após clonar o repositório, é necessário ir ao diretório raiz do projeto, pelo terminal, para poder executar os comandos descritos abaixo.

Criação do env

```bash
python -m venv env
```
Inicialização do env

```bash
source env/bin/activate
```
Instalação das dependências

```bash
(env)$ pip install -r requirements.txt
```

Para executar a API  basta executar:

```
(env)$ flask run --host 0.0.0.0 --port 5002
```

Em modo de desenvolvimento é recomendado executar utilizando o parâmetro reload, que reiniciará o servidor
automaticamente após uma mudança no código fonte. 

```
(env)$ flask run --host 0.0.0.0 --port 5002 --reload
```

### Executando com Docker

Criação da rede (Necessária para se comunicar com as outras apis)

```bash
docker network create financial-control-network 
```

Criação da imagem:

```bash
docker build -t financial-control-mvp-2 .
```

Execução da imagem:

```bash
docker run -d --name financial-control-mvp-2 --network financial-control-network -p 5002:5002 financial-control-mvp-2
