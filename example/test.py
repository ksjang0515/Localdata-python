import requests
import os
import xmltodict
from datetime import datetime
from dotenv import load_dotenv
from constants import *


if(__name__ == "__main__"):
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    start_date = "20220802"
    end_date = datetime.now().strftime('%Y%m%d')
    print(end_date)

    params = {
        "authKey": API_KEY,
        "lastModTsBgn": start_date,
        "lastModTsEnd": end_date,
        "pageIndex": "75",
        "pageSize": "100",
        "resultType": "json"
    }

    res = requests.get(API_DOMAIN, params)
    result = res.json()
    print(result)
    print("1")
    print(params)
    # print(res_dict['result']['body']['rows']['row'])
