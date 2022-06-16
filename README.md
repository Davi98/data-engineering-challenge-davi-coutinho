# Challenge-api
This is api created for a test for the Data Engineering Challenge at Jobsity


## Technology used
The api was build with python3 with the flask lib.

## How to start aplication
### Create python virtualenv and install depedencies:
virtualenv env -p python3.8
source env/bin/activate 
pip install -r requirements.txt

### Download credentials.json  that was sent in email ,move this to repository folder and set as env var:
export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"

### To start aplication just run on terminal:

python webapp.py

The webapp start on port 8080 and it's ready to receive http requests follow the patterns bellow:

### You can start the aplication using the Dockerfile, I created a script to facilitated:



## POST endpoint
http://192.168.0.42:8080/insert

## Body json schema:
```json
[{
    "region": "Rio de Janeiro",
    "origin_coord": "POINT (14.4973794438195 50.00136875782316)",
    "destination_coord": "POINT (14.43109483523328 50.04052930943246)",
    "datetime": "2022-05-28 09:03:40",
    "datasource": "funny_car"
},
{
    "region": "São Paulo",
    "origin_coord": "POINT (14.4973794438195 50.00136875782316)",
    "destination_coord": "POINT (14.43109483523328 50.04052930943246)",
    "datetime": "2022-02-22 09:03:40",
    "datasource": "funny_car"
},
{
    "region": "Salvador",
    "origin_coord": "POINT (14.4973794438195 50.00136875782316)",
    "destination_coord": "POINT (14.43109483523328 50.04052930943246)",
    "datetime": "2022-10-31 09:03:40",
    "datasource": "funny_car"
}
]

## GET endpoint's
http://192.168.0.42:8080/average_with_coord?origin_coord=POINT (14.4973794438195 50.00136875782316)&destination_coord=POINT (14.6610239449707 50.07877245872595)

### Os parametros da chamada são:

| Nome | Descrição |
| --- | --- |
| brand |  Marca do carro |
| model | Modelo do carro |
| modelYear |  Ano do modelo do carro |
| version | Versão do carro |
| source |  Fonte da versão(fipe ou webmotors) |


## Resposta : 
Um exemplo de resposta quando a chamada GET realiza uma query válida.

```json
{
    "body": "SEDAN",
    "date": "2021-02-17 16:33:51.172071",
    "doors": "4",
    "engine": "1.8",
    "fipe": {
        "id": "023098-7",
        "price": 27311,
        "version": "1.8 SEDAN 16V FLEX 4P MANUAL"
    },
    "fuel": {
        "type": "FLEX"
    },
    "gear": "MANUAL",
    "brand": "NISSAN",
    "model": "TIIDA",
    "source": "webmotors",
    "valid": true,
    "version": {
        "fipe": "1.8 SEDAN 16V FLEX 4P MANUAL",
        "webmotors": "1.8 SEDAN 16V FLEX 4P MANUAL"
    },
    "modelYear": 2013
}
```

| Nome | Descrição |
| --- | --- |
| body | Carroceria do carro |
| doors | Número de portas do carro |
| fipe.id |  Id do carro na tabela FIPE |
| fipe.price | Preço do carro na tabela FIPE |
| fipe.version |  Versão do carro na tabela FIPE |
| fuel.type | Tipo de combustível do carro |
| gear | Câmbio do carro |
| brand |  Marca do carro |
| model | Modelo do carro |
| modelYear |  Ano do modelo do carro |
| version.fipe  |  Versão do carro na FIPE |
| version.webmotors |  Versao do carro na webmotors |
| source |  Fonte da versao(fipe ou webmotors) |
| date |  Data que a query foi executada |
| valid |  retorna se query achou um carro(true) ou não(false) |


Um exemplo de resposta quando a chamada GET realiza uma query inválida: 

```json
{
    "body": null,
    "date": "2021-02-17 16:36:09.223100",
    "doors": null,
    "engine": null,
    "fipe": {
        "id": null,
        "price": 0,
        "version": null
    },
    "fuel": {
        "type": null
    },
    "gear": null,
    "brand": "NISSAN",
    "model": "TIIDA",
    "source": "webmotors",
    "valid": false,
    "version": {
        "fipe": null,
        "webmotors": null
    },
    "modelYear": 2018
}
```