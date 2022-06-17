# Challenge-api
This is API was created for a Data Engineering Challenge test at Jobsity

![Alt text](diagram.png?raw=true "Title")

# Technology used
This API was built with python3 using the flask lib and pubsub queue.


# How to start aplication
## Create python virtualenv and install depedencies:
virtualenv env -p python3.8

source env/bin/activate

pip install -r requirements.txt

## Download credentials.json that was sent in email, move this to the repository folder and set as env var:
export GOOGLE_APPLICATION_CREDENTIALS="credentials.json"

## To start the aplication just run in two differents terminal :
python webapp.py

python subscriber.py

### You can start the webapp using the Dockerfile, I created a script to facilitated(credentials.json must be in repository folder):
sh dev.sh

The webapp start on port 8080 and it's ready to receive http requests follow the patterns bellow: Also, I share the postman collection on the repository

## POST endpoint
http://192.168.0.42:8080/insert

### Body json schema:
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
### Response from POST
```json
{
    "inserteds": 2,
    "invalids": 1,
    "total": 3,
    "valids": 2
}
```
### GET average_with_coord endpoint
http://192.168.0.42:8080/average_with_coord?longitude=14.4973794438195&latitude=50.07877245872595

#### The params are:
| Name | Description |
| --- | ---|
|longitude|	longitude that you are filterig|
|latitude| latitude that you are filterig|

The response from this method is the average

### GET average_with_region endpoint
http://192.168.0.42:8080/average_with_region?region=Turin

#### The params are:
|Name	|Description|
| ---| ---|
|region	|region that you are filterig|

The response from this method is the average

__

# Challange
#### Mandatory Features

● There must be an automated process to ingest and store the data. ✅
Using PubSub + Insert in bigquery

● Trips with a similar origin, destination, and time of days should be grouped. ✅
In the view "streamingsdata.challenge.trips_final"

● Develop a way to obtain the weekly average number of trips for an area, defined by a bounding box (given by coordinates) or by a region. ✅
Two different GET methods in API

● Develop a way to inform the user about the status of the data ingestion without using a polling solution. ✅
It's possible to see the status from data ingestion on logs, response and also the user can see in PubSub interface the status of the queue

● The solution should be scalable to 100 million entries. It is encouraged to simplify the data by a data model. Please add proof that the solution is scalable. ✅
In the tests folder, the file "perfomance_test.py" can be used to test the scalability of the API, you can edit in "### Test Settings ###" some configs for the test. To run the test just run this in terminal: python -m tests.perfomance_test

● Use a SQL database. ✅
Google Bigquery

#### Bonus features

● Containerize your solution. ✅
Dockerfile

● Sketch-up how you would set up the application using any cloud provider (AWS, Google Cloud, etc).✅
I created some YAML files in Kubernets folder (k8s), you can use these files, the bitbucket-pipelines and Dockerfile to deploy the application on Google Cloud

● Include a .sql file with queries to answer these questions:
○ From the two most commonly appearing regions, which is the latest data source? ✅
○ What regions have the "cheap_mobile" Datasource appeared in? ✅
SQL folder in the project