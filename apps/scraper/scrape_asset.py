

import requests


CMC_API = 'https://api.coinmarketcap.com'


def cmc_endpoint(endpoint):
    return CMC_API + endpoint


def extract_assets():
    response = requests.get(cmc_endpoint('/v1/ticker/?limit=5000'))
    if response.status_code == 200:
        return response.json()
    else:
        raise Exception("CMC unavailable")


if __name__ == '__main__':
    resp = extract_assets()
    print('Fetched total ' + str(len(resp)))
