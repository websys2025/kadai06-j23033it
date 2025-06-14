import csv
import requests
from io import StringIO

"""
参照するオープンデータ:
- データ名: 柏市AED設置場所一覧 (CSV形式)
- 概要: 千葉県柏市内に設置されているAED（自動体外式除細動器）の
        設置場所、施設名、利用可能時間などの情報を提供するデータです。
- エンドポイント (CSV_URL): https://www.city.kashiwa.lg.jp/documents/24924/122173_aed_1.csv
- 機能: AEDの設置場所情報をCSV形式で提供します。
        各行が1つの設置場所に対応し、列には施設名、住所、
        設置階、利用可能曜日・時間などが含まれます。
- 取得方法: requestsライブラリを使用してCSVファイルをダウンロードし、
        csvモジュールを使用して読み込みます。
"""

CSV_URL = "https://www.city.kashiwa.lg.jp/documents/24924/122173_aed_1.csv"

response = requests.get(CSV_URL)
response.encoding = 'shift_jis'  # Ensure the encoding is set to utf-8

csv_file = StringIO(response.text)

reader = csv.reader(csv_file)

header = next(reader)
print(f"ヘッダー: {header}")

for i , row in enumerate(reader):
    if i < 5:
        print(row)
    else:
        break