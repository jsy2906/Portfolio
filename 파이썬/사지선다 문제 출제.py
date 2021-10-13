import random

words = {'우유':'milk' , '요거트':'yogurt' , '노트북':'laptop' , '컴퓨터':'computer' , '밥':'rice' , '커피':'coffee' , '영화':'movie'}

keys = list(words.keys())
values = list(words.values())
index = list(range(len(words)))
prob_num = ['가' , '나' , '다' , '라']

count = int(input('몇 문제를 맞추시겠습니까? '))
print()

# 문제
for i in range(count):
    values = list(words.values())
    rand_index = random.choice(index)
    quiz = keys[rand_index]
    ans = values[rand_index]
    
    print('%d. \'%s\'의 영어단어는?' % ((i+1),quiz))

# 사지선다
    values.remove(ans)
    random.shuffle(values)
    ans_list = [ans]
    for i in values[0:3]:
        ans_list.append(i)
    random.shuffle(ans_list)
    for x in range(0,4):
        print('%s) %s' % (prob_num[x], ans_list[x]), end = ' ')  
    print()

# 정답 확인
    my_ans = input('정답은? ')
    ans_num = prob_num[ans_list.index(ans)]
    if my_ans == ans_num:
      print('정답입니다!')
    else:
      print('틀렸습니다,,ㅠ 정답은 %s 입니다.' %ans_num)
    print()

    index.remove(rand_index) # 중복된 문제를 내지 않기 위해
