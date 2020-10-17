import requests
import datetime
import logging
import json

logging.basicConfig(level=logging.DEBUG)


def get_prices_with_timestamps(symbol):
    return requests.get(
        f'https://www.bankier.pl/new-charts/get-data?date_from={dateFrom}&date_to={dateTo}&symbol={symbol}&intraday=false').json().get(
        'main')


companies = list(map(lambda el: el.get('s'), requests.get('https://www.bankier.pl/sdata/300/pfinstruments')
                     .json()
                     .get("0")))

dateFrom = str(datetime.datetime(2020, 5, 1).timestamp()).replace(".", "") + "00"
dateTo = str(datetime.datetime.now().timestamp()).replace(".", "")

d = dict()

for company in companies:
    d[company] = get_prices_with_timestamps(company)

with open(f'result-{dateTo}.json', 'w') as fp:
    json.dump(d, fp)
