from google.cloud import bigquery
from src.utils.log import log
import json

class Bigquery:

    def __init__(self,project_id,dataset,table):
        self.client = bigquery.Client()
        self.project_id = project_id
        self.dataset = dataset
        self.table = table
        self.table_id = f"{self.project_id}.{self.dataset}.{self.table}"

        
    def insert_row(self,data):
        try: 
            data = (json.loads(data))
            row_to_insert = [data]
            errors = self.client.insert_rows_json(self.table_id, row_to_insert)  # Make an API request.
            if errors == []:
                log().debug("New rows have been added.")
                return True
            else:
                log().error(f"Encountered errors while inserting rows: {errors}")
                return False
        except Exception as err:
            log().error(f"Error in insert_row method {err}")
    
    def query_average_with_coord(self,longitude,latitude):
        try:
            query = f"""
                WITH
                coords_week AS (
                SELECT
                    EXTRACT(WEEK
                    FROM
                    datetime) AS week,
                    COUNT(*) AS number,
                FROM
                    `streamingsdata.challenge.Geopoints_Final`
                WHERE
                    destination_longitude < {longitude}
                    AND destination_latitude < {latitude}
                GROUP BY
                    week
                ORDER BY
                    week ASC)
                SELECT
                AVG(number) as average
                FROM
                coords_week
                        """
            query_job = self.client.query(query)  # Make an API request.

            for row in query_job:
                return str(row['average'])
        except Exception as err:
            log().error(f"Error in query_average_with_coord method {err}")

            
    def query_average_with_region(self,region):
        try:
            query = f"""
                WITH
                region_week AS (
                SELECT
                    EXTRACT(WEEK
                    FROM
                    datetime) AS week,
                    COUNT(*) AS number,
                FROM
                    `streamingsdata.challenge.Geopoints_Final`
                WHERE
                    region = "{region}"
                GROUP BY
                    week
                ORDER BY
                    week ASC)
                SELECT
                AVG(number) as average
                FROM
                region_week
                        """
            query_job = self.client.query(query)  # Make an API request.

            for row in query_job:
                return str(row['average'])
            
        except Exception as err:
            log().error(f"Error in query_average_with_region method {err}")