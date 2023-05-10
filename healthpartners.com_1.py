import requests
import time
import json

import glob

output = {}

# print(len(glob.glob("hosss_*.json")))
#
# breakpoint()

"""

Python
есть файлы с такими именами: hosss_01.json, hosss_02.json, hosss_03.json и так до файла с именем hosss_16.json
все файлы с одинаковой структурой
нужно прочитать их все
в каждом файле найти все значения с ключами "zip_code", "state", "formattedAddress" и "city"
создать json-файл с такой структурой:
{
  "54005-8581": {
	"city": "Clear Lake",
	"state": "WI",
	"formattedAddress": "357 3rd Ave, Clear Lake, WI 54005-8581"
  }
}

"""

for filename in glob.glob("hosss_*.json"):
    with open(filename, "r") as f:
        data = json.load(f)
        # print(data)

        for item in data["results"]:
            print(item["address"])
            if "zip" in item:
                print(item["zip"])
                breakpoint()

            # if "zip" in item and "state" in item and "formattedAddress" in item and "city" in item:
            #     zip_code = item["zip"]
            #     output[zip_code] = {
            #         "city": item["city"],
            #         "state": item["state"],
            #         "formattedAddress": item["formattedAddress"]
            #     }

with open("output.json", "w") as f:
    json.dump(output, f)

breakpoint()

# with open('_h.json', 'r', encoding='utf-8') as set_:
#     data_ = json.load(set_)
#
#
# for i in data_['results']:
#     print(i['name']['fullName'])
#     print(i['name']['cred'])
#     breakpoint()

# with open('hos.json', 'r', encoding='utf-8') as set_:
#     data_ = json.load(set_)
#
# print(data_['totalCount'])
#
# # for i in data_['results']:
# #     print(i['address']['zip'])
#
# breakpoint()

# pip install free-proxy
from fp.fp import FreeProxy

