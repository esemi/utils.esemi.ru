import hashlib
import uuid
import urllib.parse

import requests


template = "https://utils.esemi.ru/screenshot-miner/mnr.html?page=%s#nA8P6IYnM3KluYUc7geYgUGObEERrGQF"


def thumbalizr(options=None):
    host = "https://api.thumbalizr.com/api/v1/embed/%s/%s/"
    embed_key = 'oDITorXh3HutRCqsRdIfL9xH6ywxB'
    secret = 'XsYbuNaz4NNiBTfNDncaWKdBCt3ui'

    if not options:
        options = {}
    params = options
    params['url'] = template % uuid.uuid4().hex

    query = urllib.parse.urlencode(params)
    token = hashlib.md5((query + secret).encode('utf-8')).hexdigest()

    resp = requests.get(host % (embed_key, token), params=params)
    return resp.status_code


for i in range(300):
    print(thumbalizr({'width': 2000, 'format': 'png'}))
