import urllib
import requests
from bs4 import BeautifulSoup as bs
import pprint

header = {
    'Host': 'edu.ssafy.com',
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/76.0.3809.132 Safari/537.36',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3',
    'Referer': 'http://edu.ssafy.com/edu/lectureroom/openlearning/openLearningView.do',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7',
    'Cookie': 'WMONID=PT-_EdQXBmn; JSESSIONID_HAKSAF=mGEvu3Nd-44Og6PeYT3qYRPZofp4csTdySClPssdOwUCJRUPBI33!511610662!-935964269!1568463876957; toast.pagefit-mode=view-all'
}
a = 'http://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2019071218255448800'
url = a + '/project.json?timestamp=1568465761988'
res = requests.get(url, headers=header)
# pprint.pprint(res.json().get('pages'))
t = 1
for i in range(len(res.json().get('pages'))):
    url2 = a + '/assets/' + res.json().get('pages')[i]['background']['url'][12:]
    print(url2)
    with open('B반 SW 문제해결기본/{}'.format(url2.split('/')[-1]), 'wb') as f:
        image = requests.get(url2, stream=True, headers=header).content
        f.write(image)
        t += 1