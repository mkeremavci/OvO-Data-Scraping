import json
from tqdm import tqdm


with open("data.json", "r") as f:
    scraped = json.load(f)

with open("parti_listesi.json", "r") as f1, open("cb_listesi.json", "r") as f2, open("matches.json", "r") as f3:
    parti_listesi = json.load(f1)
    cb_listesi = json.load(f2)
    matches = json.load(f3)

mv_adaylar = {f"{i+1}": parti_listesi[i] for i in range(len(parti_listesi))}
cb_adaylar = {f"{i+1}": cb_listesi[i] for i in range(len(cb_listesi))}


mv_urls, mv_ovo = {}, {}
cb_urls, cb_ovo = {}, {}

for match in tqdm(matches):
    data = scraped[match[0]]
    
    mv_ovo[match[1]] = {
        'stats': {'sandik': 0, 'tutanak': 0, 'total_vote': 0, 'adaylar': {k: 0 for k in mv_adaylar.values()}},
        'ilceler': {}
    }
    cb_ovo[match[1]] = {
        'stats': {'sandik': 0, 'tutanak': 0, 'total_vote': 0, 'adaylar': {k: 0 for k in cb_adaylar.values()}},
        'ilceler': {}
    }
    mv_urls[match[1]], cb_urls[match[1]] = {}, {}
    
    for d, ddata in data.items():
        mv_ovo[match[1]]['ilceler'][d] = {
            'stats': {'sandik': 0, 'tutanak': 0, 'total_vote': 0, 'adaylar': {k: 0 for k in mv_adaylar.values()}},
            'sandiklar': {}
        }
        cb_ovo[match[1]]['ilceler'][d] = {
            'stats': {'sandik': 0, 'tutanak': 0, 'total_vote': 0, 'adaylar': {k: 0 for k in cb_adaylar.values()}},
            'sandiklar': {}
        }
        mv_urls[match[1]][d], cb_urls[match[1]][d] = {}, {}
        
        for n, ndata in ddata.items():
            for s, sdata in ndata.items():
                for idx, idata in sdata.items():
                    cmres, mvres = idata['cm_result'], idata['mv_result']

                    mv_urls[match[1]][d][idx] = None
                    cb_urls[match[1]][d][idx] = None

                    '''Presidential Election'''
                    cb_ovo[match[1]]['stats']['sandik'] += 1
                    cb_ovo[match[1]]['ilceler'][d]['stats']['sandik'] += 1
                    cb_ovo[match[1]]['ilceler'][d]['sandiklar'][idx] = {
                        'total_vote': 0, 'tutanak': False, 'adaylar': {k: 0 for k in cb_adaylar.values()}, 
                    }
                    
                    if cmres is not None:
                        cb_urls[match[1]][d][idx] = cmres["image_url"]

                        cb_ovo[match[1]]['stats']['tutanak'] += 1
                        cb_ovo[match[1]]['stats']['total_vote'] += cmres['total_vote']

                        cb_ovo[match[1]]['ilceler'][d]['stats']['tutanak'] += 1
                        cb_ovo[match[1]]['ilceler'][d]['stats']['total_vote'] += cmres['total_vote']

                        cb_ovo[match[1]]['ilceler'][d]['sandiklar'][idx]['tutanak'] = True
                        cb_ovo[match[1]]['ilceler'][d]['sandiklar'][idx]['total_vote'] = cmres['total_vote']
                        
                        for vk, vv in cmres['votes'].items():
                            cb_ovo[match[1]]['stats']['adaylar'][cb_adaylar[vk]] += vv
                            cb_ovo[match[1]]['ilceler'][d]['stats']['adaylar'][cb_adaylar[vk]] += vv
                            cb_ovo[match[1]]['ilceler'][d]['sandiklar'][idx]['adaylar'][cb_adaylar[vk]] = vv
                                 
                    '''Parliamentary Election'''
                    mv_ovo[match[1]]['stats']['sandik'] += 1
                    mv_ovo[match[1]]['ilceler'][d]['stats']['sandik'] += 1
                    mv_ovo[match[1]]['ilceler'][d]['sandiklar'][idx] = {
                        'total_vote': 0, 'tutanak': False, 'adaylar': {k: 0 for k in mv_adaylar.values()},
                    }
                    
                    if mvres is not None:
                        mv_urls[match[1]][d][idx] = mvres["image_url"]

                        mv_ovo[match[1]]['stats']['tutanak'] += 1
                        mv_ovo[match[1]]['stats']['total_vote'] += mvres['total_vote']

                        mv_ovo[match[1]]['ilceler'][d]['stats']['tutanak'] += 1
                        mv_ovo[match[1]]['ilceler'][d]['stats']['total_vote'] += mvres['total_vote']

                        mv_ovo[match[1]]['ilceler'][d]['sandiklar'][idx]['tutanak'] = True
                        mv_ovo[match[1]]['ilceler'][d]['sandiklar'][idx]['total_vote'] = mvres['total_vote']
                        
                        for vk, vv in mvres['votes'].items():
                            mv_ovo[match[1]]['stats']['adaylar'][mv_adaylar[vk]] += vv
                            mv_ovo[match[1]]['ilceler'][d]['stats']['adaylar'][mv_adaylar[vk]] += vv
                            mv_ovo[match[1]]['ilceler'][d]['sandiklar'][idx]['adaylar'][mv_adaylar[vk]] = vv
                            
    
with open("ovo_cb.json", "w") as f1, open("ovo_mv.json", "w") as f2, open("cb_urls.json", "w") as f3, open("mv_urls.json", "w") as f4:
    f1.write(json.dumps(cb_ovo, indent=4))
    f2.write(json.dumps(mv_ovo, indent=4))
    f3.write(json.dumps(cb_urls, indent=4))
    f4.write(json.dumps(mv_urls, indent=4))
