import os
from flask import Flask, request,abort
from src.google.Publisher import Publisher
from src.google.Bigquery import Bigquery
import src.utils.enviroment as env
import src.utils.json_validator  as json_validator
import logging
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)
from src.utils.log import log

app = Flask(__name__)



project = env.GOOGLE_CLOUD_PROJECT
subscription_name = env.GOOGLE_CLOUD_SUBSCRIPTION
dataset = env.DATASET
table = env.TABLE
bq = Bigquery(project,dataset,table)
publisher = Publisher("challenge",env.GOOGLE_CLOUD_PROJECT)


log().info("Starting webapp")

@app.route('/insert', methods=['POST'])
def insert():
    try:
        valids = 0
        inserteds = 0
        data = request.json
        
        log().info(f"Recived {len(data)} trips in request")
        
        log().debug(f"Starting validated trips")
        for trip in data:
            valid = json_validator.validateJson(trip)
            if valid:
                valids = valids + 1
                log().debug(f"Starting publish data in pubsub")
                inserted = publisher.publish(data=trip)
                if inserted is True:
                    inserteds = inserteds + 1
                
        
        final_status = {
            "valids": valids,
            "invalids": len(data) - valids,
            "inserteds": inserteds,
            "total" : len(data)
            
            }
        
        log().info(f"Ending of execution with final_status:{final_status}")

        
        return final_status

    except Exception as err:
      log().error(f"Error in insert method at webapp: {type(err)} > {err}")
      raise err
  
@app.route('/average_with_coord', methods=['GET'])
def average_with_coord():
    try:
        longitude = request.args.get('longitude',"")
        latitude = request.args.get('latitude',"")
        if longitude == "" or latitude == "":
            log().error("please send valid requests args")
            abort(400)
        else:
            return bq.query_average_with_coord(longitude,latitude)
    except Exception as err:
      log().error(f"Error in average_with_coord method at webapp: {type(err)} > {err}")
      raise err

@app.route('/average_with_region', methods=['GET'])
def average_with_region():
    try:
        region = request.args.get('region',"")
        if region == "":
            log().error("please send valid requests args")
            abort(400)
        else:
            return bq.query_average_with_region(region)
    except Exception as err:
      log().error(f"Error in average_with_region method at webapp: {type(err)} > {err}")
      raise err

    
if __name__ == '__main__':
   app.run(debug=False,host='0.0.0.0',port=int(os.environ.get('PORT', 8080)))