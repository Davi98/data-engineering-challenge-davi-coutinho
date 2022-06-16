# Challenge-api
This is api created for a test for the Data Engineering Challenge at Jobsity

# Technology used
The api was build with python3 using the flask lib and pubsub queue.

___

# How to start aplication
## Create python virtualenv and install depedencies:
virtualenv env -p python3.8 <br />
source env/bin/activate <br />
pip install -r requirements.txt

## Download credentials.json  that was sent in email ,move this to repository folder and set as env var:
export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"

## To start aplication just run in two differents terminal :

python webapp.py

python subscriber.py

## You can start the webapp using the Dockerfile, I created a script to facilitated(credentials.json must be in repository folder):
sh dev.sh

The webapp start on port 8080 and it's ready to receive http requests follow the patterns bellow:

___

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
}]
```

## Response from POST
```json
{
    "inserteds": 2,
    "invalids": 1,
    "total": 3,
    "valids": 2
}
```
___

## GET average_with_coord endpoint
http://192.168.0.42:8080/average_with_coord?origin_coord=POINT (14.4973794438195 50.00136875782316)&destination_coord=POINT (14.6610239449707 50.07877245872595)

### The params are:

| Name | Description |
| --- | --- |
| origin_coord | origin coordinate |
| destination_coord | destination coordinate |


## Response from GET average_with_region : 


___

## GET average_with_region endpoint
http://192.168.0.42:8080/average_with_region?region=Turing

### The params are:
| Name | Description |
| --- | --- |
| region | region |



## Response from GET average_with_region : 
