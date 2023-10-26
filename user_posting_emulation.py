#%%
import requests
from time import sleep
import random
from multiprocessing import Process
import boto3
import json
import sqlalchemy
from sqlalchemy import text, func


class AWSDBConnector:

    def __init__(self):

        self.HOST = "pinterestdbreadonly.cq2e8zno855e.eu-west-1.rds.amazonaws.com"
        self.USER = 'project_user'
        self.PASSWORD = ':t%;yCY3Yjg'
        self.DATABASE = 'pinterest_data'
        self.PORT = 3306
        
    def create_db_connector(self):
        engine = sqlalchemy.create_engine(f"mysql+pymysql://{self.USER}:{self.PASSWORD}@{self.HOST}:{self.PORT}/{self.DATABASE}?charset=utf8mb4")
        return engine

new_connector = AWSDBConnector()


''' #Function which finds the number of rows in the tables
def find_number_of_rows():
    for i in range(1):
        engine = new_connector.create_db_connector()
            
        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data ")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            geo_string = text(f"SELECT * FROM geolocation_data ")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            user_string = text(f"SELECT * FROM user_data ")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)
            
            print(pin_result["index"])
            print(geo_result["ind"])
            print(user_result["ind"])
'''

def run_infinite_post_data_loop():
    
    current_row = 1
    
    for i in range(11153):

        engine = new_connector.create_db_connector()

        with engine.connect() as connection:

            pin_string = text(f"SELECT * FROM pinterest_data LIMIT {current_row}, 1")
            pin_selected_row = connection.execute(pin_string)
            
            for row in pin_selected_row:
                pin_result = dict(row._mapping)

            run_post_to_topic_pin(pin_result)


            geo_string = text(f"SELECT * FROM geolocation_data LIMIT {current_row}, 1")
            geo_selected_row = connection.execute(geo_string)
            
            for row in geo_selected_row:
                geo_result = dict(row._mapping)

            geo_result['timestamp'] = geo_result['timestamp'].isoformat()

            run_post_to_topic_geo(geo_result)


            user_string = text(f"SELECT * FROM user_data LIMIT {current_row}, 1")
            user_selected_row = connection.execute(user_string)
            
            for row in user_selected_row:
                user_result = dict(row._mapping)

                user_result['date_joined'] = user_result['date_joined'].isoformat()
        
            run_post_to_topic_user(user_result)



            #print(pin_result)
            #print(geo_result)
            #print(user_result)

            print("rows " + str(current_row) + "downloaded and uploaded")
            current_row += 1


def run_post_to_topic_pin(pin_result):

    invoke_url = "https://qsmuml0e2h.execute-api.us-east-1.amazonaws.com/test2/topics/12570a5c330b.pin"

    #To send JSON messages you need to follow this structure
    payload_pin = json.dumps({
        "records": [
            {
            #Data should be send as pairs of column_name:value, with different columns separated by commas       
            "value": {"index": pin_result["index"], "unique_id": pin_result["unique_id"], "title": pin_result["title"], "description": pin_result["description"], "poster_name": pin_result["poster_name"], "follower_count": pin_result["follower_count"], "tag_list": pin_result["tag_list"], "is_image_or_video": pin_result["is_image_or_video"], "image_src": pin_result["image_src"], "downloaded": pin_result["downloaded"], "category": pin_result["category"]}
            }
        ]
    })

    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}

    response_pin = requests.request("POST", invoke_url, headers=headers, data=payload_pin)

    print(response_pin.status_code)


def run_post_to_topic_geo(geo_result):

    invoke_url = "https://qsmuml0e2h.execute-api.us-east-1.amazonaws.com/test2/topics/12570a5c330b.geo"

    payload_geo = json.dumps({
        "records": [
            {
            #Data should be send as pairs of column_name:value, with different columns separated by commas       
            "value": {"ind": geo_result["ind"], "timestamp": geo_result["timestamp"], "latitude": geo_result["latitude"], "longitude": geo_result["longitude"], "country": geo_result["country"]}
            }
        ]
    })

    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}

    response_geo = requests.request("POST", invoke_url, headers=headers, data=payload_geo)

    print(response_geo.status_code)


def run_post_to_topic_user(user_result):

    invoke_url = "https://qsmuml0e2h.execute-api.us-east-1.amazonaws.com/test2/topics/12570a5c330b.user"

    payload_usr = json.dumps({
        "records": [
            {
            #Data should be send as pairs of column_name:value, with different columns separated by commas       
            "value": {"ind": user_result["ind"], "first_name": user_result["first_name"], "last_name": user_result["last_name"], "age": user_result["age"], "date_joined": user_result["date_joined"]}
            }
        ]
    })

    headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}

    response_usr = requests.request("POST", invoke_url, headers=headers, data=payload_usr)

    print(response_usr.status_code)




if __name__ == "__main__":
    run_infinite_post_data_loop()
    


#%%
