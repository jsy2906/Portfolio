def checkSeatNum(num) :

# 입력받은 좌석이 유효한 좌석인지 체크하는 함수입니다. 설명 4번을 참고해 True False의 값을 반환하도록 코드를 완성해보세요!
    big = num[0].upper()
    number = int(num[1:])
    if len(num) == 2 or len(num) == 3:
        if (big == 'A' or big == 'B' or big == 'C' or big == 'D' or big == 'E' or big == 'F' or big == 'G' or big == 'H') and \
        (number > 0 and number < 13):
            result = True
        else:
            result = False
    else:
        result = False
    
    return result  
    
def seatNumToIndex(num) :
    # 행의 인덱스 구하기
    row = num[0].upper()
    if row == 'A' :
        i = 0
    elif row == 'B' :
        i = 1
    elif row == 'C' :
        i = 2
    elif row == 'D' :
        i = 3
    elif row == 'E' :
        i = 4
    elif row == 'F' :
        i = 5
    elif row == 'G' :
        i = 6
    else :
        i = 7

    # 열의 인덱스 구하기
    j = int(num[1:]) - 1

    return (i, j)        # 행과 열을 튜플로 반환

def calPrice(r, c) :
    # EC(Economy) : 7,000원, RE(Regular) : 8,000원, SP(Special) : 10,000원
    
    # 좌석에 따라 등급을 확인하고, 알맞은 값을 출력하는 코드를 작성하세요! 
    if seat[r][c] == 'EC':
        price = 7000
    elif seat[r][c] == 'RE':
        price = 8000
    else:
        price = 10000
    
    return price    


seat =  [['EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC'],  
        ['EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC', 'EC'],   
        ['EC', 'EC', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'EC', 'EC'],  
        ['EC', 'EC', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'EC', 'EC'],   
        ['EC', 'EC', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'EC', 'EC'],  
        ['EC', 'EC', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'RE', 'EC', 'EC'],   
        ['SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP'], 
        ['SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP', 'SP']] 

row_name = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'] # 각 행의 이름
num_row = 8                                         # 행의 개수
num_col = 12                                        # 열의 개수

print('EC : 7,000원, RE : 8,000원, SP : 10,000원\n')
print('좌석 배치도 : \n')

print('%3s' % '', end='') # 공백 3개 삽입

for a in range(0, num_col) :   # 좌석 1 번째 줄에 열 번호 삽입
    print('%3s' % str(a+1), end='') 
print() 
    
for i in range(0, num_row) : 
    print('%3s' % row_name[i], end='')  # 좌석의 행 번호 삽입

    for j in range(0, num_col) :   # 좌석 등급('EC', 'RE', 'SP') 삽입
        print('%3s' % seat[i][j], end='')       
    print() 
    
seat_num = input('\n원하는 좌석을 선택해 주세요(예:F11): ')  # 좌석번호 입력

while True :
    if checkSeatNum(seat_num): # 입력된 좌석번호가 유효하면
        print('좌석 번호:', seat_num)# 좌석 번호 출력하기
                              # 티켓 가격 출력하기
        (x, y) = seatNumToIndex(seat_num)
        print('티켓 가격:', calPrice(x,y))
        break        
    else :
                                # 좌석 번호 다시 입력 받기
        seat_num = input('\n원하는 좌석을 선택해 주세요(예:F11): ')
