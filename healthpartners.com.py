import requests
import time
import json

# with open('_h.json', 'r', encoding='utf-8') as set_:
#     data_ = json.load(set_)
#
#
# for i in data_['results']:
#     print(i['name']['fullName'])
#     print(i['name']['cred'])
#     breakpoint()

with open('hos.json', 'r', encoding='utf-8') as set_:
    data_ = json.load(set_)

print(len(data_['results']))

for i in data_['results']:
    print(i['address']['zip'])

    breakpoint()

# pip install free-proxy
from fp.fp import FreeProxy

cookies = {}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': '2f7ac93853db514ae678c2c52680a2cb=a8854b91450a7bb7e2c129bef0a97782; hp_myCluster_pi=prd4; 9f87fa6918532dc2d5b2f523687a55b7=152f0cdbb6adc9eb0698f377ec81393e; myClusterPrdOcp4=prd4; TS01677f99=018aeed6cf92c19c72c972115aea9a22dea9652f1bd5a9c02eb9be84782031a45c787db9ddf73705cae59789d6783e887257ab4d6340e915f56cea5afef3cac4d10f9bdb165d758568cfa908d5f9c30caf4b1b4add; 4ad6baf7d6c5f05efa391d0b313bfbf4=20aef68cf205149eda04bc4c20c510a9; _dy_csc_ses=t; _dy_c_exps=; _dycnst=dg; BIGipServerpool_prdaem_SSL=1038097580.47873.0000; _dyid=-8993688213657061794; _dyjsession=d748232e1291ab4184166818093ab5be; dy_fs_page=www.healthpartners.com%2Fcare%2Ffind%2Fdoctors; _dy_geo=US.NA.US_NY.US_NY_New%20York; _dy_df_geo=United%20States.New%20York.New%20York; AMCVS_2DA334FA53DB01680A490D44%40AdobeOrg=1; s_ecid=MCMID%7C88750491493707363104032278815645405238; AMCV_2DA334FA53DB01680A490D44%40AdobeOrg=179643557%7CMCIDTS%7C19487%7CMCMID%7C88750491493707363104032278815645405238%7CMCAAMLH-1684254945%7C7%7CMCAAMB-1684254945%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1683657346s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; s_cc=true; _dyid_server=-8993688213657061794; _dy_c_att_exps=; 8a4a93024a4cb0e0f1ea632a28fe802a=4b04ef9c1aeeef5c1be660a4d2631f70; _dy_toffset=1; s_ptc=0.00%5E%5E0.00%5E%5E0.00%5E%5E0.86%5E%5E1.59%5E%5E0.97%5E%5E14.24%5E%5E0.02%5E%5E16.73; _gcl_au=1.1.405161846.1683650424; _uetsid=32c7fb70ee8811edbd7f013069da8ef2; _uetvid=32c85520ee8811ed95e0c3dcd0e52663; s_sq=%5B%5BB%5D%5D; gpv_pn=%2Fcare%2Ffind%2Fdoctors%2F; _fc_def_loc=Clear+Lake%2C+Wisconsin+54005%2C+United+States; s_ppvl=%2Fcare%2Ffind%2Flocation%2Fprimary-care-clinics%2Famery-hospital-and-clinic%2Fclear-lake%2F%2C21%2C21%2C937%2C1920%2C937%2C1920%2C1080%2C1%2CP; s_ppv=%2Fcare%2Ffind%2Fdoctors%2F%2C45%2C45%2C2109%2C1002%2C937%2C1920%2C1080%2C1%2CP; TS015fa82c=018aeed6cfa41d46026c4ef8ab13625b789382d751376eb91f138252c2c14b35189de0e9e67b0ec340543645459faf82e61a4bb0e61519a7a5dbcaa0feac48a3ef43f9b413d0cf43d29a7df941f8f0ead46fd3fe8b0bfe8229654544c1a2a75fed687e660c672c9a42effc4163a178d1489d9a35db2db367759d6e16de00c63970af52d43b46250daf92a1e079befaa5768a63f59241a34441a6dbf567251f84d8d079efb8; _dy_ses_load_seq=36507%3A1683651854284; _dy_soct=634627.1225862.1683651854*637375.1230919.1683650142*766749.1457106.1683651854*769020.1460825.1683651854; _dyfs=1683651855061; _dy_lu_ses=d748232e1291ab4184166818093ab5be%3A1683651855062; _dycst=dk.w.c.ss.',
    'Origin': 'https://www.healthpartners.com',
    'Referer': 'https://www.healthpartners.com/care/find/doctors/?where=Clear+Lake%2C+Wisconsin+54005%2C+United+States&latLong=45.251907%2C-92.2713&sort=dist&page=1&dist=75',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36',
    'sec-ch-ua': '"Chromium";v="112", "Google Chrome";v="112", "Not:A-Brand";v="99"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

