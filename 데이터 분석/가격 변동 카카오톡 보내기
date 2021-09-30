import requests as r
from bs4 import BeautifulSoup
import json
import time


kakao_token = 'token'
def sendtoKakao(text):
    header = {'Authorization' : 'Bearer ' + kakao_token}
    url = 'https://kapi.kakao.com/v2/api/talk/memo/default/send'
    post = {
        "object_type": "text",
        "text": text,
        "link": {
            "web_url": "https://developers.kakao.com",
            "mobile_web_url": "https://developers.kakao.com"
        }
    }
    
    data = {'template_object':json.dumps(post)}
    return r.post(url, headers = header, data=data)

def procreate():
    url = 'https://search.shopping.naver.com/search/all?bt=0&frm=NVSCPRO&origQuery=%ED%94%84%EB%A1%9C%ED%81%AC%EB%A6%AC%EC%97%90%EC%9D%B4%ED%8A%B8%20%EB%A6%AC%EB%94%A4%EC%BD%94%EB%93%9C&pagingIndex=1&pagingSize=40&productSet=total&query=%ED%94%84%EB%A1%9C%ED%81%AC%EB%A6%AC%EC%97%90%EC%9D%B4%ED%8A%B8%20%EB%A6%AC%EB%94%A4%EC%BD%94%EB%93%9C&sort=price_asc&timestamp=&viewType=list'
    web = r.get(url)
    soup = BeautifulSoup(web.text, 'html.parser')
    
    items = soup.select('.basicList_inner__eY_mq')

    result = {}
    for item in items:
        price = int(item.select('.price_num__2WUXn')[0].text.strip('원').replace(',',''))
        mall = item.select('.basicList_mall__sbVax')[0].text
        link = 'https://smartstore.naver.com/appmarket/products/5002690247?NaPm=ct%3Dkk3xd0r4%7Cci%3Dd6c7c3c24aa8676ccd0998ec447fc69c0713c041%7Ctr%3Dslsl%7Csn%3D1172803%7Chk%3D9538ee035ae5545b92fac860090d5170f23c3131'

        if mall == '도깨비 앱마켓' and price < 6000 :
            text = f'{mall} : {price}원\n{link}'
            a = sendtoKakao(text)
            print(a.text)
            
if __name__ == '__main__':
    while True:
        procreate()
        time.sleep(60*5)
