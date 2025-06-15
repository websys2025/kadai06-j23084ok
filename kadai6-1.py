import requests

APP_ID = "ba5a7b1b6a648fd0a2e078220f4777a7a9b1a38c" # "ここに自分のアプリケーションIDを書く"
API_URL  = "https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId":"0004021080", #国民生活基礎調査/所得
    "cdCat01": "038", #令和４年の情報
    
    "lang": "J"  # 日本語を指定
}



#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)

"""
取得したデータの種類：JSON型
エンドポイント：https://api.e-stat.go.jp/rest/3.0/app/json/getStatsData
機能：国民生活基礎調査のうちの所得を年次別に表示
使い方：cdCatで年次を選択
"""