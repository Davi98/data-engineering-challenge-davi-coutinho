import unittest
import json
from webapp import app


class FlaskTest(unittest.TestCase):
    
    #check if response 200
    def test_response_code(self):
        tester = app.test_client(self)
        body = [{
        "region": "belo",
        "origin_coord": "POINT (14.4973794438195 50.00136875782316)",
        "destination_coord": "POINT (14.4973794438195 50.00136875782316)",
        "datetime": "2018-05-28 09:03:40",
        "datasource": "funny_car"
        }]
        
        response = tester.post("/insert",json=body)
        response_code = response.status_code
        self.assertEqual(response_code,200)
        
    #check if returned application/json
    def test_returned_content_type(self):
        tester = app.test_client(self)
        body = [{
        "region": "belo",
        "origin_coord": "POINT (14.4973794438195 50.00136875782316)",
        "destination_coord": "POINT (14.4973794438195 50.00136875782316)",
        "datetime": "2018-05-28 09:03:40",
        "datasource": "funny_car"
        }]
        
        response = tester.post("/insert",json=body)
        self.assertEqual(response.content_type,'application/json')
        

    # check if valid json return final_status with valids = 1 and inserteds = 1
    def test_returned_valid(self):
        tester = app.test_client(self)
        body = [{
        "region": "belo",
        "origin_coord": "POINT (14.4973794438195 50.00136875782316)",
        "destination_coord": "POINT (14.4973794438195 50.00136875782316)",
        "datetime": "2018-05-28 09:03:40",
        "datasource": "funny_car"
        }]
        
        response = tester.post("/insert",json=body)
        json_data = (json.loads(response.text))
        self.assertEqual(json_data.get('valids'),1)
        self.assertEqual(json_data.get('inserteds'),1)

    # check if invalid json return final_status with invalids = 1
    def test_returned_invalid(self):
        tester = app.test_client(self)
        body = [{
        "region": "belo",
        "origin_coord": "POINT (14.4973794438195 50.00136875782316)",
        "destination_coord": "POINT (14.4973794438195 50.00136875782316)",
        # "datetime": "2018-05-28 09:03:40",
        "datasource": "funny_car"
        }]
        response = tester.post("/insert",json=body)
        json_data = (json.loads(response.text))
        self.assertEqual(json_data.get('invalids'),1)

if __name__ == "__main__":
    unittest.main()