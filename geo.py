import requests
import json


def GEO(ip):
    get_geo = requests.get(f'http://ipwhois.app/json/{ip}')
    load = json.loads(get_geo.text)
    return 'continent:',load['continent'],  'country:',load['country'], 'timezone', load['timezone']

