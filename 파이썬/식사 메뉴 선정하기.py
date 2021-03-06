import random as r
import time

lunch = ['피자', '파스타', '쌀국수', '치킨', '김치찌개']

while True:
    print(lunch)
    menu = input('추가할 메뉴를 입력해주세요(q 입력시 중단): ' )
    if menu == 'q':
        break
    else:
        lunch.append(menu)

print()
print(lunch)
print()
set_lunch = set(lunch)   # 인자가 많아질 때를 대비해서 중복을 제거

while True:
    print(set_lunch)
    delete = input('삭제할 메뉴를 입력해주세요(q 입력시 중단): ' )
    if delete == 'q':
        break
    else:
        set_lunch -= set([delete])

print()
print(set_lunch, '중에서 선택합니다.')
print()

for i in range(5, 0, -1):
    print(i)
    time.sleep(1) # time 모듈로 시간 지연 주기

print()
print(r.choice(list(set_lunch))) # set은 에러가 뜨기 때문에 list로 바꿔줘야함
