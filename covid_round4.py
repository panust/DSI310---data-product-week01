import requests
import json
import pandas as pd

url = "https://covid19.ddc.moph.go.th/api/Cases/timeline-cases-by-provinces"
response = requests.get(url=url)
print(response.json())

with open('covid_round4.json', 'w',encoding='utf8') as outfile:
    json.dump(response.json()['data'], outfile, ensure_ascii=False,indent=4)

df = pd.json_normalize(response.json()['data']) 
df.to_csv('covid_round4.csv',index=None,encoding='utf-8-sig')