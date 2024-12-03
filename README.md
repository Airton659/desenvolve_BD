# **ZeDelivery Partner Locator API**

Esta é uma API para gerenciar parceiros e encontrar o parceiro mais próximo com base em uma localização geográfica. A aplicação utiliza **FastAPI**, **SQLAlchemy** e suporte a dados espaciais com **MySQL**.

---

## **Índice**

- [Requisitos](#requisitos)
- [Instalação](#instalação)
- [Configuração](#configuração)
- [Execução](#execução)
- [Endpoints](#endpoints)
- [Exemplos de uso](#exemplos-de-uso)

---

## **Requisitos**

- Python 3.10 ou superior
- MySQL com suporte a funções espaciais
- Dependências Python listadas no `requirements.txt`

---

## **Instalação**

1. Clone o repositório:

   ```bash
   git clone https://github.com/Airton659/desenvolve_BD.git
   cd zedelivery

2. Crie e ative um ambiente virtual:

   ```bash
   python -m venv venv
   source venv/bin/activate  # Para Windows: venv\Scripts\activate

3. Instale as dependências
   ```bash
   pip install -r requirements.txt

## **Configuração**

1. Configure o banco de dados no arquivo database.py:
   ```bash
   DATABASE_URL = "mysql+pymysql://<USUARIO>:<SENHA>@<HOST>:<PORTA>/<NOME_DO_BANCO>"

2. Certifique-se de que o banco de dadoas possui suporte para dados espaciais. Execute o seguinte comando SQL para adicionar a extensão espacial:
   ```bash
   ALTER TABLE partners 
   ADD COLUMN coverageArea GEOMETRY NOT NULL,
   ADD COLUMN address GEOMETRY NOT NULL;

3. Inicialize o banco de dados:
   ```bash
   python -c "from app.database import Base, engine; Base.metadata.create_all(engine)"


## **Execução**

1. Inicie o servidor:
   ```bash
   uvicorn app.main:app --reload

2. Acesse a documentação interativa no Swagger em:
   ```bash
   http://127.0.0.1:8000/docs


## **Endpoints**

1. Criar Parceiro:   
* **URL**: /partners
* **Método**: POST
* **Descrição**: Adiciona um novo parceiro no banco de dados.
* **Payload de Exemplo**:
  ```bash
  {
   "tradingName": "Adega Osasco",
   "ownerName": "Ze da Ambev",
   "document": "02.453.716/000170",
   "coverageArea": {
      "type": "MultiPolygon",
      "coordinates": [
         [
            [
               [-43.36556, -22.99669],
               [-43.36539, -23.01928],
               [-43.26583, -23.01802],
               [-43.36556, -22.99669]
            ]
         ]
      ]
   },
   "address": {
      "type": "Point",
      "coordinates": [-43.297337, -23.013538]
   }
}

2. Buscar Parceiro por ID:   
* **URL**: /partners/{id}
* **Método**: GET
* **Descrição**: Retorna os detalhes de um parceiro com base no ID.
* **Exemplo de resposta**:
  ```bash
  {
   "id": 1,
   "tradingName": "Adega Osasco",
   "ownerName": "Ze da Ambev",
   "document": "02.453.716/000170",
   "coverageArea": {
      "type": "MultiPolygon",
      "coordinates": [ ... ]
   },
   "address": {
      "type": "Point",
      "coordinates": [-43.297337, -23.013538]
   }
}

1. Buscar Parceiro Mais Próximo:   
* **URL**: /closest
* **Método**: GET
* **Parâmetros de Query**:
  * lat (float): Latitude da localização fornecida pelo usuário;
  * lon (float): Longitude da localização fornecida pelo usuário.
* **Descrição**: Retorna o parceiro mais próximo cuja área de cobertura inclui as coordenadas fornecidas.

## **Exemplos de uso**

**Exemplo 1: Criar Parceiro**
Envie uma requisição POST para `http://127.0.0.1:8000/partners` com o payload de exemplo listado acima.

**Exemplo 2: Buscar Parceiro por ID**
Envie uma requisição GET para `http://127.0.0.1:8000/partners/1`.

**Exemplo 3: Buscar Parceiro Mais Próximo**
Envie uma requisição GET para `http://127.0.0.1:8000/closest?lat=-23.01353&lon=-43.297337`.
    
