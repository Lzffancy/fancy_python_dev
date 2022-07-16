import time

print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1652154596)))
print(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(1653557034)))

import requests
import re
import json
import csv

f = open('招聘.csv', mode='a', encoding='utf-8', newline='')
csv_writer = csv.DictWriter(f, fieldnames=[
    '岗位名字',
    '岗位薪资',
    'base地',
    '福利',
    '经验要求',
    '学历',
    '发布日期',
    '公司所属行业',
    '公司性质',
    '详情页',
])
csv_writer.writeheader()
url = 'https://search.51job.com/list/000000,000000,0000,00,9,99,%25E5%258C%2597%25E4%25BA%25AC%25E8%258A%25AF%25E5%2590%258C,2,1.html'
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53'
}
response = requests.get(url=url, headers=headers)
print(response.text)
html_data = re.findall('window.__SEARCH_RESULT__ = (.*?)</script>', response.text)[0]
json_data = json.loads(html_data)
print(json_data)


for index in json_data['engine_jds']:
    dit = {
        '岗位名字': index['job_name'],
        '岗位薪资': index['providesalary_text'],
        '工作地点': index['workarea_text'],
        '福利': index['jobwelf'],
        '经验要求': index['attribute_text'][1],
        '学历': index['issuedate'][2],
        '发布日期': index['issuedate'],
        '公司所属行业': index['companyind_text'],
        '公司性质': index['companytype_text'],
        '详情页': index['job_href'],
    }

    csv_writer.writerow(dit)
    print(dit)