proxy_servers = {}


# zip_code = 54005
def zip_(zip_code):
    rsp_ = requests.get(f"http://api.zippopotam.us/us/{zip_code}")
    data = rsp_.json()

    lat = data['places'][0]['latitude']
    lng = data['places'][0]['longitude']
    city = data['places'][0]['place name']
    state = data['places'][0]['state']
    where_ = f'{city}, {state} {zip_code}, United States'

    return lat, lng, where_


def find_proxy():
    global cookies
    global proxy_servers

    cou_ = 0

    proxy = FreeProxy(rand=True).get()
    # print(f'PROXY: {proxy}')
    proxy_servers = {
        'http': f'{proxy}',
        'https': f'{proxy}',
    }

    while True:
        time.sleep(1)
        status_code = ''

        try:
            cou_ += 1
            print(f'{cou_} Try...')

            response = requests.get('https://www.healthpartners.com/', proxies=proxy_servers, timeout=5)
            status_code = response.status_code

            print(f'...{status_code}')
        except:
            print(f'...NO!')
            response = 'QWERTY'
            proxy = FreeProxy(rand=True).get()
            print(f'NEW PROXY: {proxy}')
            proxy_servers = {
                'http': f'{proxy}',
                'https': f'{proxy}',
            }

        if status_code == 200:
            print(f'=== 200 ===   PROXY: {proxy}')

            cookies_ = response.cookies
            ts01677f99_ = cookies_.get('TS01677f99')

            print(f'!!!!!!!!!!! \n{ts01677f99_}\n!!!!!!!!!!!')

            cookies = {
                '2f7ac93853db514ae678c2c52680a2cb': 'a8854b91450a7bb7e2c129bef0a97782',
                'hp_myCluster_pi': 'prd4',
                '9f87fa6918532dc2d5b2f523687a55b7': '152f0cdbb6adc9eb0698f377ec81393e',
                'myClusterPrdOcp4': 'prd4',
                'TS01677f99': f'{ts01677f99_}',
                '4ad6baf7d6c5f05efa391d0b313bfbf4': '20aef68cf205149eda04bc4c20c510a9',
                '_dy_csc_ses': 't',
                '_dy_c_exps': '',
                '_dycnst': 'dg',
                'BIGipServerpool_prdaem_SSL': '1038097580.47873.0000',
                '_dyid': '-8993688213657061794',
                '_dyjsession': 'd748232e1291ab4184166818093ab5be',
                'dy_fs_page': 'www.healthpartners.com%2Fcare%2Ffind%2Fdoctors',
                '_dy_geo': 'US.NA.US_NY.US_NY_New%20York',
                '_dy_df_geo': 'United%20States.New%20York.New%20York',
                'AMCVS_2DA334FA53DB01680A490D44%40AdobeOrg': '1',
                's_ecid': 'MCMID%7C88750491493707363104032278815645405238',
                'AMCV_2DA334FA53DB01680A490D44%40AdobeOrg': '179643557%7CMCIDTS%7C19487%7CMCMID%7C88750491493707363104032278815645405238%7CMCAAMLH-1684254945%7C7%7CMCAAMB-1684254945%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1683657346s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
                's_cc': 'true',
                '_dyid_server': '-8993688213657061794',
                '_dy_c_att_exps': '',
                '8a4a93024a4cb0e0f1ea632a28fe802a': '4b04ef9c1aeeef5c1be660a4d2631f70',
                '_dy_toffset': '1',
                's_ptc': '0.00%5E%5E0.00%5E%5E0.00%5E%5E0.86%5E%5E1.59%5E%5E0.97%5E%5E14.24%5E%5E0.02%5E%5E16.73',
                '_gcl_au': '1.1.405161846.1683650424',
                '_uetsid': '32c7fb70ee8811edbd7f013069da8ef2',
                '_uetvid': '32c85520ee8811ed95e0c3dcd0e52663',
                's_sq': '%5B%5BB%5D%5D',
                'gpv_pn': '%2Fcare%2Ffind%2Fdoctors%2F',
                '_fc_def_loc': 'Clear+Lake%2C+Wisconsin+54005%2C+United+States',
                's_ppvl': '%2Fcare%2Ffind%2Flocation%2Fprimary-care-clinics%2Famery-hospital-and-clinic%2Fclear-lake%2F%2C21%2C21%2C937%2C1920%2C937%2C1920%2C1080%2C1%2CP',
                's_ppv': '%2Fcare%2Ffind%2Fdoctors%2F%2C45%2C45%2C2109%2C1002%2C937%2C1920%2C1080%2C1%2CP',
                'TS015fa82c': '018aeed6cfa41d46026c4ef8ab13625b789382d751376eb91f138252c2c14b35189de0e9e67b0ec340543645459faf82e61a4bb0e61519a7a5dbcaa0feac48a3ef43f9b413d0cf43d29a7df941f8f0ead46fd3fe8b0bfe8229654544c1a2a75fed687e660c672c9a42effc4163a178d1489d9a35db2db367759d6e16de00c63970af52d43b46250daf92a1e079befaa5768a63f59241a34441a6dbf567251f84d8d079efb8',
                '_dy_ses_load_seq': '36507%3A1683651854284',
                '_dy_soct': '634627.1225862.1683651854*637375.1230919.1683650142*766749.1457106.1683651854*769020.1460825.1683651854',
                '_dyfs': '1683651855061',
                '_dy_lu_ses': 'd748232e1291ab4184166818093ab5be%3A1683651855062',
                '_dycst': 'dk.w.c.ss.',
            }
            break


