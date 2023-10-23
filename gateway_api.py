#%%
import requests
import json


pin_df_example = {'index': 1000, 'unique_id': 'e3361e4b-e1fd-44b7-a9b7-da6ae1a1512d', 'title': 'The Exact Regimen You Should Be Following for Your Skin Type', 'description': 'The Exact Regimen You Should Be Following for Your Skin Type via @ByrdieBeauty', 'poster_name': 'Byrdie', 'follower_count': '538k', 'tag_list': 'Skin Tips,Skin Care Tips,Skin Secrets,Organic Skin Care,Natural Skin Care,Organic Beauty,Organic Makeup,Natural Beauty,Natural Face', 'is_image_or_video': 'image', 'image_src': 'https://i.pinimg.com/originals/4d/8f/b9/4d8fb970e7233a363c4adea197fc589d.gif', 'downloaded': 1, 'save_location': 'Local save in /data/beauty', 'category': 'beauty'}
#geo_df_example = {'ind': 1000, 'timestamp': datetime.datetime(2021, 6, 20, 6, 8, 14), 'latitude': -81.8896, 'longitude': -153.897, 'country': 'American Samoa'}
#usr_df_example = {'ind': 1000, 'first_name': 'Angela', 'last_name': 'Berg', 'age': 20, 'date_joined': datetime.datetime(2015, 11, 10, 5, 57, 33)}


invoke_url_pin = "https://qsmuml0e2h.execute-api.us-east-1.amazonaws.com/test/topics/12570a5c330b.pin"
#invoke_url_geo = "https://qsmuml0e2h.execute-api.us-east-1.amazonaws.com/test/topics/12570a5c330b.geo"
#invoke_url_usr = "https://qsmuml0e2h.execute-api.us-east-1.amazonaws.com/test/topics/12570a5c330b.user"


#To send JSON messages you need to follow this structure
payload_pin = json.dumps({
    "records": [
        {
        #Data should be send as pairs of column_name:value, with different columns separated by commas       
        "value": {"index": pin_df_example["index"], "unique_id": pin_df_example["unique_id"], "title": pin_df_example["title"], "description": pin_df_example["description"], "poster_name": pin_df_example["poster_name"], "follower_count": pin_df_example["follower_count"], "tag_list": pin_df_example["tag_list"], "is_image_or_video": pin_df_example["is_image_or_video"], "image_src": pin_df_example["image_src"], "downloaded": pin_df_example["downloaded"], "category": pin_df_example["category"]}
        }
    ]
})

'''
payload_geo = json.dumps({

    "records": [
        {
        #Data should be send as pairs of column_name:value, with different columns separated by commas       
        "value": {"ind": geo_df_example["ind"], "timestamp": geo_df_example["timestamp"], "latitude": geo_df_example["latitude"], "longitude": geo_df_example["longitude"], "country": geo_df_example["country"]}
        }
    ]
})

payload_usr = json.dumps({
    "records": [
        {
        #Data should be send as pairs of column_name:value, with different columns separated by commas       
        "value": {"ind": usr_df_example["ind"], "first_name": usr_df_example["first_name"], "last_name": usr_df_example["last_name"], "age": usr_df_example["age"], "date_joined": usr_df_example["date_joined"]}
        }
    ]
})
'''

headers = {'Content-Type': 'application/vnd.kafka.json.v2+json'}

response_pin = requests.request("POST", invoke_url_pin, headers=headers, data=payload_pin)
#response_geo = requests.request("POST", invoke_url_geo, headers=headers, data=payload_geo, default=json_serial)
#response_usr = requests.request("POST", invoke_url_usr, headers=headers, data=payload_usr, default=json_serial)

print(response_pin.status_code)
#print(response_geo.status_code)
#print(response_usr.status_code)
#%%
