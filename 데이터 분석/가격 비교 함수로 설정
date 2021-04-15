from selenium import webdriver
from bs4 import BeautifulSoup
import time

browser = webdriver.Chrome('c:/chromedriver.exe')
url = 'https://search.shopping.naver.com/catalog/14276294183?nv_mid=14276294183&cat_id=50002543&frm=NVSHATC&query=%EC%83%A4%EC%98%A4%EB%AF%B8+%EA%B3%B5%EA%B8%B0%EC%B2%AD%EC%A0%95%EA%B8%B0&NaPm=ct%3Djrwtohn4%7Cci%3D529864238905ac8f1fe6d6f5cbc20e122264daf2%7Ctr%3Dslsl%7Csn%3D95694%7Chk%3Dfbb1fb4639787be4e184fed57f57760b1057a501'
browser.get(url)
time.sleep(2)

def item_sell_comp(x):
    html = browser.page_source
    soup = BeautifulSoup(html, 'html.parser')

    items = soup.select('.productList_list_seller___NsJk > li')
    result=[]
    for item in items:
        title = item.select('a.productList_title__uCZ0P')[0].text
        try:
            mall = item.select('img')[0]['alt']
        except:
            mall = item.select('a.productList_mall_link__1-Q4X > span')[0].text
        price = item.select('a > span > em')[0].text
        deli = item.select('.productList_delivery__2BusJ')[0].text
        if deli == '무료배송':
            deli = '0원'
        deli = deli[:-1]
        link = item.select('a.productList_title__uCZ0P')[0]['href']

        data = [title, mall, price, deli, link]
        result.append(data)
    return result
