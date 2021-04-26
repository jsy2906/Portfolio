def calc(a, b, c):
    if c == 1:
        result = a * b
        
    elif c == 2:
        result = a - b
        
    elif c == 3:
        result = a * b
        
    elif c == 4:
        result = a / b
        
    elif c == 5:
        result = a % b

    return result

print('=' * 30)
print('1. 더하기\n2. 빼기\n3. 곱하기\n4. 나누기\n5. 나머지 구하기\n6. 나가기')
print('=' * 30)


i = 0
while True:
    cal = int(input('원하는 연산자를 입력하세요: '))
    
    if cal <= 5:
        num1 = int(input('첫번째 숫자를 입력하세요: '))
        num2 = int(input('두번째 숫자를 입력하세요: '))

        if (cal == 4 or 5) and num2 == 0:
            print('0으로 나눌 수 없습니다.')
            continue
            
        else:    
            result = calc(num1, num2, cal)
        
        print('결과는 %d 입니다.' % result)
        
    elif cal == 6:
        print('종료를 선택하셨습니다. 프로그램을 종료합니다..')
        break
            
    else:
        print('잘못 입력하셨습니다. 다시 입력해 주세요.')
    print()