cookies = {}
headers = {
    'Accept': '*/*',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7,uk;q=0.6,vi;q=0.5,pt;q=0.4,ka;q=0.3',
    'Connection': 'keep-alive',
    'Content-Type': 'application/json',
    # 'Cookie': '2f7ac93853db514ae678c2c52680a2cb=a8854b91450a7bb7e2c129bef0a97782; hp_myCluster_pi=prd4; 9f87fa6918532dc2d5b2f523687a55b7=152f0cdbb6adc9eb0698f377ec81393e; myClusterPrdOcp4=prd4; TS01677f99=018aeed6cf92c19c72c972115aea9a22dea9652f1bd5a9c02eb9be84782031a45c787db9ddf73705cae59789d6783e887257ab4d6340e915f56cea5afef3cac4d10f9bdb165d758568cfa908d5f9c30caf4b1b4add; 4ad6baf7d6c5f05efa391d0b313bfbf4=20aef68cf205149eda04bc4c20c510a9; _dy_csc_ses=t; _dy_c_exps=; _dycnst=dg; BIGipServerpool_prdaem_SSL=1038097580.47873.0000; _dyid=-8993688213657061794; _dyjsession=d748232e1291ab4184166818093ab5be; AMCVS_2DA334FA53DB01680A490D44%40AdobeOrg=1; s_ecid=MCMID%7C88750491493707363104032278815645405238; s_cc=true; _dyid_server=-8993688213657061794; _dy_c_att_exps=; 8a4a93024a4cb0e0f1ea632a28fe802a=4b04ef9c1aeeef5c1be660a4d2631f70; _gcl_au=1.1.405161846.1683650424; s_sq=%5B%5BB%5D%5D; _fc_def_loc=Clear+Lake%2C+Wisconsin+54005%2C+United+States; _dyfs=1683651855061; _dycst=dk.w.c.ws.; __e_inc=1; _uetsid=1f1b64d0ef5b11ed90a57560eb928633; _uetvid=32c85520ee8811ed95e0c3dcd0e52663; 890624e1e46c118c81d01812d5339325=35a62391a3da9a1d65832f8cf302c8ce; _dy_ses_load_seq=14310%3A1683748692831; dy_fs_page=www.healthpartners.com%2Fcare%2Ffind%2Flocations; _dy_lu_ses=d748232e1291ab4184166818093ab5be%3A1683748695061; _dy_geo=TR.EU.TR_.TR__; _dy_df_geo=Turkey..; _dy_toffset=-1; AMCV_2DA334FA53DB01680A490D44%40AdobeOrg=179643557%7CMCIDTS%7C19487%7CMCMID%7C88750491493707363104032278815645405238%7CMCAAMLH-1684353526%7C6%7CMCAAMB-1684353526%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1683755926s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0; gpv_pn=%2Fcare%2Ffind%2Flocations%2F; s_ptc=0.00%5E%5E0.00%5E%5E0.00%5E%5E0.00%5E%5E2.29%5E%5E0.11%5E%5E17.55%5E%5E0.04%5E%5E19.91; MyChart_Session=qo4x4wsackgn52ogjfzed2wd; __RequestVerificationToken_L3BhdGllbnRteWNoYXJ00=Lq8TbtdmIo55HyiKRxroFUbSQubSiEe8Sd8WtDOqPNsU4AD3fIrK-qYt_zPiV2gseZjkkHAAcrH3biOv1Oi_BvQ3xOs1; MyChartLocale=en-US; MyChartPersistence=870361610.47873.0000; TS015fa82c=018aeed6cfb546b8215a83323daadfa41b13f83ec0e52f4fb17992c466bca6a4039217f04a88bc78a1903f6b9f5e5e7b7139186b40fa750377b1f7b0a5e303d92cb2ead27aebda2eddce2efd2860a2d230d08a452b1e6ac2dc386fcd9da442f7dfdd87cec5563ab5c51db1c4928cfd98ec7d5ac1e15f7db90035041ba2bf18c6b2cb92da4b7ffb2c341912790352f9176e7b67999d8f71b0c8d6a81aee5babaf798fc4638babdd9cde36b4434d5ae6390fd526c8cc; _dy_soct=634627.1225862.1683746637*637375.1230919.1683748692*766749.1457106.1683750918*769020.1460825.1683750918; s_ppvl=%2Fcare%2Ffind%2Fdoctors%2F%2C32%2C32%2C1437%2C1920%2C937%2C1920%2C1080%2C1%2CP; s_ppv=%2Fcare%2Ffind%2Flocations%2F%2C94%2C11%2C8367%2C1002%2C937%2C1920%2C1080%2C1%2CP',
    'Origin': 'https://www.healthpartners.com',
    'Referer': 'https://www.healthpartners.com/care/find/locations?where=Clear+Lake%2C+Wisconsin+54005%2C+United+States&latLong=45.251907%2C-92.2713&page=14',
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
            print(cookies_)
            ts01677f99_ = cookies_.get('TS01677f99')
            ts015fa82c_ = cookies_.get('TS015fa82c')

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
                'AMCVS_2DA334FA53DB01680A490D44%40AdobeOrg': '1',
                's_ecid': 'MCMID%7C88750491493707363104032278815645405238',
                's_cc': 'true',
                '_dyid_server': '-8993688213657061794',
                '_dy_c_att_exps': '',
                '8a4a93024a4cb0e0f1ea632a28fe802a': '4b04ef9c1aeeef5c1be660a4d2631f70',
                '_gcl_au': '1.1.405161846.1683650424',
                's_sq': '%5B%5BB%5D%5D',
                '_fc_def_loc': 'Clear+Lake%2C+Wisconsin+54005%2C+United+States',
                '_dyfs': '1683651855061',
                '_dycst': 'dk.w.c.ws.',
                '__e_inc': '1',
                '_uetsid': '1f1b64d0ef5b11ed90a57560eb928633',
                '_uetvid': '32c85520ee8811ed95e0c3dcd0e52663',
                '890624e1e46c118c81d01812d5339325': '35a62391a3da9a1d65832f8cf302c8ce',
                '_dy_ses_load_seq': '14310%3A1683748692831',
                'dy_fs_page': 'www.healthpartners.com%2Fcare%2Ffind%2Flocations',
                '_dy_lu_ses': 'd748232e1291ab4184166818093ab5be%3A1683748695061',
                '_dy_geo': 'TR.EU.TR_.TR__',
                '_dy_df_geo': 'Turkey..',
                '_dy_toffset': '-1',
                'AMCV_2DA334FA53DB01680A490D44%40AdobeOrg': '179643557%7CMCIDTS%7C19487%7CMCMID%7C88750491493707363104032278815645405238%7CMCAAMLH-1684353526%7C6%7CMCAAMB-1684353526%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1683755926s%7CNONE%7CMCAID%7CNONE%7CvVersion%7C5.5.0',
                'gpv_pn': '%2Fcare%2Ffind%2Flocations%2F',
                's_ptc': '0.00%5E%5E0.00%5E%5E0.00%5E%5E0.00%5E%5E2.29%5E%5E0.11%5E%5E17.55%5E%5E0.04%5E%5E19.91',
                'MyChart_Session': 'qo4x4wsackgn52ogjfzed2wd',
                '__RequestVerificationToken_L3BhdGllbnRteWNoYXJ00': 'Lq8TbtdmIo55HyiKRxroFUbSQubSiEe8Sd8WtDOqPNsU4AD3fIrK-qYt_zPiV2gseZjkkHAAcrH3biOv1Oi_BvQ3xOs1',
                'MyChartLocale': 'en-US',
                'MyChartPersistence': '870361610.47873.0000',
                'TS015fa82c': f'{ts015fa82c_}',
                '_dy_soct': '634627.1225862.1683746637*637375.1230919.1683748692*766749.1457106.1683750918*769020.1460825.1683750918',
                's_ppvl': '%2Fcare%2Ffind%2Fdoctors%2F%2C32%2C32%2C1437%2C1920%2C937%2C1920%2C1080%2C1%2CP',
                's_ppv': '%2Fcare%2Ffind%2Flocations%2F%2C94%2C11%2C8367%2C1002%2C937%2C1920%2C1080%2C1%2CP',
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

# json_data = {
#     'size': 20,
#     'offset': 0,
#     'sort': 'dist',
#     'seed': 'd748232e1291ab4184166818093ab5be',
#     'distance': '75',
#     'lat': lat,
#     'lng': lng,
#     'where': where_,
#     'locations': [],
#     'isMinisite': False,
# }

json_data = {
    'offset': 0,
    'size': 20,
    'brand': [],
    'sort': None,
    'specialty': [],
    'types': [],
    'minisiteExpertises': [],
    'lat': 45.251907,
    'lng': -92.2713,
    'ids': [],
    'where': 'Clear Lake, Wisconsin 54005, United States',
    'miniSiteTag': '',
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

print(data_)

offset = 0
# offset = 2340
totalCount = data_['totalCount']
print(f"totalCount: {totalCount} <<<<<<<<<<<<<<<<<<\n")

arr_p = []

cou_ = 0

while offset < totalCount:
    time.sleep(1)
    cou_ += 1

    current_page = offset // 20 + 1

    # json_data = {
    #     'size': 20,
    #     'offset': offset,
    #     'sort': 'dist',
    #     'seed': 'd748232e1291ab4184166818093ab5be',
    #     'distance': '75',
    #     'lat': lat,
    #     'lng': lng,
    #     'where': where_,
    #     'locations': [],
    #     'isMinisite': False,
    # }

    json_data = {
        'offset': offset,
        'size': 20,
        'brand': [],
        'sort': None,
        'specialty': [],
        'types': [],
        'minisiteExpertises': [],
        'lat': 45.251907,
        'lng': -92.2713,
        'ids': [],
        'where': 'Clear Lake, Wisconsin 54005, United States',
        'miniSiteTag': '',
    }

    while True:
        try:
            response = requests.post(
                'https://www.healthpartners.com/care/find/api/v1/locationPages',
                cookies=cookies,
                headers=headers,
                json=json_data,
                proxies=proxy_servers,
            )

            break
        except:
            find_proxy()

    data_ = json.loads(response.text)

    # for i in data_['results']:
    #     arr_p.append(
    #         {
    #             "carrier": "HealthPartners",
    #             "carrierId": "HPY000043C",
    #             "id": i['id'],
    #             "npi": i['npi'],
    #             "type": i['type'],
    #             "firstName": i['name']['first'],
    #             "middleName": i['name']['middle'],
    #             "lastName": i['name']['last'],
    #             "fullName": i['name']['fullName'],
    #             "cred": i['name']['cred'],
    #             "genderName": i['genderName']
    #         }
    #     )

    print(f"Current page: {current_page}, offset = {offset}    response: {response}")
    offset += 20

    with open(f'hosss!_{cou_}.json', 'w+', encoding='utf-8') as file:
        json.dump(data_, file, indent=4, ensure_ascii=False)

# https://www.healthpartners.com/care/find/location/primary-care-clinics/amery-hospital-and-clinic/clear-lake/
# https://www.healthpartners.com/care/find/doctors/?where=Clear+Lake%2C+Wisconsin+54005%2C+United+States&latLong=45.251907%2C-92.2713&sort=dist&page=2&dist=75
# https://www.healthpartners.com/care/find/doctor/199990/
