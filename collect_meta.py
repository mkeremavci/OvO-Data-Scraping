import requests
import json
from tqdm import trange
import os

if os.path.exists('data'):
    os.mkdir('data')


if os.path.exists('data/meta.json'):
    with open('data/meta.json', 'r') as f:
        meta_data = json.load(f)
else:
    meta_data = {}
    

url = "https://api-sonuc.oyveotesi.org/api/v1"


for i in trange(len(meta_data) + 1, 82):
    # İlçeler
    cUrl = f"{url}/cities/{i}/districts"
    response = requests.get(cUrl)
    data = response.json()
    
    meta_data[i] = {x['name']: {} for x in data}
    nkeys = [x['id'] for x in data]
    nnames = [x['name'] for x in data]
    
    # Mahalleler
    for nkey, nname in zip(nkeys, nnames):
        nUrl = f"{cUrl}/{nkey}/neighborhoods"
        response = requests.get(nUrl)
        data = response.json()
        
        meta_data[i][nname] = {x['name']: {} for x in data}
        skeys = [x['id'] for x in data]
        snames = [x['name'] for x in data]
        
        for skey, sname in zip(skeys, snames):
            sUrl = f"{nUrl}/{skey}/schools"
            response = requests.get(sUrl)
            data = response.json()
            
            meta_data[i][nname][sname] = {x['name']: x['id'] for x in data}
    
    with open('data/meta.json', 'w') as f:
        f.write(json.dumps(meta_data, indent=4))
