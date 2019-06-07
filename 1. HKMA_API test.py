# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 22:46:36 2019

@author: Dick Sang
"""

import urllib.request
import pandas as pd
import requests

url = 'https://api.hkma.gov.hk/public/market-data-and-statistics/monthly-statistical-bulletin/financial/monetary-statistics?offset=0'

data = requests.get(url)
data_json = data.json()