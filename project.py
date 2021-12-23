import requests
import datetime
import pandas as pd


url = "https://partner-query.finance.yahoo.com/v8/finance/chart/%5EDJI?range=1d&comparisons=undefined&includePrePost=false&interval=2m&corsDomain=tw.stock.yahoo.com&.tsrc=yahoo-tw"
response = requests.get(url)

close = response.json()[
    "chart"]["result"][0]["indicators"]["quote"][0]["close"]  # 美股指數
volume = response.json()[
    "chart"]["result"][0]["indicators"]["quote"][0]["volume"]  # 成交量

tw_time = []
timestamps = response.json()["chart"]["result"][0]["timestamp"]
for index in range(len(timestamps)):
    tw_time.append(datetime.datetime.utcfromtimestamp(
        timestamps[index]-18000))  # 台灣時間

data = {
    "tw_time": tw_time,
    "close": close,
    "volume": volume
}

df = pd.DataFrame(data)
print(df)
