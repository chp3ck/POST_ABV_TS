import urllib3
import json


def request_post_json(payload_encrypted, url, path):
    header_user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) ' \
                        'Chrome/79.0.3945.74 Safari/537.36 Edg/79.0.309.43'

    http = urllib3.PoolManager()

    print('------------------------------------------------------------------------------------')
    print(f'Trying connect: {url}{path}')
    print('------------------------------------------------------------------------------------\n')

    data = {'crypted': payload_encrypted}
    encoded_data = json.dumps(data).encode('utf-8')

    try:
        r = http.request(
            'POST',
            f'{url}{path}',
            body=encoded_data,
            headers={
                'Connection': 'keep-alive',
                'User-Agent': header_user_agent,
                'Accept': 'application/json, text/plain, */*',
                'Content-Type': 'application/json;charset=UTF-8',
                'Origin': f'{url}',
                'Referer': f'{url}',
                'Accept-Encoding': 'gzip, deflate',
                'Accept-Language': 'en-US,en;q=0.9,ru-RU;q=0.8,ru;q=0.7'
            },
            timeout=urllib3.Timeout(connect=1.0, read=1.0),
            retries=10
        )
        if r.status == '200':
            print('------------------------------------------------------------------------------------\n')
            print(json.loads(r.data.decode('utf-8')))
            print('------------------------------------------------------------------------------------\n')
            print(json.loads(r.data.decode('utf-8'))['json'])
            print('------------------------------------------------------------------------------------\n')
        print(f'status: {r.status}\ndata: {r.data}\nheaders: {r.headers}\n')
    except urllib3.exceptions.ConnectTimeoutError:
        print('Connection failed!!! Timeout error, check link or server availability...')
    except urllib3.exceptions.MaxRetryError:
        print('Connection retries failed!!! Check link or server availability...')