find_proxy()

# proxy = '5.75.227.149:8080'
#
# proxy_servers = {
#     'http': f'http://{proxy}',
#     'https': f'https://{proxy}',
# }

lat, lng, where_ = zip_(54005)

json_data = {
    'size': 20,
    'offset': 0,
    'sort': 'dist',
    'seed': 'd748232e1291ab4184166818093ab5be',
    'distance': '75',
    'lat': lat,
    'lng': lng,
    'where': where_,
    'locations': [],
    'isMinisite': False,
}

response = requests.post(
    'https://www.healthpartners.com/care/find/api/v1/practitionersPages/',
    cookies=cookies,
    headers=headers,
    json=json_data,
    proxies=proxy_servers,
    timeout=5,
)

data_ = json.loads(response.text)

offset = 0
# offset = 2340
totalCount = data_['totalCount']
print(f"totalCount: {totalCount} <<<<<<<<<<<<<<<<<<\n")

arr_p = []

while offset < totalCount:
    time.sleep(1)

    current_page = offset // 20 + 1

    json_data = {
        'size': 20,
        'offset': offset,
        'sort': 'dist',
        'seed': 'd748232e1291ab4184166818093ab5be',
        'distance': '75',
        'lat': lat,
        'lng': lng,
        'where': where_,
        'locations': [],
        'isMinisite': False,
    }

    while True:
        try:
            response = requests.post(
                'https://www.healthpartners.com/care/find/api/v1/practitionersPages/',
                cookies=cookies,
                headers=headers,
                json=json_data,
                proxies=proxy_servers,
            )
            break
        except:
            find_proxy()

    data_ = json.loads(response.text)

    for i in data_['results']:
        arr_p.append(
            {
                "carrier": "HealthPartners",
                "carrierId": "HPY000043C",
                "id": i['id'],
                "npi": i['npi'],
                "type": i['type'],
                "firstName": i['name']['first'],
                "middleName": i['name']['middle'],
                "lastName": i['name']['last'],
                "fullName": i['name']['fullName'],
                "cred": i['name']['cred'],
                "genderName": i['genderName']
            }
        )

    print(f"Current page: {current_page}, offset = {offset}    response: {response}")
    offset += 20

with open('_h.json', 'w+', encoding='utf-8') as file:
    json.dump(arr_p, file, indent=4, ensure_ascii=False)

# https://www.healthpartners.com/care/find/location/primary-care-clinics/amery-hospital-and-clinic/clear-lake/
# https://www.healthpartners.com/care/find/doctors/?where=Clear+Lake%2C+Wisconsin+54005%2C+United+States&latLong=45.251907%2C-92.2713&sort=dist&page=2&dist=75
# https://www.healthpartners.com/care/find/doctor/199990/
