import os
import numpy as np
from datetime import datetime
from dotenv import load_dotenv
from constants import *
from client import LocaldataClient


if(__name__ == "__main__"):
    # load env
    load_dotenv()
    API_KEY = os.getenv('API_KEY')

    # set query period
    start_date = "20220802"
    end_date = datetime.now().strftime('%Y%m%d')

    # initialize client
    client = LocaldataClient(API_KEY, API_DOMAIN)

    # get total number of data and create numpy array
    total_count, _ = client.get_change(
        start_date, end_date, page_index=1, page_size=1)
    data = np.empty(total_count, dtype=dict)

    # request data
    page_index = 1
    while(True):
        (total_count, change_list) = client.get_change(
            start_date, end_date, page_index, PAGE_SIZE)

        data[(page_index - 1)*PAGE_SIZE:page_index*PAGE_SIZE] = change_list

        # check for end
        if(len(change_list) == 0 or total_count <= change_list[-1]['rowNum']):
            break

        page_index += 1

    print("DONE")
    # print(res_dict['result']['body']['rows']['row'])
