import requests
import json
from tqdm import tqdm
import os


with open('meta.json', 'r') as f:
    meta_data = json.load(f)


if os.path.exists('data.json'):
    with open('data.json', 'r') as f:
        scraped = json.load(f)
else:
    scraped = {}


url = "https://api-sonuc.oyveotesi.org/api/v1/submission/school"


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
                response = requests.get(sUrl)
                data = response.json()
                
                for d in data:
                    scraped[ckey][dkey][nkey][skey][d['ballot_box_number']] = {
                        'cm_result': d['cm_result'],
                        'mv_result': d['mv_result'],
                    }

        with open('data.json', 'w') as f:
            f.write(json.dumps(scraped, indent=4))
