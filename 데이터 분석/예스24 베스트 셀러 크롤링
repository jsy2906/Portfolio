from selenium import webdriver
from bs4 import BeautifulSoup
import time
import pandas as pd

# 브라우저 열기
browser = webdriver.Chrome('C:/chromedriver.exe')
url = 'http://www.yes24.com/24/category/bestseller'
browser.get(url)
time.sleep(2)

# 페이지 정보 가져오기
html = browser.page_source
soup = BeautifulSoup(html,'html.parser')

# 원하는 정보 찾기
book_list = soup.select('ol > li')
results = []
for book in book_list:
    title = book.select('a')[2].text
    price = book.select('strong')[0].text
    
    writer = book.select('.aupu')[0].text
    author = writer.split('|')[0].strip()
    publisher = writer.split('|')[1].strip()
    
    try:   #평가점수가 없는 경우 index에러 발생  ->  에러처리 해주기
        rating = book.select('p')[6].select('img')
        star_content = 0
        for i in rating[:5]:
            if i['src'][-6:-4] == 'On':
                star_content += 1

        star_edit = 0
        for i in rating[5:]:
            if i['src'][-6:-4] == 'On':
                star_edit += 1
    except:
        star_content = 'X'
        star_edit = 'X'

    data = [title,author,publisher,price,star_content,star_edit]
    results.append(data)

browser.close()

#  데이터 저장하기   
df = pd.DataFrame(results)
df.columns = ['제목','저자','출판사','가격','내용 평가','편집/구성 평가']
df.index += 1
df.to_excel('./예스24 베스트셀러.xlsx')
