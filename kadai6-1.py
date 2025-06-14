"""
参照する統計データ (e-Stat API経由):
- データ名: 男女別年齢（5歳階級）別労働力率（柏市） (統計表ID: 0003450578)
- 概要: 政府統計の総合窓口(e-Stat)が提供するAPIを利用して、
        千葉県柏市の男女別、年齢階級別の労働力率に関する統計データを取得します。
- エンドポイント (API_URL): http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
- 機能: 指定されたパラメータに基づき、統計データをJSON形式で提供します。
        - appId: 登録済みのアプリケーションID
        - statsDataId: 取得したい統計表のID
        - cdArea: データを取得する地域のコード (例: "12217" は柏市)
        - lang: 表示言語 ("J" は日本語)
- 取得方法: requestsライブラリを使用してAPIにGETリクエストを送信し、
        返却されたJSONデータを解析して利用します。
"""

import requests
import json

APP_ID = "f721ff5d9091a3678f4b5da8dd9efee3ffde5cc8"
API_URL  = "http://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"
STATS_DATA_ID = "0003450578" #男女年齢別労働力率
params = {
    "appId": APP_ID,
    "statsDataId": STATS_DATA_ID,
    "cdArea": "12217",#柏市
    "lang": "J",  
}

response = requests.get(API_URL, params=params)

data = response.json()

print(data)