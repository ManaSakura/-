import json

import requests
from craw_model import crawmodel

AQI_URL = 'https://aqicn.org/city/beijing/'
AQI_savejson_path = 'beijing_AQI.json'
def crwa_BJ_AQI(AQI_URL,AQI_savejson_path):
    """
        parm AQI_URL: AQI的url
        parm AQI_savejson_path: 爬取AQI数据的保存路径，格式为json
    """
    model=crawmodel(url=AQI_URL, ip='114.67.94.46:8080')
    model.get_html_element()
    # print(model.html_element)
    html_bytes = model.html_bytes
    html_element = model.html_element
    # print(html_element)
    min_pm25 = html_element.xpath('//*[@id="min_pm25"]/text()')
    # min_pm25_node = etree.tostring(html_element.xpath('//*[@id="min_pm25"]')[0]) #获取节点全部文本
    max_pm25 = html_element.xpath('//*[@id="max_pm25"]/text()')
    min_pm10 = html_element.xpath('//*[@id="min_pm10"]/text()')
    max_pm10 = html_element.xpath('//*[@id="max_pm10"]/text()')
    min_humidity = html_element.xpath('//*[@id="min_h"]/text()')
    max_humidity = html_element.xpath('//*[@id="max_h"]/text()')
    min_pressure = html_element.xpath('//*[@id="min_p"]/text()')
    max_pressure = html_element.xpath('//*[@id="max_p"]/text()')
    city = html_element.xpath('//*[@id="aqiwgttitle1"]/b/text()')
    air_quality = html_element.xpath('//*[@id="aqiwgtinfo"]/text()')
    AQI = {
        'city': city,
        'air_quality': air_quality,
        'min_pm25': min_pm25,
        'max_pm25': max_pm25,
        'min_pm10': min_pm10,
        'max_pm10': max_pm10,
        'min_humidity': min_humidity,
        'max_humidity': max_humidity,
        'min_pressure': min_pressure,
        'max_pressure': max_pressure
    }
    with open(AQI_savejson_path,'w') as f:
        json.dump(AQI,f)
    print(AQI)
    # eg.write_html('1.html')
    # print('读写{}中element元素完成'.format(eg.url))
crwa_BJ_AQI(AQI_URL, AQI_savejson_path)

