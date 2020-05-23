import requests
import os
import json
import pprint
from six.moves import configparser

def get():
    config = configparser.ConfigParser()
    config.read(os.path.dirname(__file__)+'/conf.txt')

    token = config.get('section','token')
    url = 'https://api.nature.global/1/devices'
    token = 'Bearer ' + token
    headers = {'Content-type': 'application/json', 'Authorization': token}

    response = requests.get(url, headers=headers)
    result = json.loads(response.text)

    # pprint.pprint(result[0]['newest_events'])

    out=dict()
    for k,v in result[0]['newest_events'].items():
        out[k]=v['val']
    # pprint.pprint(out)

    return out

if __name__ == '__main__':
    get()
