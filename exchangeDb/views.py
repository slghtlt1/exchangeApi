import json
from urllib.request import urlopen
from . import models

def getJson():
    url = "http://localhost:3005/api/v1/ohlc?coin=BTC&exchange=binance&since=now-5m"

    response = urlopen(url)
    data_load = json.loads(response.read())
    print(data_load)
    arrayJson = []
    for i in range(len(data_load)):
        """myDict = {'index': i,
                  'open_time': data_load[i]['open_time'],
                  'close_time': data_load[i]['close_time'],
                  'open_field': data_load[i]['open'],
                  'close_field': data_load[i]['close'],
                  'high_Field': data_load[i]['high'],
                  'low_Field': data_load[i]['low'],
                  'volume_Field': data_load[i]['volume'],
                  'count_Field': data_load[i]['count'],
                  }"""
        if data_load[i]['count'] != 'None':
            arrayJson.append(data_load[i]['count'])
    sumNumber = 0
    for i in arrayJson:
        sumNumber = sumNumber + i

    return sumNumber


def saveDateModified():
    url = "http://localhost:3005/api/v1/ohlc?coin=BTC&exchange=binance&since=now-5m"
    response = urlopen(url)
    data_load = json.loads(response.read())

    exchangeDtls = models.GetData(open_Timee=data_load[0]['open_time'],
                           close_Time=data_load[0]['close_time'],
                           open_Field=data_load[0]['open'],
                           close_Field=data_load[0]['close'],
                           high_Field=data_load[0]['high'],
                           low_Field=data_load[0]['low'],
                           volume_Field=data_load[0]['volume'],
                           count_Field=data_load[0]['count'],
                           sum_Field=getJson())
    exchangeDtls.save()
    print(getJson())
#gitexchange
