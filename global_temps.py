import json
import urllib.request

json_data_source = 'https://www.ncei.noaa.gov/access/monitoring/climate-at-a-glance/global/time-series/globe/land_ocean/1/10/1880-2022.json'

with urllib.request.urlopen(json_data_source) as json_stream:
    data = json_stream.read().decode('utf-8')
# with open(json_data_source, encoding='utf-8') as data:
    anomalies = json.loads(data)

print(anomalies['description'])

for year, value in anomalies['data'].items():
    year, value = int(year), float(value)
    print(f'{year} ...{value:6.2f}')
print('*' * 80)

# print(anomalies['citation'])

