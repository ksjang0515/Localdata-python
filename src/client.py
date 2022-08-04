import requests
from utils import check_date_format
from exceptions import LocaldataException


class LocaldataClient:
    def __init__(self, api_key: str, api_domain: str):
        self.api_domain = api_domain
        self.api_key = api_key

    def call(self, params: dict) -> tuple[dict, dict]:
        # send get request
        response = requests.get(self.api_domain, params)

        # process data
        result = response.json()  # extract json
        status = result['result']['header']['process']  # get request status

        return (status, result)

    def get_change(self, start_date: str, end_date: str, page_index: int, page_size: int = 100) -> tuple[int, dict]:
        # check for date format
        if(not check_date_format(start_date) and not check_date_format(end_date)):
            raise LocaldataException(
                'date needs to have format of YYYYMMDD.', start_date, end_date)

        params = {
            "authKey": self.api_key,
            "lastModTsBgn": start_date,
            "lastModTsEnd": end_date,
            "pageIndex": str(page_index),
            "pageSize": str(page_size),
            "resultType": "json"
        }

        (status, result) = self.call(params)

        # process data
        # check request status and throw error
        if(status['code'] != '00'):
            raise LocaldataException(status)

        # total number of available rows
        total_count = result['result']['header']['paging']['totalCount']
        # list of rows recieved
        change_list = result['result']['body']['rows'][0]['row']

        return (total_count, change_list)
