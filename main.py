import requests
import json
from tqdm import tqdm
import os
import time
import random

with open('meta.json', 'r') as f:
    meta_data = json.load(f)


if os.path.exists('data.json'):
    with open('data.json', 'r') as f:
        scraped = json.load(f)
else:
    scraped = {}


url = "https://api-sonuc.oyveotesi.org/api/v1/submission/school"
headers = {
    'Accept': 'application/json, text/plain, */*',
    'Referer': 'https://tutanak.oyveotesi.org/',
    'Sec-Ch-Ua': '"Google Chrome";v="113", "Chromium";v="113", "Not-A.Brand";v="24"',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/113.0.0.0 Safari/537.36'
    }


for ckey, city in tqdm(list(meta_data.items())):
    if ckey in scraped:
        cToken = True
    else:
        cToken = False
        scraped[ckey] = {}
        
    for dkey, distinct in city.items():
        if dkey in scraped[ckey]:
            dToken = True
        else:
            dToken = False
            scraped[ckey][dkey] = {}
            
        if cToken and dToken:
            continue
        
        for nkey, neigh in distinct.items():
            scraped[ckey][dkey][nkey] = {}
            for skey, sid in neigh.items():
                scraped[ckey][dkey][nkey][skey] = {}
                
                sUrl = f"{url}/{sid}"
                status_code = 0
                while status_code != 200:
                    response = requests.get(sUrl, headers=headers)
                    status_code = response.status_code
                    time.sleep(random.uniform(2, 5))
                    print(status_code)
                data = response.json()

                time.sleep(random.uniform(0.25, 1))
                
                for d in data:
                    scraped[ckey][dkey][nkey][skey][d['ballot_box_number']] = {
                        'cm_result': d['cm_result'],
                        'mv_result': d['mv_result'],
                    }
                

        with open('data.json', 'w') as f:
            f.write(json.dumps(scraped, indent=4))
