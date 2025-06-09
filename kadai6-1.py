import requests
import json

APP_ID = "f721ff5d9091a3678f4b5da8dd9efee3ffde5cc8"
API_URL  = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
STATS_DATA_ID = "0003450578"  # 統計表ID（例: 経済センサス-基礎調査）
params = {
    "appId": APP_ID,
    "statsDataId": STATS_DATA_ID,
    "cdArea": "12217",
    "lang": "J",  
}

response = requests.get(API_URL, params=params)

data = response.json()

print(data)  