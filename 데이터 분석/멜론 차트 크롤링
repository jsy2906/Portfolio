from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

browser = webdriver.Chrome('C:/chromedriver.exe')
url = 'https://www.melon.com/chart/index.htm'
browser.get(url)
time.sleep(2)

html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

ranking_list = soup.select('table > tbody > tr')
results = []

for ranking in ranking_list:
    title = ranking.select('div.ellipsis.rank01> span > a')[0].text
    album = ranking.select('.ellipsis.rank03 > a')[0].text
    like = ranking.select('span.cnt')[0].text.replace('총건수','').strip()
    singers = ranking.select('div.ellipsis.rank02 > a')
    singer = ''
    if len(singers)>1:
        for i in singers:
            element = i.text
            singer += (element + '/')
        singer = singer[:-1]
    else:
        singer = singers[0].text
    
    
    data = [title,singer,album,like]
    results.append(data)
print(results[0])

df = pd.DataFrame(results)
df.columns=['제목','가수','앨범','좋아요수']
df.to_excel('./멜론차트.xlsx',index = False)
