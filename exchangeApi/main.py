import json
import requests
from urllib.request import urlopen

"""
def getJson():
    url = "http://localhost:3005/api/v1/ohlc?coin=BTC&exchange=binance&since=now-5m"
    response = urlopen(url)

    response = urlopen(url)
    data_load = json.loads(response.read())
    print(data_load)

    for i in range(len(getJson())):
        open_time = data_load[i]['open_time']
        close_time = data_load[i]['close_time']
        open_field = data_load[i]['open']
        close_field = data_load[i]['close']
        high_Field = data_load[i]['high']
        low_Field = data_load[i]['low']
        volume_Field = data_load[i]['volume']
        count_Field = data_load[i]['count']

    print(open_time)
    print(close_time)
    print(open_field)
    print(close_field)
    print(high_Field)
    print(low_Field)
    print(volume_Field)
    print(count_Field)



print(getJson())"""
