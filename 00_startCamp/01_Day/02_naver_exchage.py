import requests
from bs4 import BeautifulSoup
url='https://finance.naver.com/marketindex/'
html=requests.get(url).text
soup=BeautifulSoup(html, 'html.parser')
swp=soup.select_one('#exchangeList > li.on > a.head.usd > div > span.value')
print(f'오늘의 달러 환율은 {swp.text}입니다.')
