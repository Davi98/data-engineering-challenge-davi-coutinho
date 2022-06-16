from google.cloud import bigquery
from src.utils.log import log
import json

class Bigquery:

    def __init__(self,project_id,dataset,table):
        self.client = bigquery.Client()
        self.project_id = project_id
        self.dataset = dataset
        self.table = table

        
    def insert_row(self,data):
        table_id = f"{self.project_id}.{self.dataset}.{self.table}"
        data = (json.loads(data))
        row_to_insert = [data]
        errors = self.client.insert_rows_json(table_id, row_to_insert)  # Make an API request.
        # if errors == []:
        #     log().debug("New rows have been added.")
        #     return True
        # else:
        #     log().error(f"Encountered errors while inserting rows: {errors}")
        #     return False
        
    def query_average_with_coord(self,origin_coord,destination_coord):
        query = """
        SELECT name, SUM(number) as total_people
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = 'TX'
        GROUP BY name, state
        ORDER BY total_people DESC
        LIMIT 20
        """
        query_job = self.client.query(query)  # Make an API request.

        for row in query_job:
            
            print("name={}, count={}".format(row[0], row["total_people"]))
            
    def query_average_with_region(self,region):
        query = """
        SELECT name, SUM(number) as total_people
        FROM `bigquery-public-data.usa_names.usa_1910_2013`
        WHERE state = 'TX'
        GROUP BY name, state
        ORDER BY total_people DESC
        LIMIT 20
        """
        query_job = self.client.query(query)  # Make an API request.

        for row in query_job:
            
            print("name={}, count={}".format(row[0], row["total_people"]))